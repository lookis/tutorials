name = None

def setName(newName):
    global name
    name = newName

def greeting():
    print("Hi, I am "+name)

# 模拟别人在使用我们的代码
if __name__ == "__main__":
    # 我叫 peter
    setName("peter")
    # 啊，刚才弄错了，我要改成大写字母打头的
    setName("Peter")
    # 好了，我来了
    greeting()