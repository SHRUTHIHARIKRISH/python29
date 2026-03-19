# Encapsulation = Hiding data + controlling access
class emp():
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # 🔒 private

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary

ob = emp("Shruthi", 100000)

print(ob.get_salary())   # ✅ allowed

ob.set_salary(200000)    # ✅ allowed
print(ob.get_salary())   # print(ob.__salary)   ERROR
