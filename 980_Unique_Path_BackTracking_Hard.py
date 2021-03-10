class Backtracking:
    total_path = []

    def unique_path(self, grid):
        if not grid:
            return grid
        self.ilen = len(grid) - 1
        self.jlen = len(grid[0]) - 1
        self._unique_path(grid, 0, 0, [])

        return self.total_path

    def _unique_path(self, grid, i, j, path):

        if grid[i][j] == 2:
            self.total_path.append(path)
            return

        if grid[i][j] == 1:
            path.append((i, j))

        if i+1 is not -1 and i+1 <= self.ilen:
            path.append((i + 1, j))
            self._unique_path(grid, i + 1, j, path)
        if j+1 is not -1 and j+1 <= self.jlen:
            path.append((i, j + 1))
            self._unique_path(grid, i, j + 1, path)


if __name__ == "__main__":
    obj = Backtracking()
    print(obj.unique_path([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
