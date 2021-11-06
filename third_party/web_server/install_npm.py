import os


home = os.environ['HOME']

if not os.path.exists('/usr/bin/node'):
    os.chdir(home)
    os.system('curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -')
    os.system('sudo apt-get install -y nodejs')