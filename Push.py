import tkinter as tk
from os import system

def commit(window,mensaje):
  window.destroy()
  mensaje = "'"+mensaje+"'"
  commit_msg = 'git commit -m '+mensaje
  system('git status')
  system('git add .')
  system(commit_msg)
  system('git push')
  system('pause')

def init_window():
  window = tk.Tk()
  window.title('Git commit')
  window.geometry('240x90')
  window.resizable(width=False, height=False)

  label = tk.Label(window, text='git commit msg:', font=('Arial bold', 10))
  label.place(x=10,y=10)
  entry = tk.Entry(window, width=30)
  entry.place(x=10, y=50)

  button = tk.Button(window,
                    command=lambda: commit(
                      window,
                      entry.get()),text='Push',
                    bg="Blue",
                    fg="white")
  button.place(x=130,y=10)

  window.mainloop()

init_window()