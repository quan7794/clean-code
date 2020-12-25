

#6____________________________________________________________________________________
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    point1 = None
    point2 = Point(10,15)
    print(multiTwoPointY(point1,point2))

def multiTwoPointY(point1, point2):
    try:
        return (point1.y * point2.y)
    except Exception as e:
        print(f"Can not multi, error: {e}")

#5____________________________________________________________________________________
def demo5():
    emp1 = Employee("Employee 1",18)
    emp2 = Employee("Employee 2",25)
    emp3 = Employee("Employee 3",30)

    company1 = Company("Company1", [emp1,emp2,emp3])
    company2 = Company("Company2", None)

    employees = getEmployees(company2)
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


#4____________________________________________________________________________________
def demo4():
    box1 = ["cake1","cake2","cake3"]
    box2 = 10
    box3 = ["cake1","cake2","cake3","cake4","cake5"]
    sumCake = 0
    sumCake += getCakeCount(box1)
    print(sumCake)
    sumCake += getCakeCount(box2)
    print(sumCake)
    sumCake += getCakeCount(box3)
    print(sumCake)
def getCakeCount(box):
    try:
        return len(box)
    except:
        return 0
#3____________________________________________________________________________________
def tryOpenFile(filePath):
    try:
        f = open(filePath, "r")
        content = f.read()
        f.close()
        print(content)
    except Exception as e:
        createFile(filePath)

def createFile(filePath):
    return    

#2____________________________________________________________________________________
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

#1____________________________________________________________________________________
import enum
class errorHandler(enum.Enum):
    DIVISION_BY_ZERO_ERROR = "divideByZero"
    NOT_NUMBER_ERROR = "notNumber"
def divisionUseReturnCode(number1, number2):
    if not number1.isnumeric():
        return errorHandler.NOT_NUMBER_ERROR
    if not number2.isnumeric():
        return errorHandler.NOT_NUMBER_ERROR
    if int(number2) is 0:
        return errorHandler.DIVISION_BY_ZERO_ERROR
    return int(number1) / int(number2) 
def divisionUseException(number1, number2):
    try:
        return int(number1) / int(number2)
    except Exception as e:
        return e
def demoExceptionAndReturnCode():
    num1 = "10" 
    num2 = "It is not number"
    num3 = "0"
    num4 = "5"
    result = divisionUseException(num1,num3)
    print(result)

if __name__ == '__main__':
    main()
    # demoExceptionAndReturnCode()





    


