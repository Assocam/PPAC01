import cv2
#webcam=cv2.VideoCapture(0) #apre la prima webcom del nostro computer (nel nostro caso il pc ha solo una webcam) 
webcam.set(cv2.CAP_PROP_FRAME_WIDTH)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH)

#while True: 
    #ret, frame= webcam.read()  #ret=1 significa "riuscito", =0 significa "non riuscito". Frame è il fotogramma letto
    #cv2.imshow("Immagini", frame)  #mostra il fotogramma
    if cv2.waitKey(1)==27:
        break

webcam.realase()
cv2.destroyAlllWindows()