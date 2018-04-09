#Python dataTypes
#List  type

lis = ["hello", 10100, 0.25689, "X"]
print(lis[0:3])

tup = ("tup1", 125, 0.2345, "tup2")
print(tup[0:3])

dic = {}
dic["key1"]="val1"
dic["key2"]="val2"

dic2 = {}
dic2["updatekey"] = "update dict1 with dic2"
dic.update(dic2)
print(dic)
print(dic["key2"])


#nest if elif loop inside of an if else conditional statement
#python checks if the IF condition matches then it steps into the if block and exists the block on first match
#if it does not match with an if or elif then it defaults to ELSE block.

var1 = 44

if var1<100:
    print("var1 is less than 100")
    if var1 > 100:
        print("var1 is greater than 100")
    elif var1 == 100:
        print("var1 is 100")
    elif var1 < 50:
        print("var1 is less than 50")
    elif var1 < 49:
        print("var1 is less than 49")
    else:
        print("var1 is less than 100 and var1 is: " + str(var1))
else:
    print("i dont know what var1 is!")



#While loop - Note that else can be use with WHILE and FOR loops. It works differently depending on where you place it.
#Infinite while loop: while(1) or while(true)
var2 = 0
while var2 < 10:
    print("var2 value is: " + str(var2 + 1))
    var2 += 1
else:
    print("while loop condition is now false")

fruits = ['apple', 'banana', 'beet']
var3 = 'this is a string'

#For Loops allows you to iterate over the members of datatypes easily or over the characters of a string easily
for fruit in fruits:
    print(fruit)
else:
    print("The For loop has finish iterating over list of fruits")


for index in var3:
    print('characters in a String:' + index)
else:
    print('For loop has finish iterating over chars in a String')

#Important to Note that you can have nested loops, while loops inside for loops and vice versa
#Also your nested loops can contain IF ELIF ELSE conditionals statements too.

#Functions
#Example showing function passing by reference, keywords, and default variable
#Note that default varaibles most be declared last when declaring your parameters
def printMe(str, str3, str1 = " Rico is awesome"):
    "This is the Doc String"
    print(str + str1 + " " + str3)
    return


printMe(str3="keyword arguements", str = "\nhello world from my first function!")



#Class

class Person:

#Local Variable: sex
    sex=''

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def getName(self):
        return self.name

    #Assign local variable by calling class name and using dot operator
    def setSex(self, gender):
        Person.sex=gender

    #Return local variable using class name and dot operator followed by attribute
    def getSex(self):
        return Person.sex

Ronald = Person('Ronald',29)
Ronald.setSex('M')
print('Ronald sex is: ' + str(Ronald.getSex()))


#Inheritance, Child classes are declared much like parent class and like functions, you pass in their parents in the parenthesis

class Child(Person):
    def __init__(self):
        print("\nchild constructor")

    def getName(self):
        return "\nParent method overridden"

c = Child()
print(c.getName())


