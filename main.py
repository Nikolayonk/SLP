import cv2
import os
from pyzbar.pyzbar import decode

RTSP_URL = 'rtsp://admin:admin@192.168.0.103:1935' # подключаемся к камере, получив данные с приложения Free Security Camera

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    _, frame = cap.read()
    cv2.imshow('RTSP stream', frame)

    # Попытка распознать QR-код на текущем кадре
    decoded_objects = decode(frame)

    # Обработка распознанных объектов
    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        print('QR Code Data:', qr_data)
        print('QR Code Type:', obj.type)
        print('QR Code Rectangle:', obj.rect)
        print('QR Code Polygon:', obj.polygon)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
