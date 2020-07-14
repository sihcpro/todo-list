from http.server import BaseHTTPRequestHandler, HTTPServer

from base.connection import init_engine
from base.domain import Domain
from cfg import config
from route.work_management import config_work_management
from route.work_viewer import config_work_viewer


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("", config.APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    init_engine()
    config_work_management(Domain)
    config_work_viewer(Domain)
    run(handler_class=Domain)
