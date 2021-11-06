import draw_maze as draw
import maze as maze
import sys
from multiprocessing import Process



def func(path):
    m = maze.Maze()
    m.read_maze(path)

    algorithm = None
    heuristic_function = None
    figure_title = {}
    figure_title['dfs'] = 'Depth first search'
    figure_title['bfs'] = 'Breath first search'
    figure_title['best manhattan'] = 'Greedy best first search - Manhattan distance'
    figure_title['best diagonal'] = 'Greedy best first search - Diagonal distance'
    figure_title['best euclidean'] = 'Greedy best first search - Euclidean distance'
    figure_title['A manhattan'] = 'A* search - Manhattan distance'
    figure_title['A diagonal'] = 'A* search - Diagonal distance'
    figure_title['A euclidean'] = 'A* search - Euclidean distance'

    #Draw maze with route
    if sys.argv[1] != 'map':
        if sys.argv[1] == 'dfs':
            algorithm = maze.Algorithm.DEPTH_FIRST_SEARCH

        elif sys.argv[1] == 'bfs':
            algorithm = maze.Algorithm.BREADTH_FIRST_SEARCH

        elif sys.argv[1] == 'best':
            algorithm = maze.Algorithm.BEST_FIRST_SEARCH
            if sys.argv[2] == 'manhattan':
                heuristic_function = m.manhattan_distance
            elif sys.argv[2] == 'euclidean':
                heuristic_function = m.euclidean_distance
            elif sys.argv[2] == 'diagonal':
                heuristic_function = m.diagonal_distance

        elif sys.argv[1] == 'A':
            algorithm = maze.Algorithm.A_STAR_SEARCH
            if sys.argv[2] == 'manhattan':
                heuristic_function = m.manhattan_distance_A_star
            elif sys.argv[2] == 'diagonal':
                heuristic_function = m.diagonal_distance_A_star
            elif sys.argv[2] == 'euclidean':
                heuristic_function = m.euclidean_distance_A_star

        m.solve(algorithm, heuristic_function)

        str = sys.argv[1]
        if len(sys.argv) == 3:
            str += ' ' + sys.argv[2]

        m.visualize(figure_title[str])

    #Draw empty maze
    else:
        m.visualize()

    


if __name__ == '__main__':
    paths = []
    paths.append(draw.draw_maze1())
    paths.append(draw.draw_maze2())

    for path in paths:
        proc = Process(target = func, args = (path,))
        proc.start()
    
    
#1. Command format: python main.py <algo> <heu_func>
#   - <algo> - algorithm:
#       + dfs - depth first search
#       + bfs - breadth first search
#       + best - best first search
#       + A - A* search
#   - <heu_func> - heuristic function (for best and A only)
#       + manhattan - manhattan distance
#       + diagonal - diagonal distance
#       + euclidean - euclidean distance

#2. Sample command:
#   python main.py dfs
#   python main.py bfs
#   python main.py best euclidean
#   python main.py A diagonal
#   python main.py map (draw empty map)