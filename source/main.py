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
            if sys.argv[2] == 'manhattan':
                heuristic_function = m.manhattan_heuristic
            elif sys.argv[2] == 'euclidean':
                heuristic_function = m.euclidean_heuristic
            elif sys.argv[2] == 'bad':
                heuristic_function = m.bad_heuristic

        elif sys.argv[1] == 'astar':
            heuristic = maze.Heuristic.A_STAR_SEARCH
            if sys.argv[2] == 'manhattan':
                heuristic_function = m.manhattan_heuristic
            elif sys.argv[2] == 'euclidean':
                heuristic_function = m.euclidean_heuristic
            elif sys.argv[2] == 'bad':
                heuristic_function = m.bad_heuristic

        elif sys.argv[1] == 'algo1':
            heuristic = maze.Heuristic.BONUS_ORIENTED_SEARCH
            heuristic_function = m.bonus_oriented_heuristic

        m.solve(algorithm, heuristic, heuristic_function)

        file_name = sys.argv[1]
        if len(sys.argv) == 3:
            file_name += ' ' + sys.argv[2]

        sub_directory = directory.split('/', 1)[1]
        sub_directory = sub_directory.split('.', 1)[0]
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
#       + manhattan             Manhattan distance heuristic
#       + euclidean             Euclidean distance heuristic
#       + bad                   Bad distance estimation heuristic


#2. Sample command:
#   python main.py dfs
#   python main.py bfs
#   python main.py gbfs euclidean
#   python main.py astar bad
#   python main.py map (draw empty map)
