# abstractmethod can also be applied to static methods,
# class methods and properties. It appears immediately
# before the function definition
from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    @property
    @abstractmethod  # abstractmethod applied to class property
    def name(self):
        pass

    @name.setter
    @abstractmethod  # abstractmethod applied to class property
    def name(self, value):
        pass

    @classmethod
    @abstractmethod  # abstractmethod applied to classmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod  # abstractmethod applied to staticmethod
    def method2(self):
        pass

