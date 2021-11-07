import rospy
from geometry_msgs.msg import Vector3



file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args):
    '''
        prints information on the console screen
    '''
    global name
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
queue_size = int(rospy.get_param('/global/queue_size', '10'))
pub = rospy.Publisher('/led_strip', Vector3,queue_size=queue_size)
mcu_msg = Vector3()

def set_color(red,green,blue):
    global mcu_msg
    try:
        red = int(red)
        green = int(green)
        blue = int(blue)
    except Exception as e:
        #printLine("error while trying to change eyes expression",e)
        return 'failed'
    if 0<=red<=255 and 0<=green<=255 and 0<=blue<=255:
        mcu_msg.x = red
        mcu_msg.y = green
        mcu_msg.z = blue
        pub.publish(mcu_msg)
        return 'succeed'
    else:
        return 'not_Valid_colors'


