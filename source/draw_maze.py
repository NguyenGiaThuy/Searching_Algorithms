import os
import utilities as util



directory = os.path.dirname(__file__)
directory = util.remove_suffix(directory, 'source')
directory = os.path.join(directory, 'input/')
if not os.path.exists(directory):
    os.makedirs(directory)

lvl1_directory = os.path.join(directory, 'level_1/')
if not os.path.exists(lvl1_directory):
    os.makedirs(lvl1_directory)

lvl2_directory = os.path.join(directory, 'level_2/')
if not os.path.exists(lvl2_directory):
    os.makedirs(lvl2_directory)

advanced_directory = os.path.join(directory, 'advance/')
if not os.path.exists(advanced_directory):
    os.makedirs(advanced_directory)



def draw_level1_maze1():
    file_name = os.path.join(lvl1_directory, 'input_1.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('0\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('x   x   xx xx        x\n')
            outfile.write('x     x     xxxxxxxxxx\n')
            outfile.write('x x    xx  xxxx xxx xx\n')
            outfile.write('x xxx   x xx   xxxx  x\n')
            outfile.write('x    x     x   xxxx  x\n')
            outfile.write('x x        xx  xx  x x\n')
            outfile.write('xxxxxxx x      xx  x x\n')
            outfile.write('xxxxxxxxx  x x  xx   x\n')
            outfile.write('x          x x Sx x  x\n')
            outfile.write('xxxxx x  x x x     x x\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_level1_maze2():
    file_name = os.path.join(lvl1_directory, 'input_2.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('0\n')
            outfile.write('xxxxxxxxxxxxx\n')
            outfile.write('xS         xx\n')
            outfile.write('x xxxxxxxx+xx\n')
            outfile.write('x x        xx\n')
            outfile.write('x x xxxxxxxxx\n')
            outfile.write('x            \n')
            outfile.write('x xxxxxxxxxxx\n')
            outfile.write('x      xxxxxx\n')
            outfile.write('xxxxxxxxxxxxx')
    return file_name

def draw_level1_maze3():
    file_name = os.path.join(lvl1_directory, 'input_3.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('0\n')
            outfile.write('xxxxxxxxxxxxx\n')
            outfile.write('       x xxxx\n')
            outfile.write('x x x x  xxxx\n')
            outfile.write('x x   x   xxx\n')
            outfile.write('x x     x xxx\n')
            outfile.write('x x x x xxxxx\n')
            outfile.write('x x x   S xxx\n')
            outfile.write('x xxxxxxx xxx\n')
            outfile.write('x         xxx\n')
            outfile.write('xxxxxxxxxxxxx')
    return file_name

def draw_level1_maze4():
    file_name = os.path.join(lvl1_directory, 'input_4.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('0\n')
            outfile.write('xxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('xxxxxxxx x xxxxxxxxxxx xxxxxxxxxxx xx\n')
            outfile.write('x        x    xxxxxxxx xxxxxxxxxxx xx\n')
            outfile.write('x xxxxxx xxxx              xxx     xx\n')
            outfile.write('x xxxxxx xxxx xxxxxx xxx xxxxx xxxxxx\n')
            outfile.write('x x           xxxxxx xxx  xxxx xxxxxx\n')
            outfile.write('x x xxxxxxxxx xxx     xx xxx    xxxxx\n')
            outfile.write('x x xxxxxxxxx xxx xxx xx xxx xxxxxxxx\n')
            outfile.write('x xxxxx           xxx               x\n')
            outfile.write('x xxx xxxxx xxxxx     xxxxxx xxxxxxxx\n')
            outfile.write('x xxx xxxxx xxxxxxxx xxxxxxx xxx xxxx\n')
            outfile.write('x xxx xxxxx        x    S xx        x\n')
            outfile.write('x           xxxxx xxxxxxx xx x xxx xx\n')
            outfile.write('x x xxxxxxxxxxxxx         xxxx xx  xx\n')
            outfile.write('x   xxxxxxxxxxxxxxxxxxxxxxxxxx xxx xx\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_level1_maze5():
    file_name = os.path.join(lvl1_directory, 'input_5.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('0\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxx\n')
            outfile.write('xxxxxxxx                     xx xxxxx\n')
            outfile.write('xx  x xxxxxx xxxxxxxxxxxxxx xxx xxxxx\n')
            outfile.write('xx xx x                         xxx x\n')
            outfile.write('xx xx xxxxxxxxxxx xxxxxxxx        x x\n')
            outfile.write('xx x  xxxxxxxx    xxxxxxxx xxxxxxxx x\n')
            outfile.write('xx x xxxx   xx xxxxxx      xxxxxxxx x\n')
            outfile.write('x    xxxxxx     xxxxx xxxxxx        x\n')
            outfile.write('xxxx xx xxx xxxxxxxxx xxxxxx xxxx xxx\n')
            outfile.write('xxxx xx xx S                   xx xxx\n')
            outfile.write('xxx     xx xxxxxxxx xxxxxxxxxxxxx xxx\n')
            outfile.write('xxxxxxx xxxxxxxxxxx xx xxxxxxxxxx xxx\n')
            outfile.write('x    x              xx xx         xxx\n')
            outfile.write('xxxx xx x xxxxx xxx xx xxxxxxxxxxxxxx\n')
            outfile.write('xxx     xxx     xxx          xxxxxxxx\n')
            outfile.write('xxxxxxxxxxx xxxxxxxxxxxxxx        xxx\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_level2_maze1():
    file_name = os.path.join(lvl2_directory, 'input_1.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('2\n')
            outfile.write('4 5 -2\n')
            outfile.write('7 9 -5\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('x   x   xx xx        x\n')
            outfile.write('x     x     xxxxxxxxxx\n')
            outfile.write('x x    xx  xxxx xxx xx\n')
            outfile.write('  x x+x x xx   xxxx  x\n')
            outfile.write('x   x      xx  xx  x x\n')
            outfile.write('xx xx xxxx     xx  x x\n')
            outfile.write('x  xx xxx+ x x  xx   x\n')
            outfile.write('x          x x Sx x  x\n')
            outfile.write('xxxxx x  x x x     x x\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_level2_maze2():
    file_name = os.path.join(lvl2_directory, 'input_2.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('5\n')
            outfile.write('5 14 -4\n')
            outfile.write('6 5 -1\n')
            outfile.write('7 5 -1\n')
            outfile.write('7 1 -1\n')
            outfile.write('8 1 -1\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('x   x   xx xx        x\n')
            outfile.write('x     x     xxxxxxxxxx\n')
            outfile.write('x x    xx  xxxx xxx xx\n')
            outfile.write('  x x x x xx   xxxx  x\n')
            outfile.write('x   x      xx +xx  x x\n')
            outfile.write('xx xx+xxxx     xx  x x\n')
            outfile.write('x+ xx+xxx  x x  xx   x\n')
            outfile.write('x+         x x Sx x  x\n')
            outfile.write('xxxxx x  x x x     x x\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_level2_maze3():
    file_name = os.path.join(lvl2_directory, 'input_3.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('10\n')
            outfile.write('2 3 -9\n')
            outfile.write('2 8 -7\n')
            outfile.write('5 7 -1\n')
            outfile.write('5 14 -6\n')
            outfile.write('6 14 -2\n')
            outfile.write('6 5 -2\n')
            outfile.write('7 5 -1\n')
            outfile.write('7 1 -3\n')
            outfile.write('8 1 -4\n')
            outfile.write('9 10 -10\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('x   x   xx xx        x\n')
            outfile.write('x  +  x +   xxxxxxxxxx\n')
            outfile.write('x x    xx  xxxx xxx xx\n')
            outfile.write('  x x x x xx   xxxx  x\n')
            outfile.write('x      +   xx +xx  x x\n')
            outfile.write('xx xx+xxxx    +xx  x x\n')
            outfile.write('x+ xx+xxx  x x  xx   x\n')
            outfile.write('x+         x x Sx x  x\n')
            outfile.write('xxxxx x   +  x     x x\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_advanced_maze1():
    file_name = os.path.join(advanced_directory, 'input_1.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('4\n')
            outfile.write('3 1 -5\n')
            outfile.write('3 2 -5\n')
            outfile.write('3 3 -2\n')
            outfile.write('1 20 -10\n')
            outfile.write('0\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('xS                   x\n')
            outfile.write('x                    x\n')
            outfile.write('x                     \n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
    return file_name

def draw_advanced_maze2():
    file_name = os.path.join(advanced_directory, 'input_2.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as outfile:
            outfile.write('2\n')
            outfile.write('3 1 -5\n')
            outfile.write('1 20 -10\n')
            outfile.write('2\n')
            outfile.write('2 2 3 10 1\n')
            outfile.write('2 18 3 15 2\n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            outfile.write('xS                   x\n')
            outfile.write('x                    x\n')
            outfile.write('x                     \n')
            outfile.write('xxxxxxxxxxxxxxxxxxxxxx')
    return file_name