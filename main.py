import tkinter
import pygame
import random
from tkinter import *
import tkinter.messagebox
from win32api import GetSystemMetrics

# 변수 설정
test = [0 for i in range(218)]
order = []
now = 0
pygame.init()
pygame.mixer.init()
status = False


# 함수정의
def soundPlay(choose, now):
    if choose == 0:
        f = 'sounds/keyword' + str(now) + ".mp3"
    else:
        f = 'sounds/explain' + str(now) + ".mp3"
    pygame.mixer.music.load(f)
    pygame.mixer.music.play(loops=0)


def set_label(label2):
    global now, status

    if not status:
        label2.place(x=100, y=300, width=800, height=50)
        soundPlay(0, order[now])
        status = True
    else:
        label2.place(x=1000, y=300, width=800, height=50)
        status = False


def initSystem():
    global keywords, explains, now
    count = 0

    # 정보처리기사 문제 읽기
    f = open("document.txt", 'r', encoding='UTF-8')
    data = f.read()
    f.close()

    data = data.split("\n\n ")
    data2 = []
    keywords = []
    explains = []

    for i in range(len(data)):
        data2.append(data[i].split(" : "))

    for j in data2:
        keywords.append(j[0])
        explains.append(j[1])

    while count != 218:
        num = random.randrange(0, 218)
        if test[num] == 0:
            test[num] = 1
            count += 1
            order.append(num)


def nextSlide(explain, keyword):
    global now, status
    num = now + 1
    if num == 218:
        num = 0
    now = num
    explain.set(str(order[now]) + "번 문제\n\n\n" + explains[order[now]])
    keyword.set(keywords[order[now]])
    soundPlay(1, order[now])
    label2.place(x=1000, y=300, width=800, height=50)
    status = False


def preSlide(explain, keyword):
    global now, status
    num = now - 1
    if num == - 1:
        num = 217
    now = num
    explain.set(str(order[now]) + "번 문제\n\n\n" + explains[order[now]])
    keyword.set(keywords[order[now]])
    soundPlay(1, order[now])
    label2.place(x=1000, y=300, width=800, height=50)
    status = False


def search(textbox, explain, keyword):
    global status
    try:
        page = int(textbox.get("1.0", "end"))
        if page >= 218 or page < 0:
            tkinter.messagebox.showwarning("오류(Error)", "0~217 사이의 값만 입력하시오. (Insert the number that you want to "
                                                        "search, and use a number from 0 to 217")
        else:
            explain.set(str(page) + "번 문제\n\n\n" + explains[page])
            keyword.set(keywords[page])
            soundPlay(1, page)
            label2.place(x=1000, y=300, width=800, height=50)
            status = False
    except:
        tkinter.messagebox.showwarning("오류", "0~217 사이의 값만 입력하시오.")


if __name__ == "__main__":
    # 초기화
    initSystem()

    # 화면설정
    root = Tk()
    root.title("정보처리기사 시험준비")
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    x = str(int(GetSystemMetrics(0) / 2 - 1000 / 2))
    y = str(int(GetSystemMetrics(1) / 2 - 500 / 2))
    root.geometry("1000x500+" + x + "+" + y)
    root.resizable(False, False)

    # 화면 라벨 설정
    explain = tkinter.StringVar()
    explain.set(str(order[now]) + "번 문제\n\n\n" + explains[order[now]])
    keyword = tkinter.StringVar()
    keyword.set(keywords[order[now]])
    label = tkinter.Label(root, font=("맑은 고딕", 10), textvariable=explain, wraplength=600)
    label.place(x=200, y=0, width=600, height=200)
    label2 = tkinter.Label(root, textvariable=keyword)

    # 버튼생성
    btn = tkinter.Button(root, text="정답", font=("맑은 고딕", 10), command=lambda: set_label(label2))
    btn.place(x=475, y=200, width=50, height=50)

    btn_left = tkinter.Button(root, text="◀", bg="black", fg="white", command=lambda: preSlide(explain, keyword))
    btn_left.place(x=0, y=0, width=100, height=500)

    btn_right = tkinter.Button(root, text="▶", bg="black", fg="white", command=lambda: nextSlide(explain, keyword))
    btn_right.place(x=900, y=0, width=100, height=500)

    # 텍스트 박스
    textbox = tkinter.Text(root, height=1, width=10)
    textbox.place(x=800, y=30)
    btn_check = tkinter.Button(root, text="찾기", command=lambda: search(textbox, explain, keyword))
    btn_check.place(x=800, y=50)

    # 문제읽기
    soundPlay(1, order[now])

    root.mainloop()
