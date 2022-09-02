import tkinter
from tkinter import PhotoImage, Label, Button, Frame, Entry
from tkinter import messagebox, SOLID, StringVar


root = tkinter.Tk()
root.title("Quiz")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = ws - 729
y = hs - 567

img1 = PhotoImage(file="braining.png")

dimensions = "729x567"+"+"+str(int(x/2))+"+"+str(int(y/2))
root.geometry(dimensions)
root.resizable(0, 0)

background_label = Label(
    root,
    image=img1,
    )
background_label.place(x=0, y=0, relwidth=1, relheight=1)

right_ans = [1, 3, 1, 2, 2, 1, 0, 1, 3, 3, 1, 2, 1, 0, 2]
user_ans = []

indexes = []


def generate():
    global indexes
    while (len(indexes) < 10):
        x = random.randint(0, 14)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def details():
    global text_var, txt, lbl, btn_ok, btn_cancel
    x = ws - 275
    y = hs - 150

    text_var = StringVar()

    dimensions = "275x150"+"+"+str(int(x/2))+"+"+str(int(y/2))
    root.geometry(dimensions)

    lbl = Label(root, bg="#ffffff", text="Name",
                font=("Times", 14))
    lbl.place(x=5, y=5)

    txt = Entry(root, font=("Times", 14), border=2,
                textvariable=text_var)
    txt.place(x=70, y=5)

    btn_ok = Button(root, text="OK", height=2, width=10,
                    command=ok)
    btn_ok.place(x=40, y=50)
    btn_cancel = Button(root, text="Cancel", height=2,
                        width=10, command=root.destroy)
    btn_cancel.place(x=140, y=50)


def ok():
    global text_var, txt, lbl, btn_ok, btn_cancel, username
    username = text_var.get()
    if username == "":
        messagebox.showwarning("Blank name",
                               "Name cannot be empty. Try again")
    elif len(username) > 30:
        messagebox.showwarning("Name too long",
                               "Enter name within 30 characters")
    else:
        print(username)
        lbl.destroy()
        txt.destroy()
        btn_cancel.destroy()
        btn_ok.destroy()
        startquiz()


def update():
    global lblquestion, btn1, btn2, btn3, btn4, btn
    global quesnum, indexes
    global frame

    frame.destroy()
    btn.config(background='#ffffff')

    if quesnum < 10:
        lblquestion.config(text=str(quesnum+1)+". " +
                           questions[indexes[quesnum]][0])

        btn1.config(text=choices[indexes[quesnum]][0])

        btn2.config(text=choices[indexes[quesnum]][1])

        btn3.config(text=choices[indexes[quesnum]][2])

        btn4.config(text=choices[indexes[quesnum]][3])

        frame = Frame(
             root,
             bg="#ffffff",
             bd=0,
             )
        frame.place(x=270, y=325)

        quesnum += 1
    else:
        calc()


def check_ans():
    global quesnum, indexes, ans, right_ans, btn
    global app, frame
    if ans == right_ans[indexes[quesnum-1]]:
        btn.config(bg="#008000")
        app = gif.rightGIF.App(frame)
        root.after(2500, update)
    else:
        btn.config(bg="#FF0000")
        app = gif.wrongGIF.App(frame)
        root.after(2500, update)


def result(score):
    global lblimage, lblresulttext, username
    lblquestion.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()

    root.config(background="#ffffff")

    lblimage = Label(
        root,
        background="#ffffff",
        )
    lblimage.pack(pady=(50, 30))

    lblresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
        )
    lblresulttext.pack()
    if score >= 8:
        img = PhotoImage(file="great.png")
        lblimage.configure(image=img)
        lblimage.image = img
        lblresulttext.configure(text="Awesome! You have scored " + str(score) +
                                " out of 10.")
    elif (score >= 5 and score < 8):
        img = PhotoImage(file="ok.png")
        lblimage.configure(image=img)
        lblimage.image = img
        lblresulttext.configure(text="You have scored " + str(score) +
                                " out of 10. You can do better!")
    else:
        img = PhotoImage(file="bad.png")
        lblimage.configure(image=img)
        lblimage.image = img
        lblresulttext.configure(text="You have scored " + str(score) +
                                " out of 10. Try harder!")
    datalib.database.save(username, score)
    root.after(2500, root.destroy)


def calc():
    global indexes, user_ans, right_ans, score
    x = 0
    score = 0
    for i in indexes:
        if user_ans[x] == right_ans[i]:
            score += 1
        x += 1
    result(score)


quesnum = 1


# when 1st option is selected
def selected1():
    global ans, btn
    user_ans.append(0)
    ans = 0
    btn = btn1
    check_ans()


# when 2nd option is selected
def selected2():
    global ans, btn
    user_ans.append(1)
    ans = 1
    btn = btn2
    check_ans()


# when 3rd option is selected
def selected3():
    global ans, btn
    user_ans.append(2)
    ans = 2
    btn = btn3
    check_ans()


# when 4th option is selected
def selected4():
    global ans, btn
    user_ans.append(3)
    ans = 3
    btn = btn4
    check_ans()


def startquiz():
    x = ws - 729
    y = hs - 567
    dimensions = "729x567"+"+"+str(int(x/2))+"+"+str(int(y/2))
    root.geometry(dimensions)
    root.config(background="#C0C0C0")
    global lblquestion, btn1, btn2, btn3, btn4, frame
    lblquestion = Label(
        root,
        background="#ffffff",
        text="1." + questions[indexes[0]][0],
        font=("Titillium", 16),
        width=510,
        relief=SOLID,
        justify="center",
        wraplength=400,
        )
    lblquestion.pack()

    btn1 = Button(
        root,
        text=choices[indexes[0]][0],
        font=("Times", 14),
        width=20,
        height=3,
        background="#ffffff",
        relief=SOLID,
        command=selected1
        )
    btn1.place(x=150, y=100)

    btn2 = Button(
        root,
        text=choices[indexes[0]][1],
        font=("Times", 14),
        width=20,
        height=3,
        background="#ffffff",
        relief=SOLID,
        command=selected2
        )
    btn2.place(x=400, y=100)

    btn3 = Button(
        root,
        text=choices[indexes[0]][2],
        font=("Times", 14),
        width=20,
        height=3,
        background="#ffffff",
        relief=SOLID,
        command=selected3
        )
    btn3.place(x=150, y=230)

    btn4 = Button(
        root,
        text=choices[indexes[0]][3],
        font=("Times", 14),
        width=20,
        height=3,
        background="#ffffff",
        relief=SOLID,
        command=selected4
        )
    btn4.place(x=400, y=230)

    frame = Frame(
        root,
        bg="#ffffff",
        bd=0,
        )
    frame.place(x=270, y=325)


def startgame(event):
    lblexit.destroy()
    lblstart.destroy()
    background_label.destroy()
    root.config(background="#ffffff")
    generate()
    details()


def endgame(event):
    root.destroy()


img2 = PhotoImage(file="start.png")

lblstart = Label(
    root,
    image=img2,
    border=0
    )
lblstart.bind("<Button>", startgame)
lblstart.pack(pady=(400, 0))

img3 = PhotoImage(file="exit.png")

lblexit = Label(
    root,
    image=img3,
    border=0,
    )
lblexit.pack(pady=(10, 0))
lblexit.bind("<Button>", endgame)

root.mainloop()
