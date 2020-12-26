

#6__________Don't Pass Null.__________________________________________________________________________
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.hairColor = color

def main():
    Sphynx  = Cat("Sphynx", None)
    FelisCatus = Cat("Felis Catus", "Bicolor")
    print(childCatHairColor(Sphynx , FelisCatus))

def childCatHairColor(cat1, cat2):
        return (cat1.hairColor + cat2.hairColor)

















#5______________________Don't Return Null.______________________________________________________________
def demo5():
    emp1 = Employee("Employee 1",18)
    emp2 = Employee("Employee 2",25)
    emp3 = Employee("Employee 3",30)

    company1 = Company("Company1", [emp1,emp2,emp3])
    company2 = Company("Company2", None)

    employees = getEmployees(company1)
    for employee in employees:
        print(employee.name) 

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        
def getEmployees(company):
    try:
        return list(company.employees)
    except:
        return []










#4_____________Define the Normal Flow___________________
def demo4():
    box1 = ["cake1","cake2","cake3"]
    box2 = 10
    box3 = ["cake1","cake2","cake3","cake4","cake5"]
    sumCake = 0
    sumCake += getCakeCount(box1)
    print(f"Sum cakes count after check box 1: {sumCake}")
    sumCake += getCakeCount(box2)
    print(f"Sum cakes count after check box 2: {sumCake}")
    sumCake += getCakeCount(box3)
    print(f"Sum cakes count after check box 3: {sumCake}")

def getCakeCount(box):
    try:
        return len(box)
    except:
        return 0









#2___________Extract Try/Catch blocks._________________________________________________________________________
import datetime

def updateFile(filePath, newContent):
    f = open(filePath, "a")
    f.write(f"{newContent} \n")
    f.close()

def printFileContent(filePath):
    f = open(filePath, "r")
    content = f.read()
    f.close()
    print(content)

def demo2():
    existFilePath = "demo/cleanCode.txt"
    notExistFilePath = "demo/myGirlFriendInfo.txt"
    path = existFilePath

    newContent = datetime.datetime.now()
    try:
        printFileContent(path)       # Print current file content.
        updateFile(path, newContent) # Update new content.
        printFileContent(path)       # Print new file content.
    except Exception as e:
        print(f"Error: {e}")









#1________________Use Exceptions Rather Than Return Codes____________________________________________________________________
import enum

def demo1():
    num1 = "10" 
    num2 = "It is string."
    num3 = "0"
    num4 = "5"
    # result = divisionUseReturnCode(num1, num3)
    result = divisionUseException(num1, num3)
    print(result)

class errorHandler(enum.Enum):
    DIVISION_BY_ZERO_ERROR = "divideByZero"
    NOT_NUMBER_ERROR = "notNumber"

def divisionUseReturnCode(number1, number2):
    if not number1.isnumeric():
        return errorHandler.NOT_NUMBER_ERROR.value
    if not number2.isnumeric():
        return errorHandler.NOT_NUMBER_ERROR.value
    if int(number2) is 0:
        return errorHandler.DIVISION_BY_ZERO_ERROR.value
    return int(number1) / int(number2) 

def divisionUseException(number1, number2):
    try:
        return int(number1) / int(number2)
    except Exception as e:
        return e

if __name__ == '__main__':
    main()
    print("Program ended!")





    


