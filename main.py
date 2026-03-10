import tkinter as tk

clicks = 0
upgrade = 1

root = tk.Tk()
root.geometry('700x700')
root.title('Burger Clicker')

def click():
  global clicks
  global score
  clicks += upgrade
  score.grid_forget()
  score = tk.Label(root, text = clicks)
  score.grid(row=0,column=0)

score = tk.Label(root, text = clicks)
score.grid(row=0,column=0)

burger = tk.Button(root, bg = 'gray30', width = 212, height=183, command = lambda: click())
burger.grid(row=350,column=350)

root.mainloop()