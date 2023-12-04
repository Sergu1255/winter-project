import tkinter as tk
from live import *
window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")
buttonclicked = False

def changeVal():
   if buttonclicked:
      buttonclicked= True

    
def display_variable():
    global a
    a = int(entry.get())
    return a

def create_range(num):
  num_list = []
  for i in range(num+1):
    num_list.append(i)
  return num_list


hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()
a = 0
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Display variable", command=create_range)
button.pack()
if button is pressed:
   print(num_list)

tk.mainloop()

test = display_variable
print(test)