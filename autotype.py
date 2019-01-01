import pyautogui
l=[]
file = open("pulp.txt", 'rU')
line=' '
while line:
    line=file.read(1)
    l.append(line)
pyautogui.typewrite(l[0:len(l)-2], interval=0.01)
