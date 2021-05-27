import keyboard
import time
from PIL import ImageGrab


def screenshot():
    # xxxx년 x월 x일 x시 x초.. -> _20210527_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("Image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9키를 누르면 스크린샷 저장


keyboard.wait("esc")  # 사용자가 ESC를 누를 때 까지 프로그램 수행
