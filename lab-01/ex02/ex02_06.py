result = input("Nhập X, Y: ")
dia = [int(x) for x in result.split(',')]
X = dia[0]
Y = dia[1]

matrix = [[0 for col in range(Y)] for row in range(X)]

print("Mảng 2 chiều: ")
for row in range(X):
    for col in range(Y): 
        matrix[row][col] = row * col

print(matrix)
