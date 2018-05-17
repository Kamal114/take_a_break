import webbrowser
import time

num_of_breaks = 3
break_count =0

print("The timer starts at "+time.ctime())
while(break_count<3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=99iyGGbaRWE")
    break_count = break_count + 1
