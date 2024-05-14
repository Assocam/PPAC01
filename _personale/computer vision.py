import cv2
import datetime
import mediapipe as mp
mp_hands=mp.solutions.hands  #motore preaddestrato per riconoscere le mani
hands=mp_hands.Hands(static_image_mode=False, 
                     max_num_hands=2,
                     min_detection_confidence=0.5,
                     min_tracking_confidence=0.5 )


webcam=cv2.VideoCapture(0) #apre la prima webcom del nostro computer (nel nostro caso il pc ha solo una webcam) 
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True: 
    ret, frame= webcam.read()  #ret=T significa "riuscito", =F significa "non riuscito". Frame è il fotogramma letto
    if ret:

        frame_rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #converte il frame da bgr a rgb perchè hands vuole così.
        results= mp_hands.process(frame_rgb)  #processa il fotogramma tramite il motore mp_hands
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmark: #per ogni mano
                for id, landmark in enumerate(hand_landmark.landmark): #per ogni falange
                    x,y=int(landmark.x*frame.shape[1]), int(landmark.y*frame.shape[0]) # ricava coordinate assolute a partire da quelle relative
                    cv2.circle(frame, (x,y),5,(0,255,0),-1) 
                    
                    if id in (4,8,12):  # 4 è identificativo della punta del pollice (8 è indice, 12 è medio)
                        xp,yp=int(landmark.x*frame.shape[1]),int(landmark.y*frame.shape[0]) #coordinate del pollice
                        cv2.circle(frame, (xp,yp), 15, (32,255,128), -1) 

                    frame.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS) # disegna le linee di congiunzione tra le falangi
                    #print(landmark)  #stampa le coordinate posizionali di tutte le falangi
                    
        cv2.putText(frame, str(datetime.datetime.now()), (10,15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
        #parametri(nome immagine, cosa scrivere, posizione, font, dimensione in pixel, colore rgb, spessore)       
        
        cv2.imshow("Immagini", frame)  #mostra il fotogramma

        
        if cv2.waitKey(1)==27:  #waitkey aspetta che premiamo il tasto indicato dopo l'uguale per uscire dal ciclo infinito. 
            #Possiamo scegliere il tasto ESC che è 27    
            break

webcam.release()
cv2.destroyAlllWindows()