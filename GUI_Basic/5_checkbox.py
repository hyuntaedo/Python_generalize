from tkinter import *
from typing import List
root = Tk()
root.title("CodeBasic")
root.geometry("640x480")
checkbar = IntVar()  # checkbar에 int형으로 값을 저장
checkbox = Checkbutton(root, text="오늘 하루는 안보기", variable=checkbar)
# checkbox.select()  # 기본 체크가 되어있는 상태로 설정
# checkbox.deselect() # defalut값
checkbox.pack()

checkbar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=checkbar2)
checkbox2.pack()


def btncmd():
    print(checkbar.get())  # 0 = 체크해제, 1 = 체크
    print(checkbar2.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()
