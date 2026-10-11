import cv2

# Reading Image

img = cv2.imread("resources/lena.png")
print(img.shape)
cv2.imshow("output", img)
cv2.waitKey(0)

# Reading Vidios

cap = cv2.VideoCapture("resources/elon.mp4")

while True:
    succes, img = cap.read()
    print(img.shape)
    cv2.imshow("output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# reading webcam


cap = cv2.VideoCapture(0)

cap.set(3, 640) # set width
cap.set(4, 480) # set height

while True:
    succes, img = cap.read()
    print(img.shape)
    cv2.imshow("output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
