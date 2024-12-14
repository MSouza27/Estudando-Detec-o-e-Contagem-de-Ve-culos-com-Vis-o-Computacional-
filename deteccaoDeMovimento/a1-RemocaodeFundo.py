import numpy as np
import cv2

#VIDEO = "/Users/magnosouza/PycharmProjects/VisaoComputacional/deteccaoDeMovimento/videos/Rua.mp4"
VIDEO = "/Users/magnosouza/PycharmProjects/VisaoComputacional/deteccaoDeMovimento/videos/Arco.mp4"
cap = cv2.VideoCapture(VIDEO)
hasFrame, frame = cap.read()

framesIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []
for fid in framesIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    hasFrame, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
print(medianFrame.shape)
cv2.imshow('Median frame', medianFrame)
cv2.waitKey(0)
cv2.imwrite('median_frame.jpg', medianFrame)