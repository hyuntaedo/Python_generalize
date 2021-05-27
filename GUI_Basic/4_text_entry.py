from tkinter import *
root = Tk()
root.title("CodeBasic")
root.geometry("640x480")
txt = Text(root, width=30, height=5)
txt.pack()

# hint text
txt.insert(END, "글자를 입력하시오")

# 한줄로 입력받을 때 사용된다
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력")


def btncmd():
    # line = 1, column= 0 부터 가져온다.
    print(txt.get("1.0", END))
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()
