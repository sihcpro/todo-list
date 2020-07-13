from http.server import BaseHTTPRequestHandler, HTTPServer

from base.connection import init_engine
from base.domain import Domain
from cfg import config
from work_management.route import config_work_management


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("", config.APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    init_engine()
    config_work_management(Domain)
    run(handler_class=Domain)
