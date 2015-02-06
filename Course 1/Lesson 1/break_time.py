import time
import webbrowser

num = 0
print("This program started on "+time.ctime())
while(num<1):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=4K1hoMlxQmg")
    num+=1
