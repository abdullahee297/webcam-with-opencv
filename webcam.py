import cv2


def camera():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Webcam code")
    
    if not cam.isOpened():
        print("Camera not detected")
        
    print("Camera is opened Successfully")
    
    while True:
        ret, frame = cam.read()
        
        if not ret:
            print("Warning, can't recieve frame")
            break
            
        cv2.imshow("Webcom", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
if __name__ == "__main__":
    camera()
