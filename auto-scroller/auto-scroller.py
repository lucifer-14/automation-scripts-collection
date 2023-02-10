import pyautogui
import time
print("Scroll speed(-400): ", end="")
val = input() # default -2000
if not val:
	val2 = -20
else:
	val2 = int(int(val)/100)

for i in range(100):
    for j in range(100):
        pyautogui.scroll(val2)
        time.sleep(0.001) 
    # pyautogui.scroll(val)
    print(i)
    time.sleep(2)
