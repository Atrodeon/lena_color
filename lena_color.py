from PIL import Image

# Abrir a imagem original (troque 'image.jpg' pelo nome do seu arquivo)
img = Image.open('lena_color.gif')

# Transformar em tons de cinza
gray_img = img.convert('L')
gray_img.save('image_gray.gif')  # Salva a imagem cinza

# Binarizar (preto e branco)
threshold = 128  # Valor para separar preto/branco
binary_img = gray_img.point(lambda x: 255 if x > threshold else 0, mode='1')
binary_img.save('image_binary.gif')  # Salva imagem binária

print('Pronto! As novas imagens foram criadas: image_gray.gif e image_binary.gif')