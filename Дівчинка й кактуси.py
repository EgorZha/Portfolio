import tkinter
import random
g = []
def fun1(event):
 global g
 g = int(text1.get("1.0", "end"))
 a=[]
 k=0
 for i in range(g):
  a.append(random.randint(0,5))
 for i in a:
  if i==0:
    k=k+1
    l3=tkinter.Label(main, text="Яринка не доторкнулася \n до кактусів: ")
    l3.place(x=55, y=200)
    l4 = tkinter.Label(main, text=str(k))
    l4.place(x=180, y=217)

main=tkinter.Tk()
main.geometry("350x400")
main.title("Кактуси")
l1=tkinter.Label(main, text="Введіть кількість кактусів в оранжереї:")
l1.place(x=50, y=20)
text1=tkinter.Text(main, width=35, height=3)
text1.place(x=50, y=50)

button1=tkinter.Button(main, text="Далі")
button1.place(x=135, y=110)


button1.bind("<Button-1>",fun1)
