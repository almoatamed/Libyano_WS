from exception_scripts.movement.driver import run as driver_run

exception_handlers = {
    'driver': driver_run 
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)