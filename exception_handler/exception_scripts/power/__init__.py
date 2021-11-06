from exception_scripts.power.battery import run as batter_run


exception_handlers = {
    'run': batter_run
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)