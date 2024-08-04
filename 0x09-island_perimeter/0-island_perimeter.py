#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
        function that returns the perimeter of island

        Args:
            grid => The matrix that represenet land and water

        return:
            perimeter of island
    """
    visit = set()

    def dfs(r, c):
        if r >= len(grid) or c >= len(grid[0])\
                or r < 0 or c < 0 or grid[r][c] == 0:
            return 1

        if (r, c) in visit:
            return 0

        visit.add((r, c))
        perimeter = dfs(r, c + 1)
        perimeter += dfs(r + 1, c)
        perimeter += dfs(r, c - 1)
        perimeter += dfs(r - 1, c)

        return perimeter

    for r in range(len(grid)):
        if 1 in grid[r]:
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r, c)
