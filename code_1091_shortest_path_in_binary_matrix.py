from heapq import heappush, heappop
class PriorityQueue: 
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        def a_star_graph_search(start,goal_function,successor_function,heuristic):
            visited = set()
            came_from = dict()
            distance = {start: 0}
            frontier = PriorityQueue()
            frontier.add(start)
            while frontier:
                node = frontier.pop()
                if node in visited:
                    continue
                if goal_function(node):
                    return reconstruct_path(came_from, start, node)
                visited.add(node)
                for successor in successor_function(node):
                    frontier.add(
                        successor,
                        priority = distance[node] + 1 + heuristic(successor)
                    )
                    if (successor not in distance
                        or distance[node] + 1 < distance[successor]):
                        distance[successor] = distance[node] + 1
                        came_from[successor] = node
            return None
        
        def reconstruct_path(came_from, start, end):
            reverse_path = [end]
            while end != start:
                end = came_from[end]
                reverse_path.append(end)
            return list(reversed(reverse_path))
        
        def get_goal_function(grid):
            n = len(grid)
            m = len(grid[0])
            def is_bottom_right_cell(cell):
                return cell == (n-1,m-1)
            return is_bottom_right_cell

        def get_successor_function(grid):
            def get_clear_and_adjacent_cells(cell):
                row, col = cell
                return (
                    (row+a, col+b)
                    for a in (-1,0,1)
                    for b in (-1,0,1)
                    if a!=0 or b!=0
                    if 0 <= row+a < len(grid)
                    if 0 <= col+b < len(grid[0])
                    if grid[row+a][col+b] == 0
                )
            return get_clear_and_adjacent_cells

        def get_heuristic(grid):
            n = len(grid)
            m = len(grid[0])
            (a,b) = goal_cell = (n-1, m-1)
            def get_clear_path_distance_from_goal(cell):
                (row, col) = cell
                return max(abs(a-row), abs(b-col))
            return get_clear_path_distance_from_goal
    
        # implementing A*
        shortest_path = a_star_graph_search(
            start=(0,0),
            goal_function=get_goal_function(grid),
            successor_function = get_successor_function(grid),
            heuristic = get_heuristic(grid)
        )
        if not shortest_path or grid[0][0] == 1:
            return -1
        return len(shortest_path)       