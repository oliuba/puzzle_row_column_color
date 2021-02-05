"""
This module is created to check whether the board is ready for the game.
It mustn't contain same numbers in one row, in one column and on one color.

Github link: https://github.com/oliuba/puzzle_row_column_color
"""

def row_valid(board: list) -> bool:
    """
    Returns True if the board is ready in rows (each row has unrepeatable numbers).
    >>> board = ["**** **",\
    "***1 **",\
    "**  3**",\
    "* 4 1 9",\
    "     8 ",\
    " 61  35",\
    "3  8   ",\
    "      *",\
    "**2 5**",\
    "** 2***",\
    "** ****"]
    >>> row_valid(board)
    True
    """
    for row in board:
        playing_zone = row.replace('*', '')
        only_numbers = playing_zone.replace(' ', '')
        if len(only_numbers) != len(set(only_numbers)):
            return False
    return True


def column_valid(board: list) -> bool:
    """
    Returns True if the board is ready in columns (each column has unrepeatable numbers).
    >>> board = ["**** **",\
    "***1 **",\
    "**  3**",\
    "* 4 1 9",\
    "     8 ",\
    " 61  35",\
    "3  8 7 "]
    >>> column_valid(board)
    True
    """
    columns = ['' for _ in range(len(board))]
    for ind, _ in enumerate(board):
        for row in board:
            columns[ind] += row[ind]
    return row_valid(columns)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
