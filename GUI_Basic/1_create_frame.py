from tkinter import *

root = Tk()
# title
root.title("Nado GUI")

# 가로x세로 + x좌표 + y좌표
# root.geometry("640x480+500+100")
root.geometry("640x480")
# x(너비),y(높이) 창크기 변경 불가
root.resizable(False, False)

root.mainloop()
