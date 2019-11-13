def createUser():
    return {}

def setName(user, newName):
    user['name'] = newName

def greeting(user):
    print("Hi, I am "+user['name'])

if __name__ == "__main__":
    user1 = createUser()
    setName(user1, 'Peter')
    greeting(user1)
    user2 = createUser()
    setName(user2, "Cate")
    greeting(user2)