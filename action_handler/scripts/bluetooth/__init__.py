from scripts.bluetooth.connect.connect import connect, connect_default
from scripts.bluetooth.connected.connected import connected, reset_volume
from scripts.bluetooth.disconnect.disconnect import disconnect
from scripts.bluetooth.scan.scan import scan
from scripts.bluetooth.default.default import set, get, clear

# #print('Importing Bluetooth Actions')


Actions = {
    'reset_volume': reset_volume,
    'connect':connect,
    'connect_default': connect_default,
    'connected':connected,
    'disconnect':disconnect,
    'scan':scan,
    'set_default': set,
    'get_default': get,
    'clear_default': clear,
}
