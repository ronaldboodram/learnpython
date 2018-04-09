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

var1 = 10
#nest if elif loop inside of an if else conditional statement
#python checks if the IF condition matches then it steps into the if block and exists the block on first match
#if it does not match with an if or elif then it defaults to ELSE block.
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
