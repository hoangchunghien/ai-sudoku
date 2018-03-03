from utils import *

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers
    """
    twins = []  # e.g [('13', [units to eliminate...]), ...]
    for u in unitlist:
        twinsable = dict((k, values[k]) for k in u if len(values[k]) == 2)
        value_counters = dict((values[k], 0) for k in twinsable.keys())
        for k in twinsable.keys():
            value_counters[values[k]] += 1

        for v in value_counters.keys():
            if value_counters[v] != 2:
                continue
            pair = [k for k in twinsable.keys() if twinsable[k] == v]
            if len(pair) > 0:
                twins.append((v, [k for k in u if k not in pair]))
    
    # eliminate naked twins
    for v, u in twins:
        for digit in v:
            for k in u:
                values[k] = values[k].replace(digit, '')
    return values


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for k in values.keys():
        digit = values[k]
        if len(digit) > 1:
            continue

        for peer in peers[k]:
            values[peer] = values[peer].replace(digit, '')
    return values

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Use the Eliminate Strategy
        values = eliminate(values)

        # Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    
    if all(len(values[k]) == 1 for k in boxes):
        return values
    
    # Choose one of the unfilled squares with the fewest possibilities
    k = min(k for k in boxes if len(values[k]) > 1)

    # Now use recurrence to solve each one of the resulting sudokus, and 
    for digit in values[k]:
        new_board = values.copy()
        new_board[k] = digit
        attempt = search(new_board)
        if attempt:
            return attempt
