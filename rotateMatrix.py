class Matrix:
    def __init__(self):
        self.matrix = [[1,2,3],[4,5,6],[7,8,9]]

        '''
        1 2 3
        4 5 6
        7 8 9
        '''

    def rotate(self):
        '''
        7 4 1
        8 5 2
        9 6 3
        '''
        rows = len(self.matrix[0])
        columns = len(self.matrix)
        new_matrix = []
        row = []
        for j in range(rows):
            for i in range(columns):
                row.append(self.matrix[(columns - 1) - i][j])
            new_matrix.append(row)
            row = []
        print(new_matrix)

m = Matrix()
print(m.matrix)
m.rotate()
