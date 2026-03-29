import os
import shutil

categorias = {
    "Imagens":     [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos":  [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos":      [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":       [".mp3", ".wav", ".ogg", ".flac"],
    "Codigo":      [".py", ".js", ".html", ".css"],
    "Compactados": [".zip", ".rar", ".gz"],
}

pasta = input("Digite o caminho da pasta (Enter = pasta atual): ").strip()

if pasta == "":
    pasta = "."

arquivos = os.listdir(pasta)

for nome_arquivo in arquivos:
    caminho_completo = os.path.join(pasta, nome_arquivo)

    if os.path.isdir(caminho_completo):
        continue

    extensao = os.path.splitext(nome_arquivo)[1].lower()

    categoria_encontrada = "Outros"

    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            categoria_encontrada = categoria
            break

    pasta_destino = os.path.join(pasta, categoria_encontrada)

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    shutil.move(caminho_completo, os.path.join(pasta_destino, nome_arquivo))

    print(f"{nome_arquivo} movido para {categoria_encontrada}/")

print("Organização concluída!")
