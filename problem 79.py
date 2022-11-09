file = open("C:\\Users\Samadhi Kariyawasam\Documents\python\projecteuler\keylog.txt", 'r')
pins = file.read().split()
passcode = []
for pin in pins:
    position = -1
    for i in pin:
        if i not in passcode:
            passcode.insert(position, i)
        else:
            position = passcode.index(i)+1
print("".join(passcode))

