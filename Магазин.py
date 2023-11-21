import tkinter
from tkinter import messagebox
import random

def fun1(event):
    c = []
    a = [int(i) for i in text1.get("1.0", "end").split()]
    for i in range(len(a)):
        if a[i] > 200:
            tkinter.messagebox.showerror("Помилка", "Введіть кількість покупців менше 200!")
            return
    for i in range(a[i]):
        money = 0
        money += random.randint(1, 500)
        c.append(money)

    profit = sum(c)
    l1 = tkinter.Label(main, text=str(profit))
    l1.place(x=230, y=170)
    b=round(sum(c)/len(c))
    l2 = tkinter.Label(main, text=str(b))
    l2.place(x=255, y=200)
    l1.config(bg="#FCE6C9")
    l2.config(bg="#FCE6C9")

    n = 0

    for i in c:
        if i > b:
           n += 1 

    l3 = tkinter.Label(main, text=str(n))
    l3.place(x=230, y=246)
    l3.config(bg="#FCE6C9")


main=tkinter.Tk()
main.geometry("350x400")
main.config(bg="#FF8C69")
main.title("Магазин")
label1=tkinter.Label(main, text="Введіть кількість покупців \n обслужених за день(Менше 200):")
label1.place(x=60, y=30)
text1=tkinter.Text(main, width=35, height=2)
text1.place(x=50, y=70)
button1=tkinter.Button(main, text="Проаналізувати")
button1.place(x=110, y=120)
label2=tkinter.Label(main, text="Денний прибуток магазину: ")
label2.place(x=50, y=170)
label3=tkinter.Label(main, text="Середня суму споживчого чека: ")
label3.place(x=50, y=200)
label4=tkinter.Label(main, text="Покупці які витратили більше \n за суму середнього чеку: ")
label4.place(x=50, y=230)
label1.config(bg="#FF8C69")
label2.config(bg="#4876FF")
label3.config(bg="#4876FF")
label4.config(bg="#4876FF")
button1.config(bg="#EEAEEE")

button1.bind("<Button-1>",fun1)
