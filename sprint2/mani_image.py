from PIL import Image
#Abrir imagen (inicializar)
imagen = Image.open('sunset.jpg')

#Cambiar tamaño
n_tam = (500,300)
n_imagen = imagen.resize(n_tam)

#Mostrara imagen
imagen.show()
n_imagen.show()

#Guardar
n_imagen.save('C:\\Users\\Romina\\Downloads\\nuevo-sunset.jpg')