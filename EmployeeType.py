class EmployeeType:

    numOfEmployees = 0
    extraDays = 2
    
    def __init__(self, name, years, salary):
        self.name = name
        self.years = years
        self.salary = salary
        EmployeeType.numOfEmployees += 1
        self.eid = EmployeeType.numOfEmployees

    def __str__(self):
        return 'Employee: name = {}, years = {}, salary = {}, eid = {}'.format(self.name, self.years, self.salary, self.eid)

    def calculateVacationDays(self):
        return self.years * EmployeeType.extraDays + 10

    def allEmployees():
         print(EmployeeType.numOfEmployees)
        

def mymain():
    emp1 = EmployeeType("Anson Mount", 5, 34599)
    print(emp1)
    print(emp1.calculateVacationDays())
    emp2 = EmployeeType("Anson Mount", 10, 24200)
    emp2.name = "Thor Gundersen"
    #emp2.eid = 1
    print(emp2)
    print(emp2.calculateVacationDays())
    EmployeeType.allEmployees()

if __name__ == '__main__':
    mymain()


