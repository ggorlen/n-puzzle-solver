import queue as Q


class AStar:
    def __init__(self):
        pass
    
    def search(self, start, goal):
        """ 
        finds the shortest path from a start node to a 
        goal node, assuming heuristic is admissable 
        """

        came_from = { start: None }
        cost_so_far = { start: 0 }
        frontier = Q.PriorityQueue()
        frontier.put(start)

        while frontier.qsize():
            current = frontier.get()

            if current == goal:
                return self._path(goal, came_from)
            
            for neighbor in current.get_neighbors():
                new_cost = cost_so_far[current] + 1
                
                if not neighbor in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    frontier.put(neighbor)
                    came_from[neighbor] = current

    def _path(self, goal, came_from):
        path = []
        current = goal

        while came_from[current]:
            path.insert(0, current)
            current = came_from[current]    
        
        return path
