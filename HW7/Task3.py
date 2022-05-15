class Cell:
    def __init__(self, count_cells=1):
        self.__count_cells = count_cells

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.__count_cells + other.__count_cells)
        return None

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.__count_cells - other.__count_cells > 0:
                return self.__count_cells - other.__count_cells
            else:
                print('The result is less than zero!')
                # raise ArithmeticError
        return None

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.__count_cells * other.__count_cells)
        return None

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.__count_cells // other.__count_cells)
        return None

    def make_order(self, cells_in_a_row):
        line = '\n'.join(['*' * cells_in_a_row for _ in range(self.__count_cells // cells_in_a_row)] +
                         ['*' * (self.__count_cells % cells_in_a_row)])
        return line if line[-1] != '\n' else line[:-1]


cell1 = Cell()  # cells: 1
cell2 = Cell() + cell1  # cells: 2
cell3 = cell1 + cell2  # cells: 3
cell4 = cell3 * cell2 * cell2  # cells: 12
cell5 = cell4 / cell3  # cells: 4

print(cell1.make_order(3), end='\n---\n')
print(cell2.make_order(3), end='\n---\n')
print(cell3.make_order(3), end='\n---\n')
print(cell4.make_order(5), end='\n---\n')
print(cell5.make_order(5), end='\n---\n')
print(cell3 - cell4)
