from scripts.system import command
from scripts.system import controlled_process_manager
from scripts.system import dispatch
from scripts.system import kill

Actions = {
    'command': command.command,
    'start_controlled_process': controlled_process_manager.start_controlled_process,
    'kill_controlled_process': controlled_process_manager.kill_process,
    'dispatch': dispatch.dispatch,
    'kill_node': kill.kill_node
}