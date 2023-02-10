import tkinter as tk
import pyautogui
import time
import threading
import keyboard

window = tk.Tk()
window.title('Auto Scroller')
window.geometry('300x200')
pause = True
exit = False
pyautogui.FAILSAFE = False

def stop_scroll():
    global pause
    pause = not pause
    #if pause:
        #pause = False
    #else:
        #pause = True


def exit():
    global exit
    exit = True
        

def scroll():
    while True:
        global pause
        global exit
        o_val=int(text_box.get(1.0, "end-1c")) # default -2000
        if keyboard.is_pressed('up'):

            o_val= abs(o_val)
            text_box.delete(1.0, "end-1c")
            text_box.insert("1.0", o_val)
        if keyboard.is_pressed('down'):

            o_val= abs(o_val)*-1
            text_box.delete(1.0, "end-1c")
            text_box.insert("1.0", o_val)
        if keyboard.is_pressed('right'):

            n_val=abs(o_val) + 100
            if o_val < 0:
                n_val = n_val * -1
            text_box.delete(1.0, "end-1c")
            text_box.insert("1.0", n_val)
        if keyboard.is_pressed('left'):

            n_val=abs(o_val) - 100
            if n_val <= 0:
                n_val = 0
            if o_val < 0:
                n_val = n_val * -1
            text_box.delete(1.0, "end-1c")
            text_box.insert("1.0", n_val)
        if keyboard.is_pressed('END'):
            exit()
        if keyboard.is_pressed('space'):
            stop_scroll()
            time.sleep(0.5)

        if pause == False:

            if o_val:
                val2 = int(int(o_val)/100)
                pyautogui.scroll(val2)
                time.sleep(0.001)
        else:
            time.sleep(0.05)
        print(pause)
        if exit == True:
            break
    window.quit()


text_box = tk.Text(window)
text_box.place(x=10, y=20, width=280, height=30)
text_box.insert(tk.END, "-4000")

pause_btn = tk.Button(window, text="P", command=stop_scroll)
pause_btn.place(x=125, y=70, width=50, height=50)

exit_btn = tk.Button(window, text="E", command=exit)
exit_btn.place(x=230, y=70, width=50, height=50)

t1 = threading.Thread(target=scroll)
t1.start()

window.mainloop()
t1.join()