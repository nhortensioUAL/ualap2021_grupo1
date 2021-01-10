from PIL import Image


def ler_imagem(ficheiro):
    with Image.open(ficheiro) as im:
        imagem = list(im.getdata())
    return imagem


def escrever_imagem(ficheiro, ficheiro_mono, imagem_mono):
    with Image.open(ficheiro) as im:
        mode = im.mode
        size = im.size
    with Image.new(mode, size) as im:
        im.putdata(imagem_mono)
        im.save(ficheiro_mono)
