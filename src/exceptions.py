class CustomException(Exception):

    def __init__(self, message):
        self.message = message


class InvalidCountMatrixColumnsException(CustomException):

    def __init__(self, count, necessary_count):
        message = 'Invalid count of the matrix columns = {}. Necessary: {}'.format(count, necessary_count)

        super().__init__(message)


class InvalidCountMatrixRowsException(CustomException):

    def __init__(self, count, necessary_count):
        message = 'Invalid count of the matrix rows = {}. Necessary: {}'.format(count, necessary_count)

        super().__init__(message)


class InvalidSizeMatrixException(CustomException):

    def __init__(self, count_rows, count_columns):
        message = 'Invalid size of the matrix {}x{}. The count of rows and columns mush be positive'

        message.format(count_rows, count_columns)

        super().__init__(message)


class InvalidMatrixElementException(CustomException):

    def __init__(self, element):
        message = 'Invalid matrix element = {}. Necessary: 0 or 1'.format(element)

        super().__init__(message)
