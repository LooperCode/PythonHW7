def print_operation_table(operation, num_row=6, num_column=6):
    for i in range(1, num_row + 1):
        for j in range(1, num_column + 1):
            if j == num_column:
                print(operation(i, j))
            else:
                print(operation(i, j), '\t', end='')
                
                
print_operation_table(lambda x, y: x * y)