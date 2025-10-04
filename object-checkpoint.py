from ultralytics import YOLO
import cv2
# Загружаем предобученную модель (можно указать свою .pt модель на змеях)
model = YOLO("yolov8n.pt")  # замените на вашу snake-модель
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)  # прогоняем через YOLO
    annotated_frame = results[0].plot()  # рисуем боксы
    cv2.imshow("Snake Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break
cap.release()
cv2.destroyAllWindows()