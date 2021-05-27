import os
from tkinter import *
import tkinter

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480")

filename = "mynote.txt"


def create_new_file(filename):
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            textbox.insert(END, file.read())


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(textbox.get("1.0"), END)


menu = Menu(root)
# 파일 메뉴 객체
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=create_new_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="끝내기", command=root.quit)


# 메뉴 바
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


# 스크롤 바
scroll_bar = Scrollbar(root)
scroll_bar.pack(side="right", fill="y")

# 텍스트
textbox = Text(root, yscrollcommand=scroll_bar.set)
textbox.pack(side="left", fill="both", expand=True)

root.config(menu=menu)
scroll_bar.config(command=textbox.yview)
root.mainloop()
