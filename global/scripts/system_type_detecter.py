import subprocess
import os

home = os.environ['HOME']

x = subprocess.check_output('sudo lshw'.split(' ')).decode().split('\n')
p = []
for i,index in zip(x,range(len(x))):
    if 'product' in i:
        p.append(i.split(':'))

system_type = p[0][1].split(' ')[1][0]
if system_type == 'N' or system_type == u'N':
    system_type = 'J'
if system_type not in ['R', 'J']:
    system_type = 'G'

os.system('echo "export SYSTEM_TYPE=' + system_type +'" >> $HOME/.bashrc' )
file = open(home+'/catkin_ws/src/global/config/system_type.yaml','w+')
file.write('system_type: ' + system_type)
file.close()

file = open(home+'/catkin_ws/src/action_handler/launch/action_server.launch','w+')
file.write(
'''<launch>
    <param name="/action/action_service_name" value="/action" />
    <node name="%(action_handler_node_name)s" pkg="action_handler" type="action_handler.py" output="screen"/>
    <node name="%(action_server_node_name)s" pkg="action_handler" type="action_server.py" output="screen"/>
</launch>''' % {'action_handler_node_name':'action_handler_'+system_type,
                'action_server_node_name':'action_server_'+system_type}
)
file.close()
