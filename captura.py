import cv2
classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture('http://192.168.1.2:4747/mjpegfeed?640x480') #Captura A camera 
amostra = 1 
numeroamostras = 25 #numeros de fotos a ser tiradas 
id = input('Digite seu identificador: ') #pega o id do identificador ou senha numero da pessoa a ser cadastrada
largura, altura = 220, 220 # altura e largura do tamanho da foto
print ("Capturando as Faces...") # env msg 


while (True):
	conectado, imagem = camera.read()
	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5,minSize=(100,100))


	for (x, y, l, a) in facesDetectadas:
		cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
			cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + "+.jpg", imagemFace)
			print("[foto " + str(amostra) + "capturada com sucesso!]")
			amostra += 1

	cv2.imshow('Reconhecimento FACIL MR BONNANO', imagem)
	#cv2.waitKey(1)
	if (amostra >= numeroamostras + 1):
		break

print("Faces capturada com sucesso")		
camera.realease()
cv2.destroyAllWindows()