"""To ensure this script to run correctly, please delete input folder"""
import os
import utilities as util



auto_generated = False
directory = os.path.dirname(__file__)
directory = util.remove_suffix(directory, 'source')
directory = os.path.join(directory, 'input/')
if not os.path.exists(directory):
    auto_generated = True
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
    file_name = os.path.join(lvl1_directory, 'input1.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('xxxxxxxxxxxx\n')
            out_file.write('xS         x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x           \n')
            out_file.write('xxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level1_maze2():
    file_name = os.path.join(lvl1_directory, 'input2.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('xxxxxxxxxxxx\n')
            out_file.write('xS         x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('           x\n')
            out_file.write('xxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level1_maze3():
    file_name = os.path.join(lvl1_directory, 'input3.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('xxxxxxxxxxxx\n')
            out_file.write('xS         x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('x          x\n')
            out_file.write('xxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level1_maze4():
    file_name = os.path.join(lvl1_directory, 'input4.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('x                                    x         x x\n')
            out_file.write('x              xxxxxxxxxxxxx  xxxxx  x    x    x x\n')
            out_file.write('xxxxxxxx xxxxxxx                    x     x   x  x\n')
            out_file.write('x    x     x   x xxxxxxxxxxxxx      x    x    x  x\n')
            out_file.write('x       x      x             x     x     x   x   x\n')
            out_file.write('x xxxxxxxxxxxxxx             xxxxxxx    x    x   x\n')
            out_file.write('x                                       x       Sx\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level1_maze5():
    file_name = os.path.join(lvl1_directory, 'input5.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('xxxxxxxx xxxxx\n')
            out_file.write('x     xx xxxxx\n')
            out_file.write('xxxx xxx xxxxx\n')
            out_file.write('x        xxx x\n')
            out_file.write('xxx          x\n')
            out_file.write('xxx xxxxxxxx x\n')
            out_file.write('x   xxxxxxxx x\n')
            out_file.write('xxxxx        x\n')
            out_file.write('xxxxx xxxx xxx\n')
            out_file.write('x S     xx xxx\n')
            out_file.write('xxxxxxxxxx xxx\n')
            out_file.write('xxxxxxxxxx xxx\n')
            out_file.write('xx         xxx\n')
            out_file.write('xxxxxxx xxxxxx\n')
            out_file.write('x     x xxxxxx\n')
            out_file.write('xxx        xxx\n')
            out_file.write('xxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level2_maze1():
    file_name = os.path.join(lvl2_directory, 'input1.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('4\n')
            out_file.write('3 1 -5\n')
            out_file.write('3 2 -5\n')
            out_file.write('3 3 -2\n')
            out_file.write('1 20 -10\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('xS                   x\n')
            out_file.write('x                    x\n')
            out_file.write('x                     \n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level2_maze2():
    file_name = os.path.join(lvl2_directory, 'input2.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('5\n')
            out_file.write('5 14 -4\n')
            out_file.write('6 5 -1\n')
            out_file.write('7 5 -1\n')
            out_file.write('7 1 -1\n')
            out_file.write('8 1 -1\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('x   x   xx xx        x\n')
            out_file.write('x     x     xxxxxxxxxx\n')
            out_file.write('x x    xx  xxxx xxx xx\n')
            out_file.write('  x x x x xx   xxxx  x\n')
            out_file.write('x   x      xx  xx  x x\n')
            out_file.write('xx xx xxxx     xx  x x\n')
            out_file.write('x  xx xxx  x x  xx   x\n')
            out_file.write('x          x x Sx x  x\n')
            out_file.write('xxxxx x  x x x     x x\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_level2_maze3():
    file_name = os.path.join(lvl2_directory, 'input3.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('10\n')
            out_file.write('2 3 -9\n')
            out_file.write('2 8 -7\n')
            out_file.write('5 7 -1\n')
            out_file.write('5 14 -6\n')
            out_file.write('6 14 -2\n')
            out_file.write('6 5 -2\n')
            out_file.write('7 5 -1\n')
            out_file.write('7 1 -3\n')
            out_file.write('8 1 -4\n')
            out_file.write('9 10 -10\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('x   x   xx xx        x\n')
            out_file.write('x     x     xxxxxxxxxx\n')
            out_file.write('x x    xx  xxxx xxx xx\n')
            out_file.write('  x x x x xx   xxxx  x\n')
            out_file.write('x          xx  xx  x x\n')
            out_file.write('xx xx xxxx     xx  x x\n')
            out_file.write('x  xx xxx  x x  xx   x\n')
            out_file.write('x          x x Sx x  x\n')
            out_file.write('xxxxx x      x     x x\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_advanced_maze1():
    file_name = os.path.join(advanced_directory, 'input1.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('2\n')
            out_file.write('2 2 3 10 1\n')
            out_file.write('2 18 3 15 2\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('xS                   x\n')
            out_file.write('x                    x\n')
            out_file.write('x                     \n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_advanced_maze2():
    file_name = os.path.join(advanced_directory, 'input2.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('3\n')
            out_file.write('8 1 4 4 1\n')
            out_file.write('6 12 3 1 2\n')
            out_file.write('5 13 1 18 3\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('x   x   xx xx        x\n')
            out_file.write('x     x      xxxxxxxxx\n')
            out_file.write('x x    xx  x xx xxx xx\n')
            out_file.write('     xx x xx   xxxx  x\n')
            out_file.write('x           x  xx  x x\n')
            out_file.write('xx xx xxxx     xx  x x\n')
            out_file.write('x  xx xxx  x x  xx   x\n')
            out_file.write('x          x x Sx x  x\n')
            out_file.write('xxxxx x  x x x     x x\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name

def draw_advanced_maze3():
    file_name = os.path.join(advanced_directory, 'input3.txt')
    if auto_generated:
        with open(file_name, 'w') as out_file:
            out_file.write('0\n')
            out_file.write('4\n')
            out_file.write('7 1 1 45 1\n')
            out_file.write('5 29 7 5 2\n')
            out_file.write('5 11 1 16 3\n')
            out_file.write('3 48 2 1 4\n')
            out_file.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
            out_file.write('x                                    x         x x\n')
            out_file.write('x              xxxxxxxxxxxxx  xxxxx  x    x    x x\n')
            out_file.write('xxxxxxxx xxxxxxx                    x     x   x  x\n')
            out_file.write('x    x     x   x xxxxxxxxxxxxx      x    x    x  x\n')
            out_file.write('x       x                          x     x   x   x\n')
            out_file.write('x xxxxxxxxxxxxxx             xxxxxxx    x    x   x\n')
            out_file.write('x                                       x       Sx\n')
            out_file.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        out_file.close()
    return file_name