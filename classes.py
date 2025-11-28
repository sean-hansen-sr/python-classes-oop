from datetime import date
from dataclasses import dataclass

@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}...")

class Employee:
    __slots__ = ("name", "age", "_salary", "_annual_salary", "project")
    minimum_wage = 1000

    @classmethod
    def set_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Minimum wage cannot exceed $3000")
        cls.minimum_wage = new_wage
    
    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)
    
    def __init__(self, name, age, salary, project):
        self.name = name             #self.__dict__["name"] = "Ji-Soo"
        self.age = age               #self.__dict__["age"] = 38
        self.salary = salary         #self.__dict__["salary"] = 1200
        self.project = project
        self._annual_salary = None
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def info(self):
        print(f"{self.name} is {self.age} years old. Employee has a salary of ${self.salary:.2f}")
    
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee has a salary of ${self.salary:.2f}"
    
    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.salary)}, {repr(self.project)})"
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f"Minimum wage is ${Employee.minimum_wage}")
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary
    
class SlotsInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, '__slots__')

class Tester(Employee):
    def run_tests(self):
        print(f"{self.name} is running tests.")

class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ("framework")

    def __init__(self, name, age, salary, framework, project):
        super().__init__(name, age, salary, project)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus   

#e = Employee()
p = Project("Website Redesign", 5000, "Acme Corp")
e = Developer("Ji-Soo", 38, 1200, "Flask", p)
print(e.has_slots())  # Output: True
e.increase_salary(10)  # Increase salary by 10%
e.info()  # Output: Ji-Soo is 38 years old. Employee has a salary of $1320.00
print(e.__slots__)  # Output: framework
print(e)  # Output: Ji-Soo is 38 years old. Employee has a salary of $1320.00
print(repr(e))  # Output: Employee(Ji-Soo, 38, 1320.0, Project(name='Website Redesign', payment=5000, client='Acme Corp'))
print(eval(repr(e))) # Output: Ji-Soo is 38 years old. Employee has a salary of $1320.00
#print(e.__dict__)  # Output: {}
print(e.__class__)  # Output: <class '__main__.Developer'>