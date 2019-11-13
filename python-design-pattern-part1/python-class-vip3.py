class User():
    def __init__(self):
        self.name = None
    
    def setName(self, newName):
        self.name = newName

    def greeting(self):
        print("Hi, I am "+self.name)

class VipUser(User):
    def greeting(self):
        super().greeting()
        print("I am a VIP")


if __name__ == "__main__":
    user1 = User()
    user1.setName('Peter')
    user1.greeting()
    user2 = VipUser()
    user2.setName('Cate')
    user2.greeting()
    