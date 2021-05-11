class Employee:
    def __init__(self, name, lname, jdate, salary, trial, gender, phone_number=0, ldate=0):
        self.first_name = name
        self.last_name = lname
        self.join_date = jdate
        self.earned_money = salary
        self.passed_trial = trial
        self.__gender = gender
        self.phone_number = phone_number
        self.leave_date = ldate
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
        if self.__gender == "M" or self.__gender == "F":
            self.__gender = value

        else:
            raise ValueError("Gender can't be other than Male nad Female")


    trial = True

    def __bool__(self, trial):
        if trial:
            return self.passed_trial
        else:
            return self.passed_trial is None

    company_domain = "example.com"

    @property
    def email(self):
        if self.__email is None:
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


employee1 = Employee("Ani", "Nazaryan", " 01.11.2011", 130000, True, "F")


print(employee1.email)
print(employee1.earned_money)
print(employee1.passed_trial)
print(employee1.join_date)
print(employee1.full_name)
print(employee1.gender)