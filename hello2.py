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

with open('todo.txt') as fp:
    for line in fp.readlines():
        items.append(TodoItem(line.strip()))


def showList():
    print ("Things to do")
    for it in items:
        print(it)

showList()

def addItem2():
    items.append(TodoItem("test: "))

commands = {
    'show': showList,
    'add' : addItem2,
}
cmd = sys.stdin.readline().rstrip()
while cmd != 'quit':

        if cmd in commands:
            commands[cmd]()
        else:
            print('no such command '+ cmd)
        cmd = sys.stdin.readline().rstrip()


with open('todo.txt', 'w') as fp:
    for it in items:
        fp.write(it.text + '\n')
