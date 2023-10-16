from PIL import Image
from pyzbar.pyzbar import decode
import os

pasta = r"caminho_da_pasta"

# Lista de todos os arquivos JPG na pasta
arquivos_jpg = [arquivo for arquivo in os.listdir(pasta) if arquivo.lower().endswith('.jpg')]

for arquivo in arquivos_jpg:
    caminho_completo = os.path.join(pasta, arquivo)
    imagem = Image.open(caminho_completo)
    imagem = imagem.convert("L")

    codigos_barras = decode(imagem)

    if len(codigos_barras) > 0:
        codigo = codigos_barras[0].data.decode("utf-8")
        print(f"Código de barras identificado em {arquivo}: {codigo}")
    else:
        print(f"Nenhum código de barras identificado em {arquivo}")

