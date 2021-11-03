import os


path = os.path.dirname(__file__).removesuffix('source')


def draw_maze1():
    filename = os.path.join(path, 'test/maze_map1.txt')
    with open(filename, 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x   x   xx xx        x\n')
        outfile.write('x     x     xxxxxxxxxx\n')
        outfile.write('x x    xx  xxxx xxx xx\n')
        outfile.write('  xxx   x xx   xxxx  x\n')
        outfile.write('x    x     x   xxxx  x\n')
        outfile.write('x x        xx  xx  x x\n')
        outfile.write('xxxxxxx x      xx  x x\n')
        outfile.write('xxxxxxxxx  x x  xx   x\n')
        outfile.write('x          x x Sx x  x\n')
        outfile.write('xxxxx x  x x x     x x\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxx')

    return filename


def draw_maze2():
    filename = os.path.join(path, 'test/maze_map2.txt')
    with open(filename, 'w') as outfile:
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
    
    return filename