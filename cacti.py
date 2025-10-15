def cacti_number(plot):
    if not isinstance(plot, list):
        raise TypeError
    rows = len(plot)
    if rows == 0:
        return 0
    cols = len(plot[0])
    for r in plot:
        if not isinstance(r, list) or len(r) != cols:
            raise ValueError
        for v in r:
            if v not in (0, 1):
                raise ValueError

    grid = [row[:] for row in plot]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                up = grid[i - 1][j] if i > 0 else 0
                down = grid[i + 1][j] if i < rows - 1 else 0
                left = grid[i][j - 1] if j > 0 else 0
                right = grid[i][j + 1] if j < cols - 1 else 0
                if up == down == left == right == 0:
                    grid[i][j] = 1
                    count += 1
    return count
