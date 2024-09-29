class StudentNotFoundException(Exception):
    def __init__(self, student_id, message="Student not found with ID"):
        self.student_id = student_id
        self.message = f"{message}: {student_id}"
        super().__init__(self.message)


class InvalidFacultyOperation(Exception):
    def __init__(self, operation, message="Invalid operation on faculty"):
        self.operation = operation
        self.message = f"{message}: {operation}"
        super().__init__(self.message)

