import tkinter as tk
from tkinter import ttk
import threading
from playsound import playsound
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Contador do Davy Jones")
root.configure(bg="#222831")

abas = ttk.Notebook(root)
abas.pack(fill="both", expand=True)

aba_contador = tk.Frame(abas, bg="#222831")
aba_perolas =  tk.Frame(abas, bg="#222831")

abas.add(aba_contador, text="Contador")
abas.add(aba_perolas, text="Perolas do Dava")

animacao_id = None

def trocar_gif_aba(event):
    global animacao_id
    if animacao_id is not None:
        label_gif.after_cancel(animacao_id)
    aba = abas.index("current")
    if aba == 0:
        animar_gif(frames_contador)
    else:
        animar_gif(frames_perolas)

abas.bind("<<NotebookTabChanged>>", trocar_gif_aba)
gif_contador = Image.open(r"C:/Users/caue2/Desktop/vs code/dava.gif")
frames_contador = []
try:
    while True:
       frames_contador.append(ImageTk.PhotoImage(gif_contador.copy()))
       gif_contador.seek(len(frames_contador))
except EOFError:
    pass

gif_perolas = Image.open(r"C:/Users/caue2/Desktop/vs code/dava2.gif")
frames_perolas = []
try:
    while True:
       frames_perolas.append(ImageTk.PhotoImage(gif_perolas.copy()))
       gif_perolas.seek(len(frames_perolas))
except EOFError:
    pass

label_gif = tk.Label(root, bg="#222831")
label_gif.pack(pady=10)

def animar_gif(frames, indice=0):
    global animacao_id
    frame = frames[indice]
    label_gif.configure(image=frame)
    indice = (indice + 1) % len(frames)
    animacao_id = label_gif.after(100, animar_gif, frames, indice) 

animar_gif(frames_contador)

contador = 0
label = tk.Label(root, text=f"Contador: {contador}", font=("Arial", 16), fg="#FFD369", bg="#222831")
label.pack(pady=10)

def tocar_som():
    caminho = r"C:/Users/caue2/Desktop/vs code/sherba.mp3"
    if os.path.exists(caminho):
        threading.Thread(target=playsound, args=(caminho,), daemon=True).start()
    else:
        print(f"Arquivo de som não encontrado: {caminho}")

def tocar_som_2():
    caminho = r"C:/Users/caue2/Desktop/vs code/alien.mp3"
    if os.path.exists(caminho):
        threading.Thread(target=playsound, args=(caminho,), daemon=True).start()
    else:
        print(f"Arquivo de som nao encontrado: {caminho}")

def tocar_som_3():
    caminho = r"C:/Users/caue2/Desktop/vs code/adoro.mp3"
    if os.path.exists(caminho):
        threading.Thread(target=playsound, args=(caminho,), daemon=True).start()
    else:
        print(f"Arquivo de som nao encontrado: {caminho}")

def tocar_som_4():
    caminho = r"C:/Users/caue2/Desktop/vs code/todos os pals.mp3"
    if os.path.exists(caminho):
        threading.Thread(target=playsound, args=(caminho,), daemon=True).start()
    else:
        print(f"Arquivo de som nao encontrado: {caminho}")

def tocar_som_5():
    caminho = r"C:/Users/caue2/Desktop/vs code/zerei.mp3"
    if os.path.exists(caminho):
        threading.Thread(target=playsound, args=(caminho,), daemon=True).start()
    else:
        print(f"Arquivo de som nao encontrado: {caminho}")


def atualizar_label():
    label.config(text=f"Contador: {contador}")

def aumentar():
    global contador
    contador += 1
    atualizar_label()
    tocar_som()

def diminuir():
    global contador
    contador -= 1
    atualizar_label()
    tocar_som()

def resetar():
    global contador
    contador = 0
    atualizar_label()
    tocar_som()

def duplicar():
    global contador
    contador *= 2
    atualizar_label()
    tocar_som()

def tocar():
    global aba_perolas
    atualizar_label()
    tocar_som_2()

def tocar2():
    global aba_perolas
    atualizar_label()
    tocar_som_3()

def tocar3():
    global aba_perolas
    atualizar_label()
    tocar_som_4()

def tocar4():
    global aba_perolas
    atualizar_label()
    tocar_som_5()




btn_aumentar = tk.Button(aba_contador, text="Aumentar", command=aumentar, width=10, bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", bd=0)
btn_aumentar.pack(pady=2)
btn_diminuir = tk.Button(aba_contador, text="Diminuir", command=diminuir, width=10, bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", bd=0)
btn_diminuir.pack(pady=2)
btn_resetar = tk.Button(aba_contador, text="Resetar", command=resetar, width=10, bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", bd=0)
btn_resetar.pack(pady=2)
btn_duplicar = tk.Button(aba_contador, text="Duplicar", command=duplicar, width=10, bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", bd=0)
btn_duplicar.pack(pady=2)
btn_tocar = tk.Button(aba_perolas, text="Alien do Dava", command=tocar, width=10, bg="#00ADB5", fg="white", activebackground="#00CED1", activeforeground="#222831", bd=0)
btn_tocar.pack(pady=2)
btn_tocar = tk.Button(aba_perolas, text="Adoro", command=tocar2, width=10, bg="#00ADB5", fg="white", activebackground="#00CED1", activeforeground="#222831", bd=0)
btn_tocar.pack(pady=2)
btn_tocar = tk.Button(aba_perolas, text="Todos os pals", command=tocar3, width=10, bg="#00ADB5", fg="white", activebackground="#00CED1", activeforeground="#222831", bd=0)
btn_tocar.pack(pady=2)
btn_tocar = tk.Button(aba_perolas, text="Zerei todos", command=tocar4, width=10, bg="#00ADB5", fg="white", activebackground="#00CED1", activeforeground="#222831", bd=0)
btn_tocar.pack(pady=2)

root.mainloop()


