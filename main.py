import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pyautogui 

cap = cv2.VideoCapture(0)
cap.set(3, 700)  # Width
cap.set(4, 1000)   # Height

detector = HandDetector(detectionCon=0.8, maxHands=2)
prevX, prevY = 0, 0  



movement = "" 
while True:
    success, img = cap.read()

    
    if not success or img is None or not isinstance(img, np.ndarray):
        print("Invalid image ...")
        continue

    print("Image shape:", img.shape)

    try:
        # Detect hands
        hands, img = detector.findHands(img)
        print("Hands detected:", len(hands) if hands else 0)

        if hands:
            hand = hands[0]

            cx, cy = hand['center']
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

            if prevX != 0 and prevY != 0:
                dx = cx - prevX
                dy = cy - prevY

                # Check horizontal 
                if abs(dx) > abs(dy):
                    if dx > 40:
                        print("Swipe Right")
                        
                        pyautogui.press('left')
                        movement = "RIGHT"
                    elif dx < -40:
                        print("Swipe Left")
                        
                        pyautogui.press('right')
                        movement = "LEFT"

                # Check vertical 
                else:
                    if dy < -40:
                        print("Swipe Up")
                        pyautogui.press('up')
                        movement = "UP"

                    elif dy > 40:
                        print("Swipe Down")
                        pyautogui.press('down')
                        movement = "DOWN"


            # Update
            prevX, prevY = cx, cy
        
        else:
            # Reset
            prevX, prevY = 0, 0

    except Exception as e:
        print("Error in detecting hands:", e)
        continue

    if movement != "":
        cv2.putText(img, movement, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
    
    cv2.imshow("Hand Tracking", img)

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
