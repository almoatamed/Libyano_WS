import os

if not os.path.exists('/usr/bin/mongo'):
    os.system('apt update')
    os.system('apt install mongodb -y')
    os.system('systemctl enable mongodb')
    os.system('systemctl start mongodb')
    
    