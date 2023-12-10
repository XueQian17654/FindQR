import tkinter, threading, time, easygui, pyzbar.pyzbar, pyautogui, pyperclip, os, sys

ls = []
url = []


def fen():
    global ls, url
    while 1:
        r1.update()
        # print(r1.winfo_x(), r1.winfo_y(), r1.winfo_width(), r1.winfo_height())
        # region=[r1.winfo_x() + 10, r1.winfo_y(), r1.winfo_width(), r1.winfo_height() + 40]
        img = pyautogui.screenshot()
        res = pyzbar.pyzbar.decode(img)
        # print(res)

        temp = []
        if res != []:
            for i in res:
                # print(res)
                # i = res[0]
                l = tkinter.Label(r1, text='●', font=("华文行楷", 25), fg="#f60", background='gray')
                url.append(i)
                l.bind("<Button-1>", lambda event: open(event, len(url)))
                temp.append(l)
                x = i.rect.left - 25 + i.rect.width / 2
                y = i.rect.top - 20 + i.rect.height / 2
                # print(x, y)
                l.place(x=x, y=y)

        for i in ls:
            i.destroy()
        ls = temp
        # time.sleep(5000)
        # [Decoded(data=b'??yes', type='QRCODE', rect=Rect(left=154, top=84, width=251, height=251), polygon=[Point(x=154, y=84), Point(x=154, y=335), Point(x=405, y=335), Point(x=405, y=84)], quality=1, orientation='UP')]
        #             '''c = easygui.buttonbox(res[0].data.decode('utf-8'), choices=['复制', '打开'])
        # if c == '复制':
        #     pyperclip.copy(res[0].data.decode('utf-8'))
        # elif c == '打开':
        #     os.startfile(res[0].data.decode('utf-8'))
        # r1.destroy()
        # sys.exit()'''
        time.sleep(0.5)


def open(a, b):
    b = url[b - 1]
    print([a, b])
    c = easygui.buttonbox(b.data.decode('utf-8'), choices=['复制', '打开'])
    if c == '复制':
        pyperclip.copy(b.data.decode('utf-8'))
    elif c == '打开':
        os.startfile(b.data.decode('utf-8'))
    else:
        return
    r1.destroy()
    sys.exit()
    # return 0


def on_resize(evt):
    r1.configure(width=evt.width, height=evt.height)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill='gray', outline='gray')


r1 = tkinter.Tk()
r1.attributes('-fullscreen', True)
r1.overrideredirect(True)

t1 = threading.Thread(target=fen)
t1.daemon = True
t1.start()

r1.title('扫二维码')
# r1.attributes('-toolwindow', True)
r1.wm_attributes('-topmost', 1)

canvas = tkinter.Canvas(r1)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.Y)
canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill='gray', outline='gray')
r1.wm_attributes('-transparentcolor', 'gray')
r1.bind('<Configure>', on_resize)

r1.mainloop()
