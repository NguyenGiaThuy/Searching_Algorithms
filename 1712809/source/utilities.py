import matplotlib.pyplot as plt
import os



def visualize_maze(matrix, bonuses, waypoints, start, end, path = None, path_cost = 0, visited_coordinates = None, sub_directory = '', file_name = ''):
    """
    Args:
        1. matrix: The matrix read from the input file,
        2. bonuses: The array of bonus points,
        3. start, end: The starting and ending points,
        4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """

    figure_size = (len(matrix[0]), len(matrix))
    legend_size = figure_size[0] * figure_size[1] / 2
    figure_dpi = 300
    font_size = 20

    #1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']

    if path:
        direction = []
        for i in range(1, len(path)):
                if path[i][0] - path[i - 1][0] > 0:
                    direction.append('v') #v
                elif path[i][0] - path[i - 1][0] < 0:
                    direction.append('^') #^        
                elif path[i][1] - path[i - 1][1] > 0:
                    direction.append('>') #>
                elif path[i][1] - path[i - 1][1] < 0:
                    direction.append('<') #<

        direction.pop(0)

    #2. Drawing the map
    ax = plt.figure(dpi = figure_dpi, figsize = figure_size).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls], [-i[0] for i in walls], marker = 'X', s = legend_size, color = 'black')
    
    for bonus in bonuses:
        bonus_color = 'blue'
        if bonus[2] == -5:
            bonus_color = 'green'
        elif bonus[2] == -10:
            bonus_color = 'red'
        plt.scatter(bonus[1], -bonus[0], marker = 'P', s = legend_size, color = bonus_color)

    for waypoint in waypoints:
        index = chr(waypoint[4] + 48)
        plt.text(waypoint[1], -waypoint[0], 'w' + index, color = 'teal', horizontalalignment = 'center', verticalalignment = 'center', size = font_size)
        plt.text(waypoint[3], -waypoint[2], 'w' + index, color = 'teal', horizontalalignment = 'center', verticalalignment = 'center', size = font_size)

    plt.scatter(start[1], -start[0], marker = '*', s = legend_size, color = 'gold')

    if visited_coordinates:
        for i in range(len(visited_coordinates)):
            if visited_coordinates[i] not in path and visited_coordinates[i] != start:
                plt.scatter(visited_coordinates[i][1], -visited_coordinates[i][0], marker = '*', color = 'silver', s = legend_size)

    if path:
        for i in range(len(path) - 2):
            is_overlapped = False
            
            for waypoint in waypoints:
                if (path[i + 1][0] == waypoint[0] and path[i + 1][1] == waypoint[1]) or (path[i + 1][0] == waypoint[2] and path[i + 1][1] == waypoint[3]):
                    is_overlapped = True
                    break
            
            if not is_overlapped:
                plt.scatter(path[i + 1][1], -path[i + 1][0], marker = direction[i], color = 'silver', s = legend_size)

    if end != None:
        plt.text(end[1], -end[0], 'EXIT', color = 'red', horizontalalignment = 'center', verticalalignment = 'center', size = font_size)
    plt.xticks([])
    plt.yticks([])
    plt.suptitle(file_name, size = font_size)

    file_name = file_name.split(' ', 1)[0] if ' ' in file_name else file_name
    directory = os.path.dirname(__file__)
    directory = remove_suffix(directory, 'source')
    directory = os.path.join(directory, 'output/' + sub_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    figure_file_name = os.path.join(directory, file_name + '.jpg')
    path_cost_file_name = os.path.join(directory, file_name  + '.txt')
    plt.savefig(figure_file_name, format = 'jpg', dpi = figure_dpi)
    write_path_cost(path_cost_file_name, path_cost)

    print(f'Starting point (x, y) = {start[0], start[1]}')

    if end != None:
        print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonuses):
        print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')



def write_path_cost(file_name, path_cost):
    path_cost = path_cost if path_cost > 0 else 'NO'
    with open(file_name, 'w') as outfile:
        outfile.write(str(path_cost))
    outfile.close()
    return file_name
    


def read_file(file_name):
    file = open(file_name, 'r')

    # Extraction bonuses
    bonuses = []
    bonuses_count = int(next(file)[:-1])
    for i in range(bonuses_count):
        x, y, reward = map(int, next(file)[:-1].split(' '))
        bonuses.append((x, y, reward))
    
    # Extraction waypoints (if available)
    waypoints = []
    if 'advance' in file_name:
        waypoints_count = int(next(file)[:-1]) 
        for i in range(waypoints_count):
            in_x, in_y, out_x, out_y, legend = map(int, next(file)[:-1].split(' '))
            waypoints.append((in_x, in_y, out_x, out_y, legend))

    text = file.read()
    matrix = [list(i) for i in text.splitlines()]
    file.close()

    return matrix, bonuses, waypoints



def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string



class Queue:
    def __init__(self):
        self.items = []
    

    def peek(self):
        return self.items[0]
    

    def push(self, item):
        self.items.append(item)
    

    def pop(self):
        if not self.empty():
            self.items.pop(0)


    def empty(self):
        return len(self.items) == 0

    
    def sort(self, criteria):
        self.items.sort(key = criteria)
