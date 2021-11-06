from scripts.startup import main

Actions = {
    'perform': main.perform,
    'get_current_stage': main.get_current_stage,
    'main_interface': main.main_interface,
    'remote_interface': main.remote_interface,
    'begin': main.begin,
    'performables': main.get_performables,
    'get_manual_controls': main.get_manual_controls
}