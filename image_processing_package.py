# image_processing_package.py
from PIL import Image, ImageFilter
import os

def load_image(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def to_grayscale(image):
    return image.convert("L")

def resize_image(image, size):
    return image.resize(size)

def blur_image(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))

if __name__ == "__main__":
    input_path = "exemplo.jpg"
    output_path = "saida_processada.jpg"

    try:
        img = load_image(input_path)
        gray = to_grayscale(img)
        resized = resize_image(gray, (200, 200))
        blurred = blur_image(resized, radius=3)
        save_image(blurred, output_path)
        print(f"Imagem processada salva em: {output_path}")
    except Exception as e:
        print("Erro ao processar imagem:", e)
