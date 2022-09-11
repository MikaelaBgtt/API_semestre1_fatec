from tkinter import *
import pandas as pd
from openpyxl import *


data = pd.read_excel('login.xlsx',engine='openpyxl')
print(data.info())


def btn_clicked():
    print("Button Clicked")
    cred = email.get(), senha.get()
    print(cred)


window = Tk()
window.title('Login testes')
window.geometry("1440x1024")
window.configure(bg="#F0F0F0")
canvas = Canvas(
    window,
    bg="#F0F0F0",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(
    795, 560,
    text="Ao clicar em entrar, ou ao continuar com as outras opções \n abaixo, você concorda com os Termos de serviço e confirma \n que leu a Política de privacidade do Pythonators Database.",
    fill="#000000",
    justify=CENTER,
    font=("None", int(13.0)))


img0 = PhotoImage(file = f"img0.png")
img1 = PhotoImage(file="image 1.png")
label_img1 = Label(window, image=img1)
label_img1.place(x=660, y=9)

b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=540, y=600,
    width=512,
    height=64,)

email = Entry(window,
             font="Arial 18",
             bg='#CAD6D6')
email.place(
    x=540, y=380,
    width=518,
    height=50,)
email.pack
senha = Entry(window,
              font="Arial 18",
              bg='#CAD6D6',
              )
senha.pack
senha.place(x=540, y=450,
    width=518,
    height=50)



window.resizable(True, True)
window.mainloop()

top = Toplevel()
        top.title('menu principal')
        top.geometry("1440x1024")