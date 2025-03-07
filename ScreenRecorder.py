import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"MJPG") #MJPG is compatible with my mac.
filename = "Recording.avi"
fps = 30.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR) #RGBA2BGR is compatible with my mac.
    out.write(frame)
    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'): #Pressing q quits the program.
        break

out.release()
cv2.destroyAllWindows()