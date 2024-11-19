def is_reduced_echelon(matrix):
    leading_one_cols = set()

    for i in range(0,len(matrix)):
        leading_one_found = False

        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 1:
                if leading_one_found:
                    return False

                if j in leading_one_cols:
                    return False

                leading_one_found = True
                leading_one_cols.add(j)

    return True

def count_and_generate_matrices(rows :int, columns :int):
    matrices = []
    count = 0

    for i in range(0,2**(rows * columns)):

        matrix = []
        leading_one_cols = set()
        is_reduced_echelon = True

        for j in range(rows):
            row = []
            leading_one_found = False

            for k in range(columns):
                bit_value = (i // (2 ** (j * columns + k))) % 2
                row.append(bit_value)

                if bit_value == 1:

                    if leading_one_found:
                        is_reduced_echelon = False
                        break

                    if k in leading_one_cols:
                        is_reduced_echelon = False
                        break

                    leading_one_found = True
                    leading_one_cols.add(k)



            matrix.append(row)

        if is_reduced_echelon:
            count += 1
            matrices.append(matrix)

    print(f"1. The number of matrices in reduced echelon form is {count}")
    print("2. The matrices in reduced echelon form are (the leading 1’s are framed):")

    for matrix in matrices:
        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()



while True:

    print("1. Input a number of rpws and columns")
    print("2. Make a test with a set of values who laready exist")
    print("3. EXIT")

    command = int(input("Input a commnad -->"))

    if command == 1:

        rows = int(input("Input a rows value (2 <= rows <= 5) --> "))
        columns = int(input("Input a columns value (2 <= columns <= 5) --> "))


        if 2 <= columns <= 5 and 2 <= rows <= 5:
            count_and_generate_matrices(rows, columns)

        else:

            print(f"The values for rows = {rows} and columns = {columns} aren't correct. Please retry!")
            print("\n")

    elif command == 2:

        rows = 2
        columns = 3

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 3
        columns = 2

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 3
        columns = 3

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 4
        columns = 4

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 5
        columns = 5

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 4
        columns = 5

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 5
        columns = 3

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

        rows = 5
        columns = 4

        print(f"Nuber of rows is {rows}, number of columns is {columns}")
        count_and_generate_matrices(rows, columns)

    else:
        print("You exit!")
        break



