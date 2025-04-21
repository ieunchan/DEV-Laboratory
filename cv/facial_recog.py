import cv2, datetime

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 8)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow("Simple CCTV", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    if len(faces) > 0:
        cv2.imwrite("face_detected.jpg", frame)
        current_time = datetime.datetime.now().strftime("%H시:%M분:%S초")
        print(f"얼굴 감지됨 : {current_time}")
cap.release()
cv2.destroyAllWindows()