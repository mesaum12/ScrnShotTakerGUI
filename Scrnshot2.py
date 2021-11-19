# we will be using pyauto gui for taking screen shots of our screen and save it in our folder
import time
import pyautogui
import tkinter as tk

def screenshot():
    name=int(round(time.time()*1000))
    name='/home/ubuntu/Desktop/PythonProjects/Screenshots/{}.png'.format(name)
    time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button=tk.Button(frame , text = "Capture Screenshot",command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(frame,text="Quit",command=quit)

close.pack(side=tk.LEFT)
root.mainloop()
