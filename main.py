import tkinter as tk

clicks = 0
upgrade = 1

root = tk.Tk()
root.geometry('700x700')
root.title('Burger Clicker')

def click():
  global clicks
  clicks += upgrade

burger = tk.Button(root, bg = 'gray30', image = tk.PhotoImage('pixelBurger.png'), command = click)
burger.grid(row=350,column=350)

root.mainloop()