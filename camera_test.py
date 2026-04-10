import cv2 

camera_ip = "https://10.58.43.127:8080/video"
cap = cv2.VideoCapture(camera_ip)
if not cap.isOpened():
    print("Error: Could not open stream.")
else:
    print("Stream opened successfully!")

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Camera feed", frame)
            if cv2.waitKey(0) == ord('q'):
                break
        else:
            print("Error: Could not read the frame.")
            break
cap.release() 