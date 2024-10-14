from PIL import Image
import pytesseract

# Cargar la imagen
imagen = Image.open('/mnt/c/Users/soporte/Downloads/licencia.png')

# Convertir la imagen a texto
texto = pytesseract.image_to_string(imagen)

print(texto)