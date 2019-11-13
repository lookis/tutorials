name1 = None
name2 = None

def setName1(newName):
    global name1
    name1 = newName

def greeting1():
    print("Hi, I am "+name1)

def setName2(newName):
    global name2
    name2 = newName

def greeting2():
    print("Hi, I am "+name2)

if __name__ == "__main__":
    setName1("Peter")
    greeting1()
    setName2("Cate")
    greeting2()