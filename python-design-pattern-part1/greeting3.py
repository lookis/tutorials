names = {}

def setName(id, newName):
    global names
    names[id] = newName

def greeting(id):
    print("Hi, I am "+names[id])

if __name__ == "__main__":
    setName(1, "Peter")
    greeting(1)
    setName(2, "Cate")
    greeting(2)