import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

categorias = {
    "Imagens":     [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos":  [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos":      [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":       [".mp3", ".wav", ".ogg", ".flac"],
    "Codigo":      [".py", ".js", ".html", ".css"],
    "Programas":   [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".gz"],
}

pasta_escolhida = ""

def escolher_pasta():
    global pasta_escolhida
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_escolhida = pasta
        label_pasta.config(text=pasta)

def organizar():
    if pasta_escolhida == "":
        messagebox.showwarning("Aviso", "Escolha uma pasta primeiro!")
        return

    arquivos = os.listdir(pasta_escolhida)

    for nome_arquivo in arquivos:
        caminho_completo = os.path.join(pasta_escolhida, nome_arquivo)

        if os.path.isdir(caminho_completo):
            continue

        if nome_arquivo == "organizador.py" or nome_arquivo == "organizador.exe":
            continue

        extensao = os.path.splitext(nome_arquivo)[1].lower()

        categoria_encontrada = "Outros"

        for categoria, extensoes in categorias.items():
            if extensao in extensoes:
                categoria_encontrada = categoria
                break

        pasta_destino = os.path.join(pasta_escolhida, categoria_encontrada)

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        shutil.move(caminho_completo, os.path.join(pasta_destino, nome_arquivo))

    messagebox.showinfo("Concluído", "Pasta organizada com sucesso!")

janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("500x200")
janela.resizable(False, False)

tk.Label(janela, text="Organizador de Arquivos", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(janela, text="Escolher Pasta", command=escolher_pasta, width=20).pack()

label_pasta = tk.Label(janela, text="Nenhuma pasta escolhida", fg="gray")
label_pasta.pack(pady=5)

tk.Button(janela, text="Organizar", command=organizar, width=20, bg="green", fg="white").pack(pady=10)

janela.mainloop()
