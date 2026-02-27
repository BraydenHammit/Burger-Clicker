import tkinter as tk

clicks = 0
upgrade = 1

root = tk.Tk()
root.geometry('700x700')
root.title('Burger Clicker')

def click():
  global clicks
  clicks += upgrade

burger = tk.Button(root, image = tk.photoImage('path'), command = click)
burger.grid(row=0,column=0)

root.mainloop()
