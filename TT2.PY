import tkinter as tk

wn = tk.Tk()
wn.title("Выбор трансформаторов тока ")
wn.geometry("530x150+400+200")
frame_0 = tk.Frame(relief=tk.RIDGE, borderwidth=12)
frame_0.pack()


def funcA():
    global cos
    try:
        cos = float(entry1.get())
        if (float(cos)) < 0:
            label1.configure(text="введите косинус корректно")
        if (float(cos)) > 1:
            label1.configure(text="введите косинус корректно")
    except ValueError:
        label1.configure(text="Введите числовое значение")


def funcB():
    global i
    try:
        res = float(entry.get())
        i = (float(res) * 1000) // (u * k * cos)
        label.configure(text=f" Ток равен  {i} A ")
        if (float(res)) < 0:
            label.configure(text="введите положительное число")

    except ValueError:
        label.configure(text="Введите числовое значение")


def funcC():
    if i < 50 and i > 0:
        label3.configure(bg="red", text="прямое включение")
    if i > 50 and i < 75:
        label3.configure(text="ТТ 75/5")
    if i > 75 and i < 100:
        label3.configure(text="ТТ 100/5")
    if i > 100 and i < 125:
        label3.configure(text="ТТ 125/5")
    if i > 120 and i < 150:
        label3.configure(text="ТТ 150/5")
    if i > 150 and i < 200:
        label3.configure(text="ТТ 200/5")
    if i > 200 and i < 250:
        label3.configure(text="ТТ 250/5")
    if i > 250 and i < 300:
        label3.configure(text="ТТ 300/5")
    if i > 300 and i < 400:
        label3.configure(text="ТТ 400/5")
    if i > 400 and i < 630:
        label3.configure(text="ТТ 630/5")
    if i > 630 and i < 800:
        label3.configure(text="ТТ 800/5")
    if i > 800 and i < 1000:
        label3.configure(text="ТТ 1000/5")
    if i > 1000:
        label3.configure(bg="red", text="высоковольтный учет")


k = 1.73
u = 380

label1 = tk.Label(master=frame_0, bg="cyan1", text="Введите cos фи")
entry1 = tk.Entry(master=frame_0, width=4, bg="cyan1")

label = tk.Label(master=frame_0, text="Введите мощность, P кВт")
entry = tk.Entry(master=frame_0, width=4, bg="white")
btfun = tk.Button(master=frame_0, bg="snow", fg="green", text="ок", command=lambda: [funcA(), funcB(), funcC()])

btexit = tk.Button(master=frame_0, bg="red3", fg="yellow", text="выйти", command=wn.destroy)

label2 = tk.Label(master=frame_0, bg="snow2", text="Рекомендуемый трансформатор тока")
label3 = tk.Label(master=frame_0, bg="snow2")

label2.grid(row=3, column=0, sticky="w")
label3.grid(row=3, column=1)
label1.grid(row=0, column=0, sticky="w")
entry1.grid(row=0, column=0, sticky="e")
label.grid(row=1, column=0, sticky="w", padx=0, pady=1)
entry.grid(row=1, column=0, sticky="e")
btfun.grid(row=1, column=1, sticky="n")
btexit.grid(row=4, column=1, sticky="w")

wn.mainloop()
