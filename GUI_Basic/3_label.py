from tkinter import *
root = Tk()
root.title("CodeBasic")

root.geometry("640x480")

label1 = Label(root, text="hi")
label1.pack()
photo = PhotoImage(file="./check.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또만나요")
    #안에서 바꿀려면 전역변수로 선언을 해야함
    global photo2
    photo2 = PhotoImage(file="./x.png")
    label2.config(image=photo2)


btn1 = Button(root, text="click", command=change)
btn1.pack()
root.mainloop()
