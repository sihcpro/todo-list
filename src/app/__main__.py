from http.server import BaseHTTPRequestHandler, HTTPServer

from base.connection import initEngine
from base.domain import Domain
from cfg import config
from route.work_management import configWorkManagement
from route.work_viewer import configWorkViewer


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("", config.APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    initEngine()
    configWorkManagement(Domain)
    configWorkViewer(Domain)
    run(handler_class=Domain)
