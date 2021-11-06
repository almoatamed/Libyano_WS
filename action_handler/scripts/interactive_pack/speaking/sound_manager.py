import os

def playsound(path):
    os.system('mpg123 '+path)

file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))


printLine('Starting Voice Generater')

home = os.environ['HOME']
sounds_path = home + '/catkin_ws/src/action_handler/scripts/interactive/speaking/sounds/'
playing = False
printLine('Voice manager is ready')
def generate(phrase, lang,name):
    printLine('generating sound', phrase, name)
    os.chdir(home + '/catkin_ws/src/action_handler/scripts/interactive/speaking/generaters')
    os.system('/usr/bin/python3 generate_'+lang+'.py "' + phrase + '"' + ' "' + name + '"' )


def play_temp(lang,phrase):
    global playing
    if playing:
        return 'speaking'
    printLine('testing sound', phrase, lang)
    try:
        playing = True
        generate(phrase,lang,'temp')   
        os.system('mpg123 ' +sounds_path+'temp.mp3')
        os.remove(sounds_path+'temp.mp3')
        playing = False
        return 'done'
    except Exception as e:
        printLine('error while playing sound',e)
        playing = False
        return 'failed' 

def sounds_list():
    printLine('listing sound files')
    files =  [f[:-4] for f in os.listdir(sounds_path) if ( os.path.isfile(os.path.join(sounds_path, f)) and f[-3:] == 'mp3')] 
    printLine(*files)
    sound_list = []
    for file in files:
        content_file = open(sounds_path+file+'_content.txt')
        content = content_file.read()
        content_file.close()
        sound_list.append(file+'&'+content)
    return '%'.join(sound_list)

def save_sound(lang,phrase,name):
    printLine('saving sound', phrase)
    try:
        generate(phrase,lang,name)
        file = open(sounds_path+name+'_content.txt','w+')
        file.write(phrase)
        file.close()
        return 'done'
    except Exception as e:
        printLine('error while saving sound',e)
        return 'failed'

def del_sound(name):
    printLine('deleting sound file ', name)
    files = [f[:-4] for f in os.listdir(sounds_path) if ( os.path.isfile(os.path.join(sounds_path, f)) and f[-3:] == 'mp3')] 
    if name not in files:
        printLine('fine not found ', name)
        return 'not_found'
    try:
        os.remove(sounds_path+name+'.mp3')
        os.remove(sounds_path+name+'_content.txt')
        printLine('file has been deleted', name)
        return 'done'
    except Exception as e:
        printLine('Error while deleting sound file', e)
        return 'failed'

def play_saved_file(name):
    printLine('playing sound file ', name)
    files = [f[:-4] for f in os.listdir(sounds_path) if ( os.path.isfile(os.path.join(sounds_path, f)) and f[-3:] == 'mp3')] 
    if name not in files: 
        printLine('file not found')
        return 'not_found'
    try:
        printLine('file found attempting to play',sounds_path+name+'.mp3')
        os.system('mpg123 ' + sounds_path+name+'.mp3')
        return  'done'
    except Exception as e:
        printLine('Error while playing sound', e)
        return 'failed'

