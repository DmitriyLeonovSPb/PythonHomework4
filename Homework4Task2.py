# Напишите функцию для транспонирования матрицы

# Собственная функция
matrix_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]] 
def transs(matrix):
    bufer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            bufer[b][a] = matrix[a][b]
    return bufer
print("Транспонирование собственной функцией: ")
for i in matrix_in:
    print(i)
print()
transported = transs(matrix_in)
for i in transported:
    print(i) 

# С помощью библиотеки transpose
import numpy as nummy
inputt_array = nummy.array([[9, 5, 1],[6, 3, 7]])
transposed_array = inputt_array.transpose()
print("Транспонирование библиотекой transpose")
print(inputt_array)
print()
print(transposed_array)

# С помощью метода zip
zip_arra = [[9, 5, 1],[6, 3, 7]]
arra_ziped = zip(*zip_arra)
answer = [list(row) for row in arra_ziped]
print("Транспонирование методом zip")
print(zip_arra)
print()
print(answer)