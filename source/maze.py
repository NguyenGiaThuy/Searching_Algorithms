from numpy import sqrt
import utilities as util
import enum



class Algorithm(enum.Enum): 
    DEPTH_FIRST_SEARCH = 1
    BREADTH_FIRST_SEARCH = 2
    UNIFORM_COST_SEARCH = 3



class Heuristic(enum.Enum): 
    GREEDY_BEST_FIRST_SEARCH = 1
    A_STAR_SEARCH = 2
    BONUS_ORIENTED_SEARCH = 3 



class Node:
    def __init__(self, coordinate, parent = None, next_move_cost = 1):
        self.coordinate = coordinate
        self.parent = parent
        self.cost_so_far = 0

        # Evaluate cost to reach this node
        if self.parent != None:
            self.cost_so_far = self.parent.cost_so_far + next_move_cost



class Maze:
    def __init__(self):
        self.matrix = []
        self.bonuses = []
        self.waypoints = []
        self.start_coordinate = None
        self.end_coordinate = None
        self.use_node_cost = False
        self.visited_coordinates = []
        self.path = []



    def read_maze(self, path):
        # Read maze map
        self.matrix, self.bonuses, self.waypoints = util.read_file(path)
    
        # Extract START and END
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != 'x':
                    # Mark START
                    if self.matrix[i][j] == 'S':
                        self.start_coordinate = (i, j)

                    # Mark END
                    elif i == 0 or i == (len(self.matrix) - 1) or j == 0 or j == (len(self.matrix[0]) - 1):
                        self.end_coordinate = (i, j)  


    def get_new_nodes(self, current_node, x, y, next_move_cost):
        node1 = None
        node2 = None
        if self.matrix[x][y] != 'x':
            # Check for waypoint in
            for waypoint in self.waypoints:
                if waypoint[0] == x and waypoint[1] == y: 
                    # Change coordinate to waypoint out
                    node1 = Node((x, y), current_node, next_move_cost)
                    self.visited_coordinates.append(node1.coordinate)
                    node2 = Node((waypoint[2], waypoint[3]), node1, 0) # Teleportation cost = 0
                    break

                if waypoint[2] == x and waypoint[3] == y: 
                    # Change coordinate to waypoint out
                    node1 = Node((x, y), current_node, next_move_cost)
                    self.visited_coordinates.append(node1.coordinate)
                    node2 = Node((waypoint[0], waypoint[1]), node1, 0) # Teleportation cost = 0
                    break

            # Extract bonus point if it is not DFS or BFS
            if next_move_cost != -100 and next_move_cost != 0:
                for bonus in self.bonuses:
                    if bonus[0] == x and bonus[1] == y:
                        next_move_cost = bonus[2]
                        break
        
            node1 = Node((x, y), current_node, next_move_cost)
        
        return node1, node2



    def expand(self, current_node, next_move_cost):
        children = []

        # Up
        x = current_node.coordinate[0] - 1
        y = current_node.coordinate[1]
        child1, child2 = self.get_new_nodes(current_node, x, y, next_move_cost)
        if child1 != None:
            children.append(child1)
        if child2 != None:
            children.append(child2)
            
        # Right
        x = current_node.coordinate[0]
        y = current_node.coordinate[1] + 1
        child1, child2 = self.get_new_nodes(current_node, x, y, next_move_cost)
        if child1 != None:
            children.append(child1)
        if child2 != None:
            children.append(child2)

        # Down
        x = current_node.coordinate[0] + 1
        y = current_node.coordinate[1]
        child1, child2 = self.get_new_nodes(current_node, x, y, next_move_cost)
        if child1 != None:
            children.append(child1)
        if child2 != None:
            children.append(child2)

        # Left
        x = current_node.coordinate[0]
        y = current_node.coordinate[1] - 1
        child1, child2 = self.get_new_nodes(current_node, x, y, next_move_cost)
        if child1 != None:
            children.append(child1)
        if child2 != None:
            children.append(child2)

        return children



    def solve(self, algorithm = None, heuristic = None, heuristic_function = None):
        # Initialize solver
        next_move_cost = 0
        function = None
        if algorithm == Algorithm.DEPTH_FIRST_SEARCH:
            next_move_cost = -100 # Act as a stack
            function = self.ucs
        elif algorithm == Algorithm.BREADTH_FIRST_SEARCH:
            next_move_cost = 0 # Act as a queue
            function = self.ucs
        elif algorithm == Algorithm.UNIFORM_COST_SEARCH:
            next_move_cost = 1
            function = self.ucs
        elif heuristic == Heuristic.GREEDY_BEST_FIRST_SEARCH:
            # Return no path if END is not found
            if self.end_coordinate == None:
                return self.path

            next_move_cost = 1
            self.use_node_cost = False
            function = heuristic_function
        elif heuristic == Heuristic.A_STAR_SEARCH:
            # Return no path if END is not found
            if self.end_coordinate == None:
                return self.path

            next_move_cost = 1
            self.use_node_cost = True
            function = heuristic_function
        elif heuristic == Heuristic.BONUS_ORIENTED_SEARCH:
            # Return no path if END is not found
            if self.end_coordinate == None:
                return self.path

            next_move_cost = 1
            self.use_node_cost = True
            function = heuristic_function
            
        frontier = util.Queue()
        current_node = Node(self.start_coordinate)
        frontier.push(current_node)
        children = []
        
        # Solve
        while not frontier.empty():
            # Extract node at front of frontier
            current_node = frontier.peek()
            frontier.pop()

            # Proceed to next step if current node is not visited
            if current_node.coordinate not in self.visited_coordinates:
                self.visited_coordinates.append(current_node.coordinate) # Mark node visited

                # This is the SOLUTION
                if current_node.coordinate == self.end_coordinate:
                    # Backtrack path
                    path = []
                    cost = 0
                    node_in_path = current_node
                    while node_in_path:
                        path.append(node_in_path.coordinate)
                        cost += node_in_path.cost_so_far
                        node_in_path = node_in_path.parent

                    # Reverse list
                    path = list(reversed(path))
                    self.path = path
                    return self.path

                # Expand all possible moves (children)
                children = self.expand(current_node, next_move_cost)

                # Add children to frontier
                for child in children:
                    frontier.push(child)
                
                # Act as an priority queue
                frontier.sort(function) 
                

    def visualize(self, sub_directory = '', file_name = ''):
        print(f'The height of the matrix: {len(self.matrix)}')
        print(f'The width of the matrix: {len(self.matrix[0])}')
        util.visualize_maze(self.matrix, self.bonuses, self.waypoints, self.start_coordinate, self.end_coordinate, self.path, self.visited_coordinates, sub_directory, file_name)


    """Cost functions"""
    # Applied for dfs, bfs, ucs
    def ucs(self, node):
        g = node.cost_so_far

        return g

    # Best heuristic
    def manhattan_heuristic(self, node):
        g = 0
        if self.use_node_cost == True:
            g = node.cost_so_far

        h = abs(node.coordinate[0] - self.end_coordinate[0]) + abs(node.coordinate[1] - self.end_coordinate[1])

        return g + h
    
    # Good heuristic
    def euclidean_heuristic(self, node):
        g = 0
        if self.use_node_cost == True:
            g = node.cost_so_far

        h = round(sqrt(pow(node.coordinate[0] - self.end_coordinate[0], 2) + pow(node.coordinate[1] - self.end_coordinate[1], 2)))

        return g + h

    # Bad heuristic
    def bad_heuristic(self, node):
        top_left = sqrt(pow(0 - node.coordinate[0], 2) + pow(0 - node.coordinate[1], 2))  
        top_right = sqrt(pow(0 - node.coordinate[0], 2) + pow(len(self.matrix[0]) - node.coordinate[1] - 1, 2))
        bottom_left = sqrt(pow(len(self.matrix) - node.coordinate[0] - 1, 2) + pow(0 - node.coordinate[1], 2))
        bottom_right = sqrt(pow(len(self.matrix) - node.coordinate[0] - 1, 2) + pow(len(self.matrix[0]) - node.coordinate[1] - 1, 2))
        h = round(max(top_left, top_right, bottom_left, bottom_right))

        return h

    # Point-oriented heuristic
    def bonus_oriented_heuristic(self, node):
        """Heuristic does not ensure the path is shortest but tries to pick up as many as
           posible bonuses with the relatively short path. The idea of heuristic is to find
           the 3x3 cluster containing most weighted bonuses and expand to its direction. In
           the process of searching for relevant cluster, it also estimates the distance to
           exit and current cost to choose as short as possible path."""
        # g function
        g = node.cost_so_far

        # Weight to calculate h function
        min_points = 1000000
        triangle_vertex = (0, 0)
        visited_bonuses = []

        for bonus in self.bonuses:
             # Only check not visited bonuses
            if bonus not in visited_bonuses:
                visited_bonuses.append(bonus)

                # Total points of 3x3 cluster
                total_points = bonus[2]

                # Define 3x3 cluster
                top = max(bonus[0] - 1, 1)
                bottom = min(bonus[0] + 1, len(self.matrix) - 2)
                left = max(bonus[1] - 1, 1)
                right = min(bonus[1] + 1, len(self.matrix[0]) - 2)

                # Search for 3x3 cluster around this bonus
                for other_bonus in self.bonuses:
                    if other_bonus != bonus:
                        if (other_bonus[0] == top and other_bonus[1] == left) or \
                        (other_bonus[0] == top and other_bonus[1] == bonus[1]) or \
                        (other_bonus[0] == top and other_bonus[1] == right) or \
                        (other_bonus[0] == bonus[0] and other_bonus[1] == left) or \
                        (other_bonus[0] == bonus[0] and other_bonus[1] == right) or \
                        (other_bonus[0] == bottom and other_bonus[1] == left) or \
                        (other_bonus[0] == bottom and other_bonus[1] == bonus[1]) or \
                        (other_bonus[0] == bottom and other_bonus[1] == right):
                            total_points += other_bonus[2]
                            visited_bonuses.append(other_bonus) # No need to check bonuses in 3x3 cluster
                
                # Pick bonus in the most weighted cluster
                if total_points < min_points:
                    min_points = total_points
                    triangle_vertex = (bonus[0], bonus[1])

        # Evaluate h function in consideration of distance to the most weighted cluster and exit
        h = round(sqrt(pow(node.coordinate[0] - triangle_vertex[0], 2) + pow(node.coordinate[1] - triangle_vertex[1], 2)) + \
            sqrt(pow(node.coordinate[0] - self.end_coordinate[0], 2) + pow(node.coordinate[1] - self.end_coordinate[1], 2)))

        return g + h
    """==================="""