import json
from typing import Dict, List

GRID_SIZE = 30
SPLIT = GRID_SIZE // 2


def make_horizontal_grid(top_color: int, bottom_color: int) -> List[List[int]]:
    """Return a grid split horizontally with different colors."""
    top = [[top_color] * GRID_SIZE for _ in range(SPLIT)]
    bottom = [[bottom_color] * GRID_SIZE for _ in range(GRID_SIZE - SPLIT)]
    return top + bottom


def make_vertical_grid(left_color: int, right_color: int) -> List[List[int]]:
    """Return a grid split vertically with different colors."""
    row = [left_color] * SPLIT + [right_color] * (GRID_SIZE - SPLIT)
    return [row[:] for _ in range(GRID_SIZE)]


def make_diagonal_grid(
    color_a: int, color_b: int, main: bool = True
) -> List[List[int]]:
    """Return a grid split diagonally with different colors."""
    grid = []
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            if main:
                cond = i <= j
            else:
                cond = i + j <= GRID_SIZE - 1
            row.append(color_a if cond else color_b)
        grid.append(row)
    return grid


def make_solution(color: int) -> List[List[int]]:
    """Return a uniform solution grid filled with the given color."""
    return [[color] * GRID_SIZE for _ in range(GRID_SIZE)]


def make_datasets() -> Dict[str, List[Dict[str, List[List[int]]]]]:
    """Return examples grouped by puzzle type."""
    datasets: Dict[str, List[Dict[str, List[List[int]]]]] = {
        "top_bottom": [],
        "bottom_top": [],
        "left_right": [],
        "right_left": [],
        "diagonal_main_a": [],
        "diagonal_main_b": [],
        "diagonal_anti_a": [],
        "diagonal_anti_b": [],
    }

    colors = range(10)
    for c1 in colors:
        for c2 in colors:
            if c1 == c2:
                continue

            # horizontal split
            grid = make_horizontal_grid(c1, c2)
            datasets["top_bottom"].append({"input": grid, "output": make_solution(c1)})
            datasets["bottom_top"].append({"input": grid, "output": make_solution(c2)})

            # vertical split
            grid = make_vertical_grid(c1, c2)
            datasets["left_right"].append({"input": grid, "output": make_solution(c1)})
            datasets["right_left"].append({"input": grid, "output": make_solution(c2)})

            # diagonal main split
            grid = make_diagonal_grid(c1, c2, main=True)
            datasets["diagonal_main_a"].append({"input": grid, "output": make_solution(c1)})
            datasets["diagonal_main_b"].append({"input": grid, "output": make_solution(c2)})

            # diagonal anti split
            grid = make_diagonal_grid(c1, c2, main=False)
            datasets["diagonal_anti_a"].append({"input": grid, "output": make_solution(c1)})
            datasets["diagonal_anti_b"].append({"input": grid, "output": make_solution(c2)})

    return datasets


def main() -> None:
    """Generate and dump puzzle datasets per puzzle type."""
    datasets = make_datasets()
    for name, examples in datasets.items():
        with open(f"{name}_puzzles.json", "w") as f:
            json.dump(examples, f)


if __name__ == "__main__":
    main()
