from tkinter import  *

def calcular():
 if peso.get() == '' or altura.get() == '':
     resposta['text'] = 'Por favor Digite os dados'
 else:
     peso1 = float(peso.get())
     altura1 = float(altura.get())
     imc = peso1/altura1**2

     resposta['text'] = round(imc,2)
     if imc <= 18.4:
         respostaPeso['text'] = 'Abaixo do peso'
     elif imc >= 18.5 and imc <= 24.9:
         respostaPeso['text'] = 'Peso Normal'
     elif imc >= 25 and imc <= 29.9:
         respostaPeso['text'] = 'Acima do peso'
     elif imc >= 30 and imc <= 34.9:
         respostaPeso['text'] = 'Obesidade tipo I'
     elif imc >= 34 and imc <= 39.9:
         respostaPeso['text'] = 'Obesidade tipo II'
     else:
         respostaPeso['text'] = 'Obesidade tipo III'






janela = Tk()
janela.title('Calcular massa corporal')
janela.geometry('300x150')
janela.resizable(False, False)

Label(janela, text='Insira seu dados').grid(row=0, column=0, columnspan=2)

Label(janela,text='PESO').grid(row=1, column=0)

peso = Entry(janela)
peso.grid(row=1, column=1)

Label(janela,text='ALTURA').grid(row=2, column=0)

altura = Entry(janela)
altura.grid(row=2, column=1)


Button(janela,text='CALCULAR', command=calcular, bg='yellow').grid(row=3, column=0)

resposta = Label(janela, text='Está acima do peso?')
resposta.grid(row=3, column=1)

respostaPeso = Label(janela, text='Vamos calcular!')
respostaPeso.grid(row=4, column=1)

deselvolvedor = Label(janela, text='Programa feito por César Severo')
deselvolvedor.grid(row=5, column=1)



janela.mainloop()