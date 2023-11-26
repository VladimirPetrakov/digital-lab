from src.exceptions import InvalidCountMatrixRowsException, InvalidCountMatrixColumnsException


class Matrix:

    def __init__(self, count_rows, count_columns):
        self._count_rows = count_rows
        self._count_columns = count_columns

        self._data = []

    def get_count_rows(self):
        return self._count_rows

    def get_count_columns(self):
        return self._count_columns

    def set_element(self, row_index, column_index, value):
        self._data[row_index][column_index] = value

    def get_element(self, row_index, column_index):
        return self._data[row_index][column_index]

    def fill(self, data):
        self._data = []

        count_rows = len(data)

        if count_rows != self._count_rows:
            raise InvalidCountMatrixRowsException(count_rows, self._count_rows)

        for row_index in range(0, count_rows):
            count_columns = len(data[row_index])

            if count_columns != self._count_columns:
                raise InvalidCountMatrixColumnsException(count_columns, self._count_columns)

            self._data.append([])

            for column_index in range(0, len(data[row_index])):
                self._data[row_index].append(data[row_index][column_index])

    def copy(self):
        matrix_copied = Matrix(self._count_rows, self._count_columns)

        matrix_copied.fill(self._data)

        return matrix_copied


class MatrixConverter:

    def __init__(self, matrix, matrix_template):
        self._matrix = matrix
        self._matrix_template = matrix_template

        self._matrix_converted = None

        self._rules = {
            0: '*',
            1: '2',
        }

    def run(self):
        self._matrix_converted = self._matrix.copy()

        if not self._is_valid_matrix_template():
            return self._matrix_converted

        for row_index in range(0, self._get_max_row()):
            for column_index in range(0, self._get_max_column()):
                if not self._is_contains_pattern(row_index, column_index):
                    continue

                self._convert_by_template(row_index, column_index)

                column_index += (self._matrix_template.get_count_columns() - 1)

        return self._matrix_converted

    def _is_valid_matrix_template(self):
        is_valid_count_rows = self._get_max_row() >= 1
        is_valid_count_columns = self._get_max_column() >= 1

        return is_valid_count_rows and is_valid_count_columns

    def _get_max_row(self):
        return self._matrix.get_count_rows() - self._matrix_template.get_count_rows() + 1

    def _get_max_column(self):
        return self._matrix.get_count_columns() - self._matrix_template.get_count_columns() + 1

    def _is_contains_pattern(self, row_start_index, column_start_index):
        for template_row_index in range(0, self._matrix_template.get_count_rows()):
            row_offset_index = row_start_index + template_row_index

            for template_column_index in range(0, self._matrix_template.get_count_columns()):
                column_offset_index = column_start_index + template_column_index

                value = self._matrix_converted.get_element(row_offset_index, column_offset_index)
                template_value = self._matrix_template.get_element(template_row_index, template_column_index)

                if value != template_value:
                    return False

        return True

    def _convert_by_template(self, row_start_index, column_start_index):
        for template_row_index in range(0, self._matrix_template.get_count_rows()):
            row_offset_index = row_start_index + template_row_index

            for template_column_index in range(0, self._matrix_template.get_count_columns()):
                column_offset_index = column_start_index + template_column_index

                old_value = self._matrix.get_element(row_offset_index, column_offset_index)
                new_value = self._convert_value(old_value)

                self._matrix_converted.set_element(row_offset_index, column_offset_index, new_value)

    def _convert_value(self, value):
        return self._rules[value]
