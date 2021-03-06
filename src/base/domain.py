import json
import urllib.parse as urlparse
from functools import wraps
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs, unquote

from cfg import logger
from .connection import initSession


def loadUrl(path) -> (str, int, dict):
    request = urlparse.urlparse(path)
    request_paths = request.path.split("/")
    request_target = request_paths[1]
    request_identifier = (
        int(request_paths[2]) if len(request_paths) > 2 else -1
    )
    request_params = parse_qs(unquote(request.query))
    logger.debug("param %r", request_params)
    return request_target, request_identifier, request_params


def loadData(request) -> dict:
    length = int(request.headers.get("content-length"))
    if length == 0:
        return {}
    request_data = json.loads(request.rfile.read(length))
    return request_data


class Domain(SimpleHTTPRequestHandler):
    query_handler = {}
    command_handler = {}
    session = initSession()

    def do_GET(self):
        logger.debug("GET - %s : %r", self.client_address[0], self.path)

        try:
            request_target, request_identifier, request_params = loadUrl(
                self.path
            )
            if request_target in Domain.query_handler:
                func = Domain.query_handler[request_target]
                response_data = func(
                    data=None,
                    identifier=request_identifier,
                    param=request_params,
                )
                self.responseJson(code=200, data=response_data)
            else:
                logger.debug(
                    f"{request_target} not in {Domain.query_handler.keys()}"
                )
                raise Exception("Not found!")
        except Exception as e:
            self.session.rollback()
            logger.exception(e)
            self.responseJson(
                code=500,
                data={
                    "status": 500,
                    "message": str(e),
                    "data": getattr(e, "data", {}),
                },
            )

    def do_POST(self):
        logger.debug("POST - %s : %r", self.client_address[0], self.path)

        try:
            request_target, request_identifier, request_params = loadUrl(
                self.path
            )
            if request_target in Domain.command_handler:
                request_data = loadData(self)
                logger.debug("/COMMAND/ param %s", request_data)
                func = Domain.command_handler[request_target]
                response_data = func(
                    data=request_data,
                    identifier=request_identifier,
                    param=request_params,
                )
                self.responseJson(code=200, data=response_data)
            else:
                logger.debug(
                    f"{request_target} not in {Domain.command_handler.keys()}"
                )
                raise Exception("Not found!")
            self.session.commit()
        except Exception as e:
            logger.exception(e)
            self.responseJson(
                code=500,
                data={
                    "status": 500,
                    "message": str(e),
                    "data": getattr(e, "data", {}),
                },
            )

    def responseJson(self, code: int, data: dict):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = json.dumps(data)
        self.wfile.write(bytes(data, "utf-8"))

    @classmethod
    def registerCommand(cls, command_name):
        @wraps(command_name)
        def wrapRegisterCommand(func):
            logger.debug("/COMMAND/ %r", command_name)
            Domain.command_handler[command_name] = func

        return wrapRegisterCommand

    @classmethod
    def registerQuery(cls, query_name):
        @wraps(query_name)
        def wrapRegisterQuery(func):
            logger.debug("/QUERY/ %r", query_name)
            cls.query_handler[query_name] = func

        return wrapRegisterQuery
