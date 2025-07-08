import json
from typing import List, Dict

GRID_SIZE = 30
TOP_ROWS = 15


def make_grid(color_top: int, color_bottom: int) -> List[List[int]]:
    """Return a 30x30 grid with top half color_top and bottom half color_bottom."""
    top = [[color_top] * GRID_SIZE for _ in range(TOP_ROWS)]
    bottom = [[color_bottom] * GRID_SIZE for _ in range(GRID_SIZE - TOP_ROWS)]
    return top + bottom


def make_solution(color: int) -> List[List[int]]:
    """Return a 30x30 grid filled entirely with the given color."""
    return [[color] * GRID_SIZE for _ in range(GRID_SIZE)]


def make_examples() -> List[Dict[str, List[List[int]]]]:
    examples = []
    colors = range(10)
    for top_color in colors:
        for bottom_color in colors:
            if top_color == bottom_color:
                continue
            example = {
                "input": make_grid(top_color, bottom_color),
                "output": make_solution(top_color),
            }
            examples.append(example)
    return examples


def main() -> None:
    """Generate and dump the puzzle dataset."""
    examples = make_examples()
    payload = {"count": len(examples), "examples": examples}
    with open("top_bottom_puzzles.json", "w") as f:
        json.dump(payload, f)


if __name__ == "__main__":
    main()
