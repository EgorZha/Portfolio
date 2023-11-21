import tkinter
from tkinter import messagebox

def fun1(event):
    a = [int(i) for i in text1.get("1.0", "end").split()]
    for i in range(len(a)):
      if a[i]>12:
       tkinter.messagebox.showerror("Помилка", "Введіть число від 1 до 12.")
       return
    max_val = max(a)
    min_val = min(a)
    l1 = tkinter.Label(main, text=str(max_val))
    l1.place(x=210, y=150)
    l2 = tkinter.Label(main, text=str(min_val))
    l2.place(x=190, y=180)
    b=round(sum(a)/len(a))
    l3 = tkinter.Label(main, text=str(b))
    l3.place(x=175, y=210)

    p=0
    s=0
    d=0
    v=0

    for i in a:
      if i <= 3 and i>0:
       p=p+1
       tkinter.Label(frame1, text=p).grid(row=1, column=0)
      if i <= 6 and i>3:
        s=s+1
        tkinter.Label(frame1, text=s).grid(row=1, column=1)
      if i<= 9 and i>6:
        d=d+1
        tkinter.Label(frame1, text=d).grid(row=1, column=2)
      if i<=12 and i>9:
        v=v+1
        tkinter.Label(frame1, text=v).grid(row=1, column=3)


main=tkinter.Tk()
main.geometry("350x400")
main.title("Оцінювання")
label1=tkinter.Label(main, text="Проаналізувати оцінки: \n (Введіть оцінки через пропуск)")
label1.place(x=95, y=10)
text1=tkinter.Text(main, width=35, height=3)
text1.place(x=50, y=50)
button1=tkinter.Button(main, text="Проаналізувати")
button1.place(x=110, y=110)
label2=tkinter.Label(main, text="Максимальне значення: ")
label2.place(x=50, y=150)

label3=tkinter.Label(main, text="Мінімальне значення: ")
label3.place(x=50, y=180)

label4=tkinter.Label(main, text="Середнє значення: ")
label4.place(x=50, y=210)
label5=tkinter.Label(main, text="Рівні: ")
label5.place(x=150, y=230)

button1.bind("<Button-1>",fun1)

frame1=tkinter.Frame(main)
frame1.place(x=100, y=250)

le1=tkinter.Label(frame1, text="П", width=4)
le1.grid(row=0, column=0)
le2=tkinter.Label(frame1, text="С", width=4)
le2.grid(row=0, column=1)
le3=tkinter.Label(frame1, text="Д", width=4)
le3.grid(row=0, column=2)
le4=tkinter.Label(frame1, text="В", width=4)
le4.grid(row=0, column=3)
