from exception_scripts.system_R.status import run as status_run
from exception_scripts.system_R.mode import run as mode_run
from exception_scripts.system_R.action_handler import run as action_handler_run
exception_handlers = {
    'status': status_run,
    'action_handler': action_handler_run,
    'mode': mode_run
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)