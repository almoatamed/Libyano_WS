import rospy
from mcu_msgs.msg import mcu_input



file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
faces = {
 'BLINK': 1,
 'CLOSING': 2,
 'DOLLARS': 3,
 'HAPPY': 4,
 'LOADINGLEFT': 5,
 'LOADINGRIGHT': 6,
 'MAD': 7,
 'MAD2': 8,
 'OPENING': 9,
 'SAD': 10,
 'SNEAKY': 11,
 'SUDDEN': 12,
 'CLEAR': 13
}

mcu_topic = rospy.get_param('/mcu/mcu_input_topic','/mcu/interactive/input')
queue_size = int(rospy.get_param('/global/queue_size', '10'))
pub = rospy.Publisher(mcu_topic, mcu_input,queue_size=queue_size)
mcu_msg = mcu_input()
mcu_msg.Element = 22

def set_eyes(face,color='0', roll='0',period='200',go_default='1'):
    global mcu_msg
    try:
        color = float(int(color, 16))
        roll = float(roll)
        period = float(period)
        go_default = float(go_default)
    except Exception as e:
        #printLine("error while trying to change eyes expression",e)
        return 'failed'
    face = face.upper()
    if face in faces:
        mcu_msg.values = [faces[face],roll,color,period,go_default]
        mcu_msg.Part_and_function = 64
        pub.publish(mcu_msg)
        return 'succeed'
    else:
        return 'not_found'

def set_brightness(brightness):
    global mcu_msg
    try:
        brightness = float(brightness)
    except Exception as e:
        #printLine("error while trying to change brightness",e)
        return 'failed'
    if brightness >250 or brightness <0:
        return 'out_of_boundries'
    mcu_msg.values = [brightness]
    mcu_msg.Part_and_function = 66
    pub.publish(mcu_msg)
    return 'succeed'

