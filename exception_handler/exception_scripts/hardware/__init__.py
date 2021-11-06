from exception_scripts.hardware.laser_scanner import run as laser_scanner_run
from exception_scripts.hardware.movement_mcu import run as movement_mcu_run

exception_handlers = {
    'laser_scanner': laser_scanner_run,
    'movement_mcu': movement_mcu_run
}


def run(current_status):
    for handler in exception_handlers:
        exception_handlers[handler](current_status)