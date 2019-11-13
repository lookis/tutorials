def createUser():
    user = {
        "name": None,
    }
    def setName(newName):
        user['name'] = newName
    def greeting():
        print("Hi, I am "+user['name'])
    user['setName'] = setName
    user['greeting'] = greeting
    return user
        
if __name__ == "__main__":
    user1 = createUser()
    user1['setName']('Peter')
    user1['greeting']()
    user2 = createUser()
    user2['setName']('Cate')
    user2['greeting']()