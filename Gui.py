import tkinter, threading, time, easygui, pyzbar.pyzbar, pyautogui, pyperclip, os, sys


def fen():
    while 1:
        r1.update()
        # print(r1.winfo_x(), r1.winfo_y(), r1.winfo_width(), r1.winfo_height())
        img = pyautogui.screenshot(region=[r1.winfo_x() + 10, r1.winfo_y(), r1.winfo_width(), r1.winfo_height() + 40])
        res = pyzbar.pyzbar.decode(img)
        # print(res)
        if res != []:
            # print(res)
            l = tkinter.Label(r1, text='●', font=("华文行楷", 30), fg="green", background='gray')
            x = res[0].rect.left - 25 + res[0].rect.width / 2
            y = res[0].rect.top - 63 + res[0].rect.height / 2
            # print(x, y)
            l.place(x=x, y=y)
            # [Decoded(data=b'??yes', type='QRCODE', rect=Rect(left=154, top=84, width=251, height=251), polygon=[Point(x=154, y=84), Point(x=154, y=335), Point(x=405, y=335), Point(x=405, y=84)], quality=1, orientation='UP')]
            c = easygui.buttonbox(res[0].data.decode('utf-8'), choices=['复制', '打开'])
            if c == '复制':
                pyperclip.copy(res[0].data.decode('utf-8'))
            elif c == '打开':
                os.startfile(res[0].data.decode('utf-8'))
            r1.destroy()
            sys.exit()
        time.sleep(0.5)


def on_resize(evt):
    r1.configure(width=evt.width,height=evt.height)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill='gray', outline='gray')


r1 = tkinter.Tk()

t1 = threading.Thread(target=fen)
t1.daemon = True
t1.start()

r1.title('扫二维码')
r1.attributes('-toolwindow', True)
r1.wm_attributes('-topmost',1)

canvas = tkinter.Canvas(r1)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.Y)
canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill='gray', outline='gray')
r1.wm_attributes('-transparentcolor', 'gray')
r1.bind('<Configure>', on_resize)

r1.mainloop()
