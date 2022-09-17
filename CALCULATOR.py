print('CALCULATOR')
print()
print('Choose your Operator:')
print()
print('(1) add')
print()
print('(2) subtract')
print()
print('(3) multiply')
print()
print('(4) division')
print()
operators_ = int(input("Enter Operator: "))


def Ouput():
  val1 = float(input("Enter First Number: "))
  val2 = float(input("Enter Second Number: "))
  return val1, val2

#SWICTH STATEMENT
def add():
  val1, val2 = Ouput()
  return val1 + val2
def subtract():
  val1, val2 = Ouput()
  return val1 - val2 
def multiply():
  val1, val2 = Ouput()
  return val1 * val2 
def division():
  val1, val2 = Ouput()
  return val1 / val2 


operators = [add, subtract, multiply, division]
Output = operators[operators_ - 1]()
print(Output)