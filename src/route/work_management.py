from xml.dom import NotFoundErr

from cfg import config
from .data_define import AddWorkData, UpdateWorkData
from .resource import WorkResource


def configWorkManagement(Domain):
    session = Domain.session
    ignore_extra = config.IGNORE_EXTRA_FIELDS

    @Domain.registerCommand("add-work")
    def addWork(data, identifier, param):
        verified_data = AddWorkData.create(data, ignore_extra=ignore_extra)
        new_work = WorkResource(**verified_data.serialize())
        session.add(new_work)
        session.commit()
        return new_work.asDict()

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

    @Domain.registerQuery("show-work")
    def showWork(data, identifier, param):
        if identifier < 0:
            results = session.query(WorkResource).all()
            return [result.asDict() for result in results]
        else:
            result = (
                session.query(WorkResource)
                .filter(WorkResource.id == identifier)
                .first()
            )
            if result is None:
                raise NotFoundErr("Work not found")
            return result.asDict()
