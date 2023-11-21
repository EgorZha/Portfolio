import random
import tkinter
from tkinter import Scale

main=tkinter.Tk()
main.config(bg="#A2CD5A")
main.geometry("350x450")
main.title("Стрижка квіточок")
l1=tkinter.Label(main, text="Введіть кількість квітів в саду:", font='Comfortaa 10')
l1.place(x=50, y=30)
l1.config(bg="#A2CD5A")
text1=tkinter.Text(main, width=30, height=1)
text1.place(x=50, y=60)
button1=tkinter.Button(main, text="Продовжити")
button1.place(x=110, y=90)
button1.config(bg="#FFB6C1")
l2=tkinter.Label(main, text="Оберіть нижню межу:", font='Comfortaa 10')
l2.place(x=80, y=140)
l2.config(bg="#54FF9F")
scale1 = Scale(main, 
orient="horizontal",length=150,from_=20,to=60,tickinterval=10,resolution=10)
scale1.place(x=85, y=170)
scale1.config(bg="#F4A460")
l3=tkinter.Label(main, text="Оберіть верхню межу:", font='Comfortaa 10')
l3.place(x=80, y=250)
l3.config(bg="#54FF9F")
scale2 = Scale(main, 
orient="horizontal",length=200,from_=120,to=160,tickinterval=10,resolution=10)
scale2.place(x=70, y=280)
scale2.config(bg="#F4A460")
button2=tkinter.Button(main, text="Дізнатися")
button2.place(x=120, y=350)
button2.config(bg="#FFB6C1")


def fun1(event):
  global h1
  global h2
  global a
  a=[]
  n=int(text1.get("1.0", "end"))
  for i in range(n):
   a.append(random.randint(20,180))
  print(a)
  return a
  
def fun2(event):
  global a
  k=0
  h1=scale1.get()
  h2=scale2.get()
  for i in a:
      if i>h1 and i<h2:
         k=k+1
  l4=tkinter.Label(main, text="Онук підстриг "+str(k)+" рослин", font='Comfortaa 10')
  l4.place(x=85, y=400)
  l4.config(bg="#AEEEEE")
  
button1.bind("<Button-1>",fun1)
button2.bind("<Button-1>",fun2)
