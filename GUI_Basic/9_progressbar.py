import time
import tkinter.ttk as ttk
from tkinter import *
root = Tk()
root.title("CodeBasic")
root.geometry("640x480")

#progress_bar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progress_bar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progress_bar.start(10)  # 10ms마다 움직임
# progress_bar.pack()


# def btncmd():
#     # 작동 중지
#     progress_bar.stop()

p_var2 = DoubleVar()  # 실수 반영
progress_bar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progress_bar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        # progressbar 값을 설정
        p_var2.set(i)
        # 매번 for문동작하는것을 반영
        progress_bar2.update()
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()
root.mainloop()
