from company.Employee import Employee


class Developer(Employee):
    def __init__(self, name, salary, p_language):
        super().__init__(name, salary)
        self.p_language = p_language

    def get_details(self):
        return super().get_details() + f", programavimo kalba: {self.p_language}"



