from company.Employee import Employee


class Designer(Employee):
    def __init__(self, name, salary, d_tool):
        super().__init__(name, salary)
        self.d_tool = d_tool

    def get_details(self):
        return super().get_details() + f", dizaino įrankis: {self.d_tool}"
