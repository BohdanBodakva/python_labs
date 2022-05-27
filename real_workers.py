from abstract_worker import Employee


class Manager(Employee):
    def __init__(self, name: str, age: int, company: str) -> None:
        self.__company = company
        super().__init__(name, age)

    def do_work(self) -> None:
        print("Me name is {}, I'm working as manager in {}".format(self.get_name(), self.get_company()))

    def get_company(self) -> str:
        return self.__company

    def set_company(self, company: str) -> None:
        self.__company = company

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " + super().__str__() + f" , company: {self.get_company()}"


class Scientist(Employee):
    def __init__(self, name: str, age: int, university: str) -> None:
        self.__university = university
        super().__init__(name, age)

    def do_work(self) -> None:
        print("Me name is {}, I'm working as scientist in {}".format(self.get_name(), self.get_university()))

    def get_university(self) -> str:
        return self.__university

    def set_project(self, university: str) -> None:
        self.__university = university

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " + super().__str__() + f", university: {self.get_university()}"


class Worker(Employee):
    def __init__(self, name: str, age: int, factory: str) -> None:
        self.__factory = factory
        super().__init__(name, age)

    def do_work(self) -> None:
        print("Me name is {}, I'm working as worker in {}".format(self.get_name(), self.get_factory()))

    def get_factory(self) -> str:
        return self.__factory

    def set_factory(self, factory: str) -> None:
        self.__factory = factory

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " + super().__str__() + f" factory: {self.get_factory()}"


class Foreman(Employee):
    def __init__(self, name: str, age: int, warehouse: str) -> None:
        self.__warehouse = warehouse
        super().__init__(name, age)

    def do_work(self) -> None:
        print("Me name is {}, I'm working as foreman in {}".format(self.get_name(), self.get_warehouse()))

    def get_warehouse(self) -> str:
        return self.__warehouse

    def set_factory(self, warehouse: str) -> None:
        self.__warehouse = warehouse

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " + super().__str__() + f" warehouse: {self.get_warehouse()}"
