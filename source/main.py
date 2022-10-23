import draw_maze as draw
import maze
import sys



def func(directory):
    m = maze.Maze()
    m.read_maze(directory)

    algorithm = None
    heuristic = None
    heuristic_function = None

    #Draw maze with route
    if sys.argv[1] != 'map':
        if sys.argv[1] == 'dfs':
            algorithm = maze.Algorithm.DEPTH_FIRST_SEARCH

        elif sys.argv[1] == 'bfs':
            algorithm = maze.Algorithm.BREADTH_FIRST_SEARCH

        elif sys.argv[1] == 'ucs':
            algorithm = maze.Algorithm.UNIFORM_COST_SEARCH

        elif sys.argv[1] == 'gbfs':
            heuristic = maze.Heuristic.GREEDY_BEST_FIRST_SEARCH
            if sys.argv[2] == '1':
                heuristic_function = m.manhattan_heuristic
            elif sys.argv[2] == '2':
                heuristic_function = m.euclidean_heuristic
            elif sys.argv[2] == '3':
                heuristic_function = m.bad_heuristic

        elif sys.argv[1] == 'astar':
            heuristic = maze.Heuristic.A_STAR_SEARCH
            if sys.argv[2] == '1':
                heuristic_function = m.manhattan_heuristic
            elif sys.argv[2] == '2':
                heuristic_function = m.euclidean_heuristic
            elif sys.argv[2] == '3':
                heuristic_function = m.bad_heuristic

        elif sys.argv[1] == 'algo1':
            heuristic = maze.Heuristic.BONUS_ORIENTED_SEARCH
            heuristic_function = m.bonus_oriented_heuristic

        m.solve(algorithm, heuristic, heuristic_function)

        file_name = sys.argv[1] + '_heuristic_' + sys.argv[2]  if len(sys.argv) == 3 else sys.argv[1]
        sub_directory = directory.split('/', 1)[1]
        sub_directory = sub_directory.split('.', 1)[0]
        sub_directory += '/' + sys.argv[1]
        m.visualize(sub_directory, file_name)

    #Draw empty maze
    else:
       m.visualize()
 
    

if __name__ == '__main__':
    directories = []
    directories.append(draw.draw_level1_maze1())
    directories.append(draw.draw_level1_maze2())
    directories.append(draw.draw_level1_maze3())
    directories.append(draw.draw_level1_maze4())
    directories.append(draw.draw_level1_maze5())
    directories.append(draw.draw_level2_maze1())
    directories.append(draw.draw_level2_maze2())
    directories.append(draw.draw_level2_maze3())
    directories.append(draw.draw_advanced_maze1())
    directories.append(draw.draw_advanced_maze2())
    directories.append(draw.draw_advanced_maze3())

    for directory in directories:
        func(directory)


    
#1. Command format: python main.py <algo/heu> <heu_func>
#   - <algo/heu> - algorithm/heuristic:
#       + dfs                   Depth first search
#       + bfs                   Breadth first search
#       + ucs                   Uniform-cost search
#       + gbfs                  Greedy best first search
#       + astar                 A* search
#       + algo1                 Bonus-oriented search
#   - <heu_func> - heuristic function (for heuristic only)
#       + 1                     Manhattan distance heuristic
#       + 2                     Euclidean distance heuristic
#       + 3                     Bad distance estimation heuristic


#2. Sample command:
#   python main.py dfs
#   python main.py bfs
#   python main.py gbfs 2
#   python main.py astar 3
#   python main.py map (draw empty map)
