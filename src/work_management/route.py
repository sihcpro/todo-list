from cfg import config
from xml.dom import NotFoundErr
from .data_define import AddWorkData, UpdateWorkData
from .resource import WorkResource


def config_work_management(Domain):
    session = Domain.session

    ignore_extra = config.IGNORE_EXTRA_FIELDS

    @Domain.registerQuery("show-work")
    def showWork(data, identifier, param):
        results = session.query(WorkResource).all()
        return [result.as_dict() for result in results]

    @Domain.registerCommand("add-work")
    def addWork(data, identifier, param):
        verified_data = AddWorkData.create(data, ignore_extra=ignore_extra)
        new_work = WorkResource(**verified_data.serialize())
        session.add(new_work)
        session.commit()
        return new_work.as_dict()

    @Domain.registerCommand("update-work")
    def updateWork(data, identifier, param):
        if not data:
            return {
                "message": "OK",
                "count": 0,
            }
        verified_data = UpdateWorkData.create(data, ignore_extra=ignore_extra)
        updated_work_count = (
            session.query(WorkResource)
            .filter(WorkResource.id == identifier)
            .update(verified_data.serialize())
        )
        if updated_work_count > 0:
            return {"message": "OK", "count": updated_work_count}
        else:
            raise NotFoundErr("Work not found")

    @Domain.registerCommand("delete-work")
    def deleteWork(data, identifier, param):
        deleted_work_count = (
            session.query(WorkResource)
            .filter(WorkResource.id == identifier)
            .delete()
        )
        if deleted_work_count > 0:
            return {"message": "OK", "count": deleted_work_count}
        else:
            raise NotFoundErr("Work not found")
