from exception_scripts.interactive.head import run as head_run
from exception_scripts.interactive.mcu import run as interactive_mcu_run

exception_handlers = {
    'head': head_run,
    'interactive_mcu':interactive_mcu_run
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)