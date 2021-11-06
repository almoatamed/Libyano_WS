from exception_scripts.web_server.rosbridge import run as rosbridge_run
from exception_scripts.web_server.backend import run as backend_run
from exception_scripts.web_server.interface import run as interface_run
exception_handlers = {
    'rosbridge': rosbridge_run,
    'backend': backend_run,
    'interface': interface_run
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)