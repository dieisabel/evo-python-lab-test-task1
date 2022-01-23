from typing import List
from typing import Dict


def direction_first_solution(facing: str, turn: int) -> str:
    """1st solution, based on amount of turns"""

    # List all available directions
    directions: List[str] = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    # Check for errors
    if turn not in range(-1080, 1080 + 1) and turn % 45 != 0:
        raise ValueError(f'Turn degree must be between -1080 and 1080 and can be divided by 45, not {turn}')
    if facing not in directions:
        raise ValueError(f'We cannot face {facing} direction!')

    # Calculate amount of turns we need to do
    need_to_turn: int = turn // 45

    # Calculate amount of turns we already did
    already_turned: int = directions.index(facing)

    # Calculate total amount of turns we need to do, also mod by amount of directions to get rid of circle repeats
    turns: int = (need_to_turn + already_turned) % len(directions)
    return directions[turns]


def direction_second_solution(facing: str, turn: int) -> str:
    """2nd solution, based on degrees"""

    # Map directions and its degrees in dictionary
    directions: Dict[str, int] = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315,
    }

    # Check for errors
    if turn not in range(-1080, 1080 + 1) and turn % 45 != 0:
        raise ValueError(f'Turn degree must be between -1080 and 1080 and can be divided by 45, not {turn}')
    if facing not in directions.keys():
        raise ValueError(f'We cannot face {facing} direction!')

    # Get starting degree
    start_degree: int = directions[facing]

    # Calculate ending degree
    end_degree: int = turn + start_degree

    # Get rid of circle repeats in end_degree
    if end_degree < 0:
        while end_degree < 0:
            end_degree += 360
    elif end_degree >= 360:
        while end_degree >= 360:
            end_degree -= 360

    # Find direction by end degree
    for direction, degree in directions.items():
        if degree == end_degree:
            return direction
