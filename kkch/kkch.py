from tkinter import*

def out(a, b):
    a = (a * 10000) // 10 / 1000
    b = (b * 10000) // 10 / 1000
    global result
    result.place(x=150, y=600)
    c = str(a) + " + " + str(b) + "i"
    result = Label(window, text=c, bg="White")
    result.pack()
    result.place(x=150, y=400)

def addition():
    a = float(inp1.get())
    b = float(inp2.get())
    c = float(inp3.get())
    d = float(inp4.get())
    x1 = a + c
    x2 = b + d
    out(x1, x2)

def subtraction():
    a = float(inp1.get())
    b = float(inp2.get())
    c = float(inp3.get())
    d = float(inp4.get())
    x1 = a - c
    x2 = b - d
    out(x1, x2)

def multiplication():
    a = float(inp1.get())
    b = float(inp2.get())
    c = float(inp3.get())
    d = float(inp4.get())
    x1 = a * c - b * d
    x2 = a * d + b * c
    out(x1, x2)

def division():
    a = float(inp1.get())
    b = float(inp2.get())
    c = float(inp3.get())
    d = float(inp4.get())
    dv = c ** 2 + d ** 2
    x1 = (a * c - b * (-d)) / dv
    x2 = (a * (-d) + b * c) / dv
    out(x1, x2)


window = Tk()

window["bg"] = "#fafaaa"
window.title("ккч")
window.geometry("390x490")
window.resizable(width=False, height=False)

result = Label(window, text="  ", bg="White")
result.pack()
result.place(x=150, y=400)

inp1 = Entry(window, justify="center")
inp1.pack()
inp1.place(x=50, y=100)
inp2 = Entry(window, justify="center")
inp2.pack()
inp2.place(x=200, y=100)
inp3 = Entry(window, justify="center")
inp3.pack()
inp3.place(x=50, y=200)
inp4 = Entry(window, justify="center")
inp4.pack()
inp4.place(x=200, y=200)

Label(window, text="Калькулятор комплексных чисел, Катков ПИ21-5", bg="lightblue").place(x=60, y=30)
Label(window, text="Введите первое число", bg="lightblue").place(x=125, y=75)
Label(window, text="Введите второе число", bg="lightblue").place(x=125, y=175)
Label(window, text="+", bg="White").place(x=180, y=200)
Label(window, text="+", bg="White").place(x=180, y=100)
Label(window, text="i", bg="White").place(x=330, y=200)
Label(window, text="i", bg="White").place(x=330, y=100)
Label(window, text="Выберете операцию", bg="lightblue").place(x=130, y=275)

Button(window, text="   +   ", bg="White", command=addition).place(x=50, y=300)
Button(window, text="   -   ", bg="White", command=subtraction).place(x=125, y=300)
Button(window, text="   *   ", bg="White", command=multiplication).place(x=200, y=300)
Button(window, text="   /   ", bg="White", command=division).place(x=275, y=300)
Label(window, text="Результат", bg="lightblue").place(x=150, y=375)

window.mainloop()