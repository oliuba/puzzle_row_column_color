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


def color_valid(board: list) -> bool:
    """
    Returns True if the board is ready in colors (each color has unrepeatable numbers).
    The board is painted in edges 5X5, starting from the left bottom edge
    and making the whole board together.
    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]
    >>> color_valid(board)
    True
    """
    colors_number = len(board) - 4
    colors = ['' for _ in range(colors_number)]
    for ind, row in enumerate(board):
        if ind + 1 < colors_number:
            row_colors = ind + 1
            for i in range(row_colors):
                colors[i] += row[-(colors_number + i)]
        else:
            if ind + 1 == colors_number:
                row_colors = ind + 1
            else:
                row_colors -= 1
            for i in range(row_colors):
                if i + 1 == row_colors:
                    colors[-(i + 1)] += row[i: (i + colors_number)]
                else:
                    colors[-(i + 1)] += row[i]
    return row_valid(colors)


def validate_board(board: list) -> bool:
    """
    Returns True if the board is valid for the game.
    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 2****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]
    >>> validate_board(board)
    True
    """
    return row_valid(board) and column_valid(board) and color_valid(board)
