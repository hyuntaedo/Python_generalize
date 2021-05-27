from tkinter import *
from typing import List

root = Tk()
root.title("CodeBasic")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")


# set이없으면 스크롤을내려도 다시 올라감
listbox = Listbox(frame, selectmode="extended",
                  height=5, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)
root.mainloop()
