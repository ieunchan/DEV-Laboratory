import cv2

cap = cv2.VideoCapture(0)  # 0번 카메라

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam Feed", frame)  # 컬러 화면 출력

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()