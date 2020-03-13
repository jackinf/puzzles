class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        seen = set()
        q = [(Y, 0)]

        if X > Y:
            return X - Y

        while q:
            y, lvl = q.pop(0)
            if y == X:
                return lvl
            if y in seen:
                continue
            if y % 2 == 0:
                if max(X, y) // min(X, y) < 2:
                    if y > X:
                        return X - y // 2 + 1 + lvl
                    if y < X:
                        return X - y + lvl

                q.append((y // 2, lvl + 1))
                seen.add(y)
            q.append((y + 1, lvl + 1))
            seen.add(y)

        return -1