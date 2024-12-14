import numpy as np
import cv2
from time import sleep

VIDEO = "/Users/magnosouza/PycharmProjects/VisaoComputacional/deteccaoDeMovimento/videos/Rua.mp4"
delay = 10

cap = cv2.VideoCapture(VIDEO)
hasFrame, frame = cap.read()

framesIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []
for fid in framesIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    hasFrame, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
#print(medianFrame.shape)
#cv2.imshow('Median frame', medianFrame)
#cv2.waitKey(0)
cv2.imwrite('median_frame.jpg', medianFrame)

#---- Aula 2 transformando as cores em cinza

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Cinza', grayMedianFrame)
#cv2.waitKey(0)
cv2.imwrite('grayMedian_frame.jpg', grayMedianFrame)

# --- Lanço para realizar a alteração das cores dos frames em um loop até finalizar todos os frames analisados
while (True):
    #--- Trecho para reduzir a velocidade do video
    tempo = float(1 / delay)
    sleep(tempo)

    hasFrame, frame = cap.read()

    if not hasFrame:
        print("Nenhum frame foi encontrado.")
        break

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #--- Mascara de cores
    dframe = cv2.absdiff(frameGray, grayMedianFrame)
    th, dframe = cv2.threshold(dframe, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow('frame', dframe)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()