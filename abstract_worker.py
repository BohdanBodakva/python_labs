from abc import abstractmethod, ABC


class Employee(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_age(self) -> str:
        return self.__age

    def set_name(self, age: int) -> None:
        self.__age = age

    @abstractmethod
    def do_work(self) -> None:
        pass

    def __str__(self) -> str:
        return f"name: {self.__name}, age: {self.__age} y.o."
