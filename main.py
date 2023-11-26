from src.exceptions import CustomException, InvalidCountMatrixColumnsException, InvalidSizeMatrixException, \
    InvalidMatrixElementException
from src.entities import Matrix, MatrixConverter


def main():
    matrix_a, matrix_b = build_matrices()

    matrix_converted = convert_matrix(matrix_b, matrix_a)

    print_matrix(matrix_converted)


def build_matrices():
    matrix_a = None
    matrix_b = None

    while True:
        if matrix_a is not None and matrix_b is not None:
            break

        input_line = input()
        n, k = map(int, input_line.split())

        check_valid_size_matrix(n, k)

        matrix_data = []

        for i in range(0, n):
            input_line = input()

            row = tuple(map(int, input_line.split()))

            check_valid_matrix_row(row, k)

            matrix_data.append(row)

        if matrix_a is None:
            matrix_a = Matrix(n, k)
            matrix_a.fill(matrix_data)

            continue

        if matrix_b is None:
            matrix_b = Matrix(n, k)
            matrix_b.fill(matrix_data)

    return matrix_a, matrix_b


def check_valid_size_matrix(count_rows, count_columns):
    if count_rows < 1 or count_columns < 1:
        raise InvalidSizeMatrixException(count_rows, count_columns)


def check_valid_matrix_row(row, necessary_count_columns):
    count_columns = len(row)

    if count_columns != necessary_count_columns:
        raise InvalidCountMatrixColumnsException(count_columns, necessary_count_columns)

    for element in row:
        if element != 0 and element != 1:
            raise InvalidMatrixElementException(element)


def convert_matrix(matrix, matrix_template):
    matrix_converter = MatrixConverter(matrix, matrix_template)

    return matrix_converter.run()


def print_matrix(matrix):
    count_rows = matrix.get_count_rows()
    count_columns = matrix.get_count_columns()

    for row_index in range(0, count_rows):
        for column_index in range(0, count_columns):
            element = matrix.get_element(row_index, column_index)

            print(element, end="")

            if column_index != count_columns - 1:
                print(" ", end="")

        if row_index != count_rows - 1:
            print("\n", end="")


if __name__ == '__main__':
    try:   
        main()
    except CustomException as e:
        print(e.message)
