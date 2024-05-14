import cv2
webcam=cv2.VideoCapture(0) #apre la prima webcom del nostro computer (nel nostro caso il pc ha solo una webcam) 

while True: 
    ret, frame= webcam.read()  #ret=1 significa "riuscito", =0 significa "non riuscito". Frame è il fotogramma letto
    cv2.imshow("Immagini", frame)  #mostra il fotogramma