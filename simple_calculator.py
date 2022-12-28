# Provide a program for the calculator from terminal.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):                        #FOR ADDITION
        return self.num1 + self.num2

    def subtract(self):                   #FOR SUBTRACTION
        return self.num1 - self.num2

    def multiply(self):                   #FOR MULTIPLICATION
        return self.num1 * self.num2

    def Divide(self):                     #FOR DIVIDE
        return self.num1 / self.num2

####### FOR EXPRESSION 624-12 #############
num1 = 624
num2 = 12
my_Result = Calculator(num1, num2)
my_Result.subtract()
print("the answer for expression 564/10 is:",my_Result.subtract())

##### FOR EXPRESSION 564 / 10 ############
num1=564
num2=10
my_Result = Calculator(num1, num2)
my_Result.Divide()
print("the answer for expression 564/10 is:",my_Result.Divide())

##### FOR EXPRESSION 456*1234-09=12 #######
num1=456
num2=1234
num3=9
num4=12
x=num1*num2
y=num3-num4
my_Result = Calculator(x,y)
my_Result.add()
print("the answer for expression 456*1234+09-12 is:",my_Result.add())

#if select == 1:
 #   print(num1, "+", num2, "=", my_Result.add())
#elif (select == 2):
 #   print(num1, "-", num2, "=", my_Result.subtract())
#elif (select == 3):
 #   print(num1, "*", num2, "=", my_Result.multiply())
#elif (select == 4):
 #   print(num1, "/", num2, "=", my_Result.Divide())

#else:
 #   print("invalid number")




