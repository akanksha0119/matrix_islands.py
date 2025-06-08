
from typing import List

def count_islands_with_diagonals(matrix: List[List[int]]) -> int:
    """
    Count the number of islands in a 2D matrix where islands are
    connected in all 8 directions.

    Args:
        matrix (List[List[int]]): 2D matrix of 0s and 1s

    Returns:
        int: Number of islands
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # All 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(r: int, c: int):
        """Depth-First Search to mark all connected 1s as visited"""
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                not visited[nr][nc] and matrix[nr][nc] == 1):
                dfs(nr, nc)

    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                island_count += 1

    return island_count


def run_tests():
    """Run sample test cases"""
    print("=== Matrix Islands With Diagonals: Sample Test Cases ===\n")
    test_cases = [
        {
            "matrix": [
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 1]
            ],
            "expected": 3
        },
        {
            "matrix": [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]
            ],
            "expected": 2
        },
        {
            "matrix": [
                [0, 0],
                [0, 0]
            ],
            "expected": 0
        },
        {
            "matrix": [
                [1]
            ],
            "expected": 1
        },
        {
            "matrix": [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1]
            ],
            "expected": 1
        }
    ]

    for idx, case in enumerate(test_cases, 1):
        result = count_islands_with_diagonals(case["matrix"])
        print(f"Test Case {idx}:")
        for row in case["matrix"]:
            print(" ", row)
        print(f"Expected: {case['expected']}, Got: {result}")
        print("Result:", "✅ Passed\n" if result == case["expected"] else "❌ Failed\n")

if __name__ == "__main__":
    run_tests()
