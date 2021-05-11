from datetime import datetime

class Employee:
    company_domain = "example.com"

    def __init__(self, name, lname, jdate, salary, gender, trial_passed= False, phone_number=None, ldate=None):
        self.first_name = name
        self.last_name = lname
        self.join_date = datetime.strptime(jdate, "%Y-%m-%d")
        self.earned_money = salary
        if not isinstance(trial_passed, bool):
            raise TypeError("trial_passed should be an instance of bool")
        self.trial_passed = trial_passed
        self.gender = gender
        self.phone_number = phone_number
        self.leave_date = ldate
        if ldate is not None:
            self.leave_date = datetime.strptime(ldate, "%Y-%m-%d")
        self.__email = None
        self.__full_name = None

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        name, lname = value.split()
        self.first_name = name
        self.last_name = lname

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value not in {'M', 'F'}:
            raise ValueError("Gender can't be other than Male and Female")
        self.__gender = value



    @property
    def email(self):
        if self.__email is  None:
            return f"{self.first_name.lower()}.{self.last_name.lower()}@{self.company_domain}"
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __lt__(self, other):
        if self.earned_money is None or other.earned_money is None:
            raise ValueError("Employees must get salary")


employee1 = Employee("Ani", "Nazaryan", "2011-11-1", 130000, "F")
employee2 = Employee("Davit", "Tovmasyan", "2014-12-4", 1500000, "M", phone_number="098-325-200")


print(employee1.email)
print(employee1.earned_money)
print(employee1.trial_passed)
print(employee1.join_date)
print(employee1.full_name)
print(employee1.gender)

print(employee2.email)
print(employee2.gender)
print(employee2.phone_number)
