import random
import tkinter
from tkinter import messagebox

main=tkinter.Tk()
main.config(bg="#FCE6C9")
main.geometry("350x400")
main.title("Відгадай число")
l1=tkinter.Label(main, text="Введіть своє ім'я:", font='Comfortaa 10')
l1.place(x=50, y=30)
text1=tkinter.Entry(main, width=28)
text1.place(x=50, y=60)
button1=tkinter.Button(main, text="Підтвердити")
button1.place(x=110, y=90)
l2=tkinter.Label(main, text="Введіть число(натисніть start):", font='Comfortaa 10')
l2.place(x=50, y=200)
text2=tkinter.Text(main, width=30, height=1)
text2.place(x=50, y=230)
button2=tkinter.Button(main, text="Start")
button2.place(x=110, y=260)
l1.config(bg="#FCE6C9")
l2.config(bg="#FCE6C9")

def fun1(event):
  global a
  global number
  name = text1.get()
  l1.destroy()
  text1.destroy()
  button1.destroy()
  l5=tkinter.Label(main, text="Привіт "+ name +" я загадав число \n від 1 до 10,спробуй його вгадати", font='Comfortaa 10')
  l5.place(x=50, y=30)
  a=[]
  for i in range(10):
   a.append(random.randint(1,10))
  number=random.choice(a)
  l5.config(bg="#97FFFF")

s=0

def fun2(event):
  global s
  ch = int(text2.get("1.0", "end"))
  s += 1
  if ch == number:
     messagebox.showinfo(title=":)", message="Молодець!")
     button2.destroy()
     l6=tkinter.Label(main, text="Молодець!Ти пройшов гру.", font='Comfortaa 10')
     l6.place(x=70, y=260)
     l6.config(bg="#97FFFF")
  if ch < number:
     messagebox.showwarning(title="Спробуй ще!", message="Число менше загаданого")
  if ch > number:
     messagebox.showwarning(title="Спробуй ще!", message="Число більше загаданого")
  if s == 3 and ch != number:
        messagebox.showerror(title="Помилка!", message="Спроби закінчилися.")
        button2.destroy()
        l7=tkinter.Label(main, text="Загадане число було "+str(number), font='Comfortaa 10')
        l7.place(x=70, y=260)
        l7.config(bg="#97FFFF")


button1.bind("<Button-1>",fun1)
button2.bind("<Button-1>",fun2)
