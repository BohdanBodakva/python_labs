from abstract_worker import Employee


class Manager(Employee):
    def do_work(self) -> None:
        print("Me name is {}, I'm working as manager in {}".format(self.get_name(), self.get_company()))

    def __init__(self, name: str, age: int, company: str) -> None:
        self.__company = company
        super().__init__(name, age)

    def get_company(self) -> str:
        return self.__company

    def set_company(self, company: str) -> None:
        self.__company = company

    def __str__(self) -> str:
        return "Manager: {}, {} y.o., company: {}".format(self.get_name(), self.get_age(), self.get_company())


class Scientist(Employee):
    def do_work(self) -> None:
        print("Me name is {}, I'm working as scientist in {}".format(self.get_name(), self.get_university()))

    def __init__(self, name: str, age: int, university: str) -> None:
        self.__university = university
        super().__init__(name, age)

    def get_university(self) -> str:
        return self.__university

    def set_project(self, university: str) -> None:
        self.__university = university

    def __str__(self) -> str:
        return "Scientist: {}, {} y.o., university: {}".format(self.get_name(), self.get_age(), self.get_university())


class Worker(Employee):
    def do_work(self) -> None:
        print("Me name is {}, I'm working as worker in {}".format(self.get_name(), self.get_factory()))

    def __init__(self, name: str, age: int, factory: str) -> None:
        self.__factory = factory
        super().__init__(name, age)

    def get_factory(self) -> str:
        return self.__factory

    def set_factory(self, factory: str) -> None:
        self.__factory = factory

    def __str__(self) -> str:
        return "Worker: {}, {} y.o., factory: {}".format(self.get_name(), self.get_age(), self.get_factory())


class Foreman(Employee):
    def do_work(self) -> None:
        print("Me name is {}, I'm working as foreman in {}".format(self.get_name(), self.get_warehouse()))

    def __init__(self, name: str, age: int, warehouse: str) -> None:
        self.__warehouse = warehouse
        super().__init__(name, age)

    def get_warehouse(self) -> str:
        return self.__warehouse

    def set_factory(self, warehouse: str) -> None:
        self.__warehouse = warehouse

    def __str__(self) -> str:
        return "Worker: {}, {} y.o., warehouse: {}".format(self.get_name(), self.get_age(), self.get_warehouse())
