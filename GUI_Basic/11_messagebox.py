import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("CodeBasic")
root.geometry("640x480")


def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료")


def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진")


def error():
    msgbox.showerror("에러", "결제 오류가 발생")


def OkCancel():
    msgbox.askokcancel("확인/취소", "예매 하시겠습니까?")


def retryCancel():
    msgbox.askretrycancel("재시도/취소", "일시적인 오류입니다 다시 시도 하시겠습니까?")


def YesNo():
    msgbox.askyesno("예/아니요", "역방향인데 예매 하시겠습니까?")


def YesNoCancel():
    response = msgbox.askyesnocancel(
        title=None, message="애매 내역이 저장되지않았습니다. \n저장하시겠습니까?")
    # 네 :저장후 종료
    # 아니요 : 저장안하고 종료
    # 취소 : 프로그램 종료/취소
    print("응답", response)
    if response == 1:
        print("네")
    elif response == 0:
        print("아니요")
    else:
        print("취소")


# pop up이미지
btn = Button(root, command=info, text="알림")
btn2 = Button(root, command=warn, text="경고")
btn3 = Button(root, command=error, text="에러")
btn4 = Button(root, command=OkCancel, text="확인 취소")
btn5 = Button(root, command=retryCancel, text="재시도")
btn6 = Button(root, command=YesNo, text="예 아니요")
btn7 = Button(root, command=YesNoCancel, text="예 아니요 취소")


btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
root.mainloop()
