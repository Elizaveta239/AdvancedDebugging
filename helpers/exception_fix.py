def check_collision(board, shape, offset):
    """
    See if the matrix stored in the shape will intersect anything
    on the board based on the offset. Offset is an (x, y) coordinate.
    """
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            new_y = cy + off_y
            new_x = cx + off_x
            if new_y >= len(board) or new_x >= len(board[new_y]):
                return True
            if cell and board[new_y][new_x]:
                return True
    return False
