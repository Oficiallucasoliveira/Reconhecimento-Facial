import cv2


image_path = cv2.VideoCapture('http://192.168.1.2:4747/mjpegfeed?640x480') # imagem

cascade_path = 'haarcascade_frontalface_default.xml' # arquivo de cascade

clf = cv2.CascadeClassifier(cascade_path) #cria o classificador

img = cv2.imread(image_path) #ler a imagem

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte a img para cinza

faces = clf.detectMultiScale(gray, 1.3, 10)

for (x, y, w, h) in faces: #percorrer faces do rosto
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), )

	cv2.imshow('facial detection', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()