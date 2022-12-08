from collections import deque

f = open("input.txt")

class Entry:
    def __init__(self, name) -> None:
        self.name: str = name

    def size(self):
        pass

class Directory(Entry):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.children : dict[str, Entry] = {}

    def addChild(self, entry):
        self.children.append(entry)

    def size(self):
        return 0

    def __str__(self) -> str:
        return f'{self.name}: [{self.children}]'

    def __repr__(self):
        return self.__str__()

class File(Entry):
    def __init__(self, name, size) -> None:
        super().__init__(name)
        self.size = size

    def __str__(self) -> str:
        return f'{self.name} ({self.size})'

    def __repr__(self):
        return self.__str__()

root = Directory('/')

directoryStack = deque([root])

dirSum = 0


def traverse(directory: Directory):
    global dirSum
    sum = 0

    for entry in directory.children.values():
        print(entry)
        print(type(entry))
        if isinstance(entry, File):
            print('is file')
            sum += entry.size
        else:
            print('is dir')
            sum += traverse(entry)

    if sum < 100000:
        dirSum += sum
    
    return sum


while line := f.readline().strip():
    tokens = line.split(' ')
    print(tokens)
    if (tokens[0] == '$'):
        if (tokens[1] == 'cd'):
            if (tokens[2] == '..'):
                directoryStack.popleft()
            elif (tokens[2] != '/'):
                directoryStack.appendleft(directoryStack[0].children[tokens[2]])
            
    elif (tokens[0] == 'dir'):
        directoryStack[0].children[tokens[1]] = Directory(tokens[1])
    else: 
        directoryStack[0].children[tokens[1]] = File(tokens[1], int(tokens[0]))


print(root)

traverse(root)

print(dirSum)



