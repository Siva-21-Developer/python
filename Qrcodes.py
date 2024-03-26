from tkinter import *
import pyqrcode
win = Tk()
win.geometry("3000x3000")
win.resizable(True, True)
entry = StringVar()
save = StringVar()
def saves():
    global f1
    if save.get():
        qr.png(save.get()+".png", scale=8)
        Label(f1, text="Save successfully", background="yellow", foreground="black", borderwidth=10,
              highlightbackground="black", highlightthickness=5, width=30).place(x=220, y=650)
    if not save.get():
        Label(f1, text="enter the name", background="yellow", foreground="black", borderwidth=10, highlightbackground="black", highlightthickness=5, width=30).place(x=220, y=650)

def generate():
    if entry.get():
        global qr, photo
        qr = pyqrcode.create(f"Name : {entry.get()} \n"
                             f"Age : 21 \n"
                             f"Contact No: 8110015941")
        photo = BitmapImage(data=qr.xbm(scale=3))
        Label(f1, text="Qrcode is created successfully", background="yellow", foreground="black", borderwidth=10, highlightbackground="black", highlightthickness=5, width=30).place(x=220, y=650)
    if not entry.get():
        Label(f1, text="Please enter something", borderwidth=10, background="yellow", width=30, highlightthickness=5, highlightbackground="black").place(x=220, y=650)

def showcode():
    label_get.config(image=photo)

label = Label(win, text="QR code creator", font=('aria', 20, 'bold'), foreground="orange", background="black", width=400, height=2, highlightthickness=15, highlightcolor="yellow", highlightbackground="orange")
label.pack()

f1 = Frame(win, background="lightgreen", borderwidth=5, highlightthickness=4, highlightbackground="black", width=700, height=635).place(x=0, y=100)
Label(f1, text="ENTER THE ULR  :", font=('impact',15, "bold"), borderwidth=5, background="orange").place(x=10, y=150)
Entry(f1, background="lightblue", width=60, textvariable=entry, borderwidth=5, highlightbackground="black", highlightthickness=2, highlightcolor='black').place(x=200, y=155)
Button(f1, text="CREATE", borderwidth=5, background="lightblue", font=('aria',13, 'bold'), foreground="red", command=generate).place(x=300, y=250)
Entry(f1, background="lightblue", width=60, textvariable=save, borderwidth=5, highlightbackground="black", highlightthickness=2, highlightcolor='black').place(x=200, y=355)
Label(f1, text="ENTER THE NAME  :", font=('impact',15, "bold"), borderwidth=5, background="orange").place(x=10, y=350)
Button(f1, text="SAVE", width=7, borderwidth=5, background="lightblue", font=('aria',13, 'bold'), foreground="red", command=saves).place(x=300, y=450)

f2 = Frame(win,  background="lightgreen", borderwidth=5, highlightthickness=4, highlightbackground="black", width=700, height=635).place(x=700,y=100)

Button(f2, text="VIEW", font=("aira",15,"bold"), background="lightblue", foreground="red", command=showcode).place(x=980, y=650)
label_get = Label(f2, background="lightgreen")
label_get.place(x=950, y=310)

win.mainloop()