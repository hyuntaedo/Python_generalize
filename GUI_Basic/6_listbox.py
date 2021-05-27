from tkinter import *
from typing import List
root = Tk()
root.title("CodeBasic")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # listbox.delete(0)

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가있음")

    # 항목 확인
    print("1번~3번항목까지는", listbox.get(0, 2), "가 있음")

    # 선택된 항목 확인 (index 값으로 반환)
    print("선택된 항목은", listbox.curselection())


btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()
