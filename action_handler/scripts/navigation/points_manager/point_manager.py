import os


file_name = __file__.split('/')[-1][:-3]
if file_name == '__init__' or file_name == '__init__.':
    file_name = __file__.split('/')[-2]
def printLine(*args): 
    '''
        prints information on the console screen
    '''
    print(file_name+': '+'\n      - '+'\n      - '.join([str(arg) for arg in list(args)]))
    
    
home = os.environ['HOME']
points_file_path = home + '/catkin_ws/src/action_handler/scripts/navigation/points_manager/points.txt'
def fetch_points():
    global points_file_path
    file = open(points_file_path,'r')
    points = file.read()
    return  points

def decode_points():
    file = open(points_file_path,'r')
    points = file.read()
    file.close()
    points = points.split('|')
    points = [point.split('&') for point in points]
    points = {point[0]:point[1:] for point in points }
    return points
    
def parse_points(points):
    return  '|'.join(['&'.join([point]+points[point]) for point in points ])


def del_point(name):
    points = decode_points()
    if name not in points:
        return 'not_found'
    else:
        points.pop(name)
        file = open(points_file_path, 'w+')
        points = parse_points(points)
        file.write(points)
        file.close()
        return 'done'
    
def add_point(name,*args):
    points = decode_points()
    points[name] = list(args)
    points = parse_points(points)
    file = open(points_file_path, 'w+')
    file.write(points)
    file.close()
    
    

    
    
    