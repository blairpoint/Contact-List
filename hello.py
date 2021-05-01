import sys

class TodoItem(object):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def update(self,newText):
        self.text = newText

items = [TodoItem("hello"),TodoItem("world")]

def addItem(text):
    items.append(TodoItem(text))


def showList():
    print ("Things to do")
    for it in items:
        print(it)

showList()

commands = {
    'show': showList,
}
cmd = sys.stdin.readline().rstrip()
while cmd != 'quit':
    # if cmd == 'show':
    #     showList()
    # elif cmd == 'add':
        if cmd in commands:
            commands[cmd]()
        else:
            print('no such command '+ cmd)
        cmd = sys.stdin.readline().rstrip()




print("Enter item to add:")
newItem = sys.stdin.readline().rstrip()
addItem(newItem)
showList()
