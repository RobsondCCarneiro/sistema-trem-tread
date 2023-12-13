#EDMILSON DIAS TAVARES FILHO
#JHONAT HEBERSON AVELINO DE SOUZA
#ROBSON DA COSTA CARNEIRO
#Grupo 1 - Sistemas de Tempo Real
import threading
from tkinter import *
import time

#imprimindo os trilhos
def visualizarPosicaoDosTrens(window):
    window.geometry("400x400")    

    trilhoVerde = canvas.create_rectangle(20, 20, 120, 120, outline="green", width="5")
    trilhoAzul = canvas.create_rectangle(20, 150, 380, 250, outline="blue", width="5")
    trilhoRoxo = canvas.create_rectangle(150, 20, 250, 120, outline="purple", width="5")
    trilhoAmarelo = canvas.create_rectangle(280, 20, 380, 120, outline="yellow", width="5")
    

#Botoes que aumentam e abaixam a velocidade do trem
def painelDeControle(window):
    global verde
    global amarelo
    global roxo
    global azul

    botaoAumentarVelocTremVerde = Button(window, text="+ 0.1", bg='green', command=lambda: aumentarVelocidade(verde))
    botaoDiminuirVelocTremVerde = Button(window, text=" - 0.1 ", bg='green', command= lambda: diminuirVelocidade(verde))
    botaoAumentarVelocTremVerde.place(x = 20, y = 300)
    botaoDiminuirVelocTremVerde.place(x = 20, y = 350)

    botaoAumentarVelocTremRoxo= Button(window, text="+ 0.1", bg='purple', command=lambda: aumentarVelocidade(roxo))
    botaoDiminuirVelocTremRoxo = Button(window, text=" - 0.1 ", bg='purple', command= lambda: diminuirVelocidade(roxo))
    botaoAumentarVelocTremRoxo.place(x = 120, y = 300)
    botaoDiminuirVelocTremRoxo.place(x = 120, y = 350)

    botaoAumentarVelocTremAmarelo= Button(window, text="+ 0.1", bg='yellow', command= lambda: aumentarVelocidade(amarelo))
    botaoDiminuirVelocTremAmarelo = Button(window, text=" - 0.1 ", bg='yellow', command=lambda: diminuirVelocidade(amarelo))
    botaoAumentarVelocTremAmarelo.place(x = 220, y = 300)
    botaoDiminuirVelocTremAmarelo.place(x = 220, y = 350)

    botaoAumentarVelocTremAzul= Button(window, text="+ 0.1", bg='blue', command=lambda: aumentarVelocidade(azul))
    botaoDiminuirVelocTremAzul = Button(window, text=" - 0.1 ", bg='blue', command=lambda: diminuirVelocidade(azul))
    botaoAumentarVelocTremAzul.place(x = 320, y = 300)
    botaoDiminuirVelocTremAzul.place(x = 320, y = 350)

#Funcao que aumenta a velocidade que sera utilizado como parametro na funcao time.sleep(velocidadeTremCor)
def aumentarVelocidade(trem):
    global velocidadeTremVerde
    global velocidadeTremRoxo
    global velocidadeTremAmarelo
    global velocidadeTremAzul
    global verde
    global amarelo
    global roxo
    global azul

    if(trem == verde):
        if(velocidadeTremVerde <= 0.1):
            velocidadeTremVerde = 0.1
        else:
            velocidadeTremVerde -= 0.1
    elif (trem == amarelo):
        if(velocidadeTremAmarelo <= 0.1):
            velocidadeTremAmarelo = 0.1
        else:
            velocidadeTremAmarelo -= 0.1
    elif (trem == roxo):
        if(velocidadeTremRoxo <= 0.1):
            velocidadeTremRoxo = 0.1
        else:
            velocidadeTremRoxo -= 0.1
    elif (trem == azul):
        if(velocidadeTremAzul <= 0.1):
            velocidadeTremAzul = 0.1
        else:
            velocidadeTremAzul -= 0.1
    else:
        print("cor inválida!")

#Funcao que diminui a velocidade que sera utilizado como parametro na funcao time.sleep(velocidadeTremCor)
def diminuirVelocidade(trem):
    global velocidadeTremVerde
    global velocidadeTremRoxo
    global velocidadeTremAmarelo
    global velocidadeTremAzul
    global verde
    global amarelo
    global roxo
    global azul

    if(trem == verde):
        if(velocidadeTremVerde >= 2):
            velocidadeTremVerde = 2
        else:
            velocidadeTremVerde += 0.1
    elif (trem == amarelo):
        if(velocidadeTremAmarelo >= 2):
            velocidadeTremAmarelo = 2
        else:
            velocidadeTremAmarelo += 0.1
    elif (trem == roxo):
        if(velocidadeTremRoxo >= 2):
            velocidadeTremRoxo = 2
        else:
            velocidadeTremRoxo += 0.1
    elif (trem == azul):
        if(velocidadeTremAzul >= 2):
            velocidadeTremAzul = 2
        else:
            velocidadeTremAzul += 0.1
    else:
        print("cor inválida!")


def trilhoVerde(window, canvas):
    
    global velocidadeTremVerde
    global L1 
    global L2
    global L3 
    global L4 
    global mutexL2L8

    tremVerde = canvas.create_rectangle(10, 10, 30, 30, fill="green")

    while(1):
        if(L1<10):
            canvas.move(tremVerde, 10, 0)   
            L1 = L1+1
            L2 =0
        else:
            if (L2 < 10):
                if(L2 == 0):
                    sem1.acquire()
                    mutexL2L8.acquire()
                canvas.move(tremVerde, 0, 10) 
                L2=L2+1
            else:
                if(L2 == 10):
                    mutexL2L8.release()
                    sem1.release()
                    L2=L2+1
                if (L3 < 10):
                    if(L2 == 11):
                        mutexL3L13.acquire()
                        L2 = L2 +1
                    canvas.move(tremVerde, -10, 0) 
                    L3=L3+1 
                else:
                    if(L3 == 10):
                        mutexL3L13.release()
                        L3 = L3 +1
                    if (L4 < 10):
                        canvas.move(tremVerde, 0, -10) 
                        L4=L4+1
                    else:
                        L1=0
                        L2=0
                        L3=0
                        L4=0
        time.sleep(velocidadeTremVerde)

def trilhoRoxo(window, canvas):
    global L5
    global L6
    global L7
    global L8
    global velocidadeTremRoxo
    global mutexL2L8
    global mutexL6L12

    TremRoxo = canvas.create_rectangle(140, 10, 160, 30, fill="purple")

    while(1):
        if(L5<10):
            canvas.move(TremRoxo, 10, 0)   
            L5 = L5+1
        else:
            if(L5 == 10):
                sem2.acquire()
                mutexL6L12.acquire()
                L5 = L5 +1
            if (L6 < 10):
                canvas.move(TremRoxo, 0, 10) 
                L6=L6+1
            else:
                if(L6 == 10):
                    mutexL6L12.release()
                    sem2.release()
                    L6 = L6 +1
                if(L7 < 10):
                    if(L7 == 0):
                        sem1.acquire()
                        mutexL7L14.acquire()
                    canvas.move(TremRoxo, -10, 0) 
                    L7=L7+1
                    L8 = 0
                else:
                    if(L8<10):
                        if(L8 == 0):
                            mutexL2L8.acquire()
                            mutexL7L14.release()
                            sem1.release()
                        canvas.move(TremRoxo, 0, -10) 
                        L8=L8+1
                    else:
                        if(L8 == 10):
                            mutexL2L8.release()
                            L8=L8+1
                        L5=0
                        L6=0
                        L7=0
                        L8=0
        time.sleep(velocidadeTremRoxo)
       
def trilhoAmarelo(window, canvas):
    global L9
    global L10
    global L11
    global L12
    global mutexL6L12
    global velocidadeTremAmarelo

    TremAmarelo = canvas.create_rectangle(270, 10, 290, 30, fill="yellow")

    while(1):
        if(L9<10):
            canvas.move(TremAmarelo, 10, 0)   
            L9 = L9+1
        elif (L10 < 10):
            canvas.move(TremAmarelo, 0, 10) 
            L10=L10+1
        elif (L11 < 10):
            if(L11 == 0):
                sem2.acquire()
                mutexL11L15.acquire()
            canvas.move(TremAmarelo, -10, 0) 
            L11=L11+1
        elif (L12< 10):
            if(L11 == 10):
                mutexL6L12.acquire()
                mutexL11L15.release()
                sem2.release()
                L11 = L11+1
            canvas.move(TremAmarelo, 0, -10) 
            L12=L12+1
        else:
            if(L12 == 10):
                mutexL6L12.release()
                L12 = L12 + 1
            L9=0
            L10=0
            L11=0
            L12=0
        time.sleep(velocidadeTremAmarelo)
    

def trilhoAzul(window, canvas):
    global L13
    global L14
    global L15
    global L16
    global L17
    global L18
    global velocidadeTremAzul

    TremAzul = canvas.create_rectangle(10, 140, 30, 160, fill="blue")

    while(1):
        if(L13<12):
            if(L13 == 0):
                sem1.acquire()
                mutexL3L13.acquire()
            canvas.move(TremAzul, 10, 0)   
            L13 = L13+1
        else:
            if(L13==12):
                mutexL3L13.release()
                sem1.release()
                L14=13
                L13=L13+1
            if(L14 > 12 and L14 < 24):
                if(L14 == 13):
                    sem2.acquire()
                    mutexL7L14.acquire()
                canvas.move(TremAzul, 10, 0) 
                L14=L14+1
            else:
                if(L14==24):
                    mutexL7L14.release()
                    sem2.release()
                    L15=25
                    L14=L14+1
                if(L15>24 and L15<38):
                    if(L15 == 25):
                        mutexL11L15.acquire()
                    canvas.move(TremAzul, 10, 0) 
                    L15=L15+1
                    L16=0
                else:
                    if(L16 == 0):
                        mutexL11L15.release()
                    if(L16<10):
                        canvas.move(TremAzul, 0, 10) 
                        L16=L16+1
                        L17=0
                    else:
                        if(L17<36):
                            canvas.move(TremAzul, -10, 0) 
                            L17=L17+1
                        else:
                            if(L18<10):
                                canvas.move(TremAzul, 0, -10)
                                L18=L18+1
                            else:
                                L13=0 
                                L14=0
                                L15=0
                                L16=0
                                L17=0
                                L18=0        
        time.sleep(velocidadeTremAzul)
   

#criando e inicializando os mutex
mutexL2L8 = threading.Lock()
mutexL6L12 = threading.Lock()
mutexL3L13 = threading.Lock()
mutexL7L14 = threading.Lock()
mutexL11L15 = threading.Lock()

#criando e inicializando semaforos
sem1 = threading.Semaphore(2) #cruzamento do primeiro conjunto de trilhos (L2, L7 e 13)
sem2 = threading.Semaphore(2) #cruzamento do segundo conjunto de trilhos (L6, L11 e L14)

# variaveis que identificam qual o trem atraves de um valor int para serem utilizadas a ex: command=lambda: aumentarVelocidade(azul)
verde = 1 
roxo = 2
amarelo = 3
azul = 4

#variaveis que representam os trilhos laterais de cada trem
L1 = 0
L2 = 0
L3 = 0
L4 = 0
L5 = 0
L6 = 0
L7 = 0
L8 = 0
L9 = 0
L10 =0
L11 =0
L12 =0
L13 =0
L14 =0
L15 =0
L16 =0
L17 =0
L18 =0

#variaveis que controlam a velocidade dos trens
velocidadeTremVerde = 1
velocidadeTremRoxo = 1
velocidadeTremAmarelo = 1
velocidadeTremAzul = 1


window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()

#criação das threads
t1 = threading.Thread(target=visualizarPosicaoDosTrens, args=[window] )
t2 = threading.Thread(target=trilhoVerde, args=[window, canvas] )
t3 = threading.Thread(target=trilhoRoxo, args=[window, canvas] )
t4 = threading.Thread(target=trilhoAmarelo, args=[window, canvas] )
t5 = threading.Thread(target=trilhoAzul, args=[window, canvas] )
t6 = threading.Thread(target=painelDeControle, args=[window] )

# inicia as threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

window.mainloop()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()