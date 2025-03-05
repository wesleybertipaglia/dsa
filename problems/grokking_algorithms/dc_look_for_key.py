def look_for_key(box):
    if (box.content == None):
        print('box empty')    
    elif (type(box.content) == str):
        print('found key')
    else:
        look_for_key(box.content)

class Box:
    def __init__(self, content = None):
        self.content = content

def test():
    box5 = Box()
    box4 = Box(box5)
    box3 = Box(box4)
    box2 = Box(box3)
    box1 = Box(box2)

    look_for_key(box1)

    box5 = Box("my key")
    box4 = Box(box5)
    box3 = Box(box4)
    box2 = Box(box3)
    box1 = Box(box2)

    look_for_key(box1)

test()