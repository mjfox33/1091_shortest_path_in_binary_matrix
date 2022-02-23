from code_1091_shortest_path_in_binary_matrix import Solution

def test_example_1():
    s = Solution()
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    output = 4
    assert s.shortestPathBinaryMatrix(grid) == output