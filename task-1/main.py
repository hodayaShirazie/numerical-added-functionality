'''submitted by: hodaya shirazie, zohar monsonego, shulamit mor ysesf'''



#function that prints matrix
def print_matrix(matrix):
   for i in range(len(matrix[0])):
      for j in range(len(matrix[0])):
         print(matrix[i][j], end=" ")
      print()

# function that returns The sum matrix of 2 matrices
def sum_matrix(matrix_1, matrix_2):
    matrix = []
    rows = []
    for i in range(len(matrix_1[0])):
       for j in range(len(matrix_1[0])):
          rows.append(matrix_1[i][j] + matrix_2[i][j])
       matrix.append(rows)
       rows = []
    return matrix

# function that returns The product matrix of 2 matrices
def mult_matrix(matrix_1,matrix_2):
   matrix = []
   rows = []
   sum = 0
   for i in range(len(matrix_1[0])):
      for j in range(len(matrix_1[0])):
         for k in range(len(matrix_1[0])):
            sum += matrix_1[i][k] * matrix_2[k][j]
         rows.append(sum)
         sum = 0
      matrix.append(rows)
      rows = []
   return matrix





if __name__ == '__main__':

   rows_1 = []
   rows_2 = []
   matrix_1 = []
   matrix_2 = []


   #building matrices by user input

   size_1 = int(input("enter size of matrix 1: "))
   print("enter matrix-1 elements: ")

   for i in range(size_1):
      for j in range(size_1):
         rows_1.append(int(input()))
      matrix_1.append(rows_1)
      rows_1 = []


   size_2 = int(input("enter size of matrix 2: "))
   print("enter matrix-2 elements: ")

   for i in range(size_2):
      for j in range(size_2):
         rows_2.append(int(input()))
      matrix_2.append(rows_2)
      rows_2 = []

   print("matrix_1:")
   print_matrix(matrix_1)
   print()

   print("matrix_2:")
   print_matrix(matrix_2)
   print()


   #if matrices can be multiplied and added---
   if size_1 == size_2:

      print("matrix_1 + matrix_2:")
      print_matrix(sum_matrix(matrix_1, matrix_2))
      print()

      print("matrix_1 * matrix_2:")
      print_matrix(mult_matrix(matrix_1, matrix_2))

   #if not - inform the user
   else:
      print("lengths are not valid to allow adding and multiplication")
