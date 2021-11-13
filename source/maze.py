from numpy import sqrt
import utilities as util
import enum



class Algorithm(enum.Enum): 
    DEPTH_FIRST_SEARCH = 1
    BREADTH_FIRST_SEARCH = 2
    HEURISTIC = 3



class Node:
    def __init__(self, coordinate, parent = None, next_move_cost = 1):
        self.coordinate = coordinate
        self.parent = parent
        self.move_cost = 0

        #Evaluate cost to reach this node
        if self.parent != None:
            self.move_cost = self.parent.move_cost + next_move_cost



class Maze:
    def __init__(self):
        self.start_coordinate = None
        self.end_coordinate = None
        self.matrix = []
        self.bonus_points = []
        self.route = []
        self.visited_coordinates = []


    def read_maze(self, path):
        #Read maze map
        self.bonus_points, self.matrix = util.read_file(path)
    
        #Extract START and END
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != 'x':
                    #Mark START
                    if self.matrix[i][j] == 'S':
                        self.start_coordinate = (i, j)

                    #Mark END
                    elif (i == 0) or (i == len(self.matrix) - 1) or (j == 0) or (j == len(self.matrix[0]) - 1):
                        self.end_coordinate = (i, j)  


    def expand(self, current_node):
        children = []

        #Up
        x = current_node.coordinate[0] - 1
        y = current_node.coordinate[1]
        next_move_cost = 1
        if self.matrix[x][y] != 'x':
            #Extract bonus point for next move
            if self.matrix[x][y] == '+':
                for bonus_point in self.bonus_points:
                    if bonus_point[0] == x and bonus_point[1] == y:
                        next_move_cost = bonus_point[2]
                        break

            children.append(Node((x, y), current_node, next_move_cost))

        #Right
        x = current_node.coordinate[0]
        y = current_node.coordinate[1] + 1
        next_move_cost = 1
        if self.matrix[x][y] != 'x':
            #Extract bonus point for next move
            if self.matrix[x][y] == '+':
                for bonus_point in self.bonus_points:
                    if bonus_point[0] == x and bonus_point[1] == y:
                        next_move_cost = bonus_point[2]
                        break

            children.append(Node((x, y), current_node, next_move_cost))

        #Down
        x = current_node.coordinate[0] + 1
        y = current_node.coordinate[1]
        next_move_cost = 1
        if self.matrix[x][y] != 'x':
            #Extract bonus point for next move
            if self.matrix[x][y] == '+':
                for bonus_point in self.bonus_points:
                    if bonus_point[0] == x and bonus_point[1] == y:
                        next_move_cost = bonus_point[2]
                        break

            children.append(Node((x, y), current_node, next_move_cost))

        #Left
        x = current_node.coordinate[0]
        y = current_node.coordinate[1] - 1
        next_move_cost = 1
        if self.matrix[x][y] != 'x':
            #Extract bonus point for next move
            if self.matrix[x][y] == '+':
                for bonus_point in self.bonus_points:
                    if bonus_point[0] == x and bonus_point[1] == y:
                        next_move_cost = bonus_point[2]
                        break

            children.append(Node((x, y), current_node, next_move_cost))

        return children


    def solve(self, algorithm, heuristic_function = None):
        #Select suitable data structure
        frontier = None
        if algorithm == Algorithm.DEPTH_FIRST_SEARCH:
            frontier = util.Stack()
        else:
            frontier = util.Queue()

        #Initialize
        current_node = Node(self.start_coordinate)
        frontier.push(current_node)
        children = []
        
        while not frontier.empty():
            #Extract node at front/back of frontier
            current_node = frontier.peek()
            frontier.pop()

            #Proceed to next step if current node is not visited
            if current_node.coordinate not in self.visited_coordinates:
                self.visited_coordinates.append(current_node.coordinate) #Mark node visited

                #This is the SOLUTION
                if current_node.coordinate == self.end_coordinate:
                    # Backtrack route
                    while current_node:
                        self.route.append(current_node.coordinate)
                        current_node = current_node.parent

                    # Reverse list
                    self.route = list(reversed(self.route))

                    #End function
                    return

                #Expand all possible moves (children)
                #Set current node as parent for each child
                #Add children to frontier
                children = self.expand(current_node)
                for child in children:
                    frontier.push(child)
                
                #Best first search or A* search
                if algorithm == Algorithm.HEURISTIC:
                    frontier.sort(heuristic_function)
                

    def visualize(self, title = ''):
        print(f'The height of the matrix: {len(self.matrix)}')
        print(f'The width of the matrix: {len(self.matrix[0])}')
        util.visualize_maze(self.matrix, self.bonus_points, self.start_coordinate, self.end_coordinate, self.route, self.visited_coordinates, title)


    """Heuristic functions"""
    def manhattan_distance(self, node):
        f = abs(node.coordinate[0] - self.end_coordinate[0]) + abs(node.coordinate[1] - self.end_coordinate[1])
        return f


    def diagonal_distance(self, node):
        f = abs(node.coordinate[0] - self.end_coordinate[0]) + abs(node.coordinate[1] - self.end_coordinate[1]) \
            + (sqrt(2) - 2) * min(abs(node.coordinate[0] - self.end_coordinate[0]), abs(node.coordinate[1] - self.end_coordinate[1]))
        return f
    

    def euclidean_distance(self, node):
        f =  sqrt(pow(node.coordinate[0] - self.end_coordinate[0], 2) + pow(node.coordinate[1] - self.end_coordinate[1], 2))   
        return f


    def manhattan_distance_A_star(self, node):
        f = abs(node.coordinate[0] - self.end_coordinate[0]) + abs(node.coordinate[1] - self.end_coordinate[1])
        g = node.move_cost
        return f + g

    
    def diagonal_distance_A_star(self, node):
        f = abs(node.coordinate[0] - self.end_coordinate[0]) + abs(node.coordinate[1] - self.end_coordinate[1]) \
            + (sqrt(2) - 2) * min(abs(node.coordinate[0] - self.end_coordinate[0]), abs(node.coordinate[1] - self.end_coordinate[1]))
        g = node.move_cost
        return f + g


    def euclidean_distance_A_star(self, node):
        f =  sqrt(pow(node.coordinate[0] - self.end_coordinate[0], 2) + pow(node.coordinate[1] - self.end_coordinate[1], 2))
        g = node.move_cost
        return f + g


    def dijkstra(self, node):
        f = node.move_cost
        return f
    """==================="""