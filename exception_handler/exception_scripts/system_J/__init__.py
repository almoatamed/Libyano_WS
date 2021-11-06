from exception_scripts.system_J.action_handler import run as action_handler_run
from exception_scripts.system_J.networking import run as network_run
exception_handlers = {
    'action_handler': action_handler_run,
    'network': network_run
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)