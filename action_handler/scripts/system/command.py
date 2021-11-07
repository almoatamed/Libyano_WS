import os


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))

def command(command):
    #printLine('excecuting command',command)
    try:
        os.system(command)
        return 'done'
    except Exception as e:
        #printLine('Error while excecuting command', e)
        return 'failed'
    