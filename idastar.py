class IDAStar:
    def __init__(self):
        pass

    def search(self, start, goal):
        """ 
        finds the shortest path from a start node to a 
        goal node, assuming heuristic is admissable 
        """
        self.came_from = { start: None }
        self.goal = goal
        threshold = start.get_heuristic()
        
        while 1:
            result = self._search(start, 0, threshold)

            if result is True:
                return []
            elif result == float("inf"): # Time limit exceeded
                return []

            threshold = result
            print(threshold)
        
    def _search(self, node, g, threshold):
        f = g + node.get_heuristic()

        if f > threshold:
            return f
        elif node == self.goal:
            return True #self._path(self.goal, self.came_from)

        min_f = float("inf")

        for neighbor in node.get_neighbors():
            result_f = self._search(neighbor, g + node.cost_to(neighbor), threshold)

            if result_f is True: 
                return True

            min_f = min(result_f, min_f)

        return min_f
        

    def _path(self, goal, came_from):
        path = []
        current = goal

        while came_from[current]:
            path.insert(0, current)
            current = came_from[current]    
        
        return path 
