def checkmate(board):
    rows = board.splitlines() if isinstance(board, str) else []
    n = len(rows)
    if n == 0 or any(len(r) != n for r in rows):
        print("Error")
        return

    kings = [(r, c) for r in range(n) for c in range(n) if rows[r][c] == "K"]
    if len(kings) != 1:
        print("Error")
        return
    kr, kc = kings[0]

    pieces = "PBRQK"

    def attacked_along(dr, dc, attackers):
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            if rows[r][c] in pieces:
                return rows[r][c] in attackers
            r, c = r + dr, c + dc
        return False

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if attacked_along(dr, dc, "RQ"):
            print("Success")
            return

    for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if attacked_along(dr, dc, "BQ"):
            print("Success")
            return
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if 0 <= r < n and 0 <= c < n and rows[r][c] == "P":
            print("Success")
            return

    print("Fail")
