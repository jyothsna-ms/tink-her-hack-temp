import cv2
import mediapipe as mp
import numpy as np

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

# Finger color mapping
FINGER_COLORS = {
    4: (0,0,255),      # Thumb → Red
    8: (255,0,0),  # Index → White
    12: (0,0,0),       # Middle → Black
    16: (0,255,0),     # Ring → Green
    20: (255,255,255)      # Pinky → Blue
}

pen_color = (255,0,0)   # Default blue
selected_color = (255,0,0)

drawing_mode = False

cap = cv2.VideoCapture(0)

canvas = None
px, py = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:
            
            lm = hand_landmarks.landmark
            # =============================
            # Show colors on fingertips
            # =============================
            for tip_id, color in FINGER_COLORS.items():

                tip = lm[tip_id]

                x = int(tip.x * w)
                y = int(tip.y * h)

                cv2.circle(frame,(x,y),12,color,-1)
            # =============================
            # Gesture Detection
            # =============================
            fingers = []

            # Thumb
            fingers.append(lm[4].x < lm[3].x)

            # Other fingers
            fingers.append(lm[8].y < lm[6].y)
            fingers.append(lm[12].y < lm[10].y)
            fingers.append(lm[16].y < lm[14].y)
            fingers.append(lm[20].y < lm[18].y)

            fingers_up = sum(fingers)
            

            # =============================
            # Draw using Index Finger
            # =============================
            # Select color based on single finger gesture
            if fingers_up == 1:

                # Thumb
                if fingers[0]:
                    pen_color = (0,0,255)

                # Index
                elif fingers[1]:
                    pen_color = (255,0,0)

                # Middle
                elif fingers[2]:
                    pen_color = (0,0,0)

                # Ring
                elif fingers[3]:
                     pen_color = (0,255,0)

                # Pinky
                elif fingers[4]:
                        pen_color = (255,255,255)

                drawing_mode = True
            elif fingers_up == 2 or drawing_mode:

                tip = lm[8]

                x = int(tip.x * w)
                y = int(tip.y * h)

                cv2.circle(frame,(x,y),8,pen_color,-1)

                if px == 0 and py == 0:
                    px, py = x, y

                cv2.line(canvas,(px,py),(x,y),pen_color,5)

                px, py = x, y
            # =============================
            # Fist → Erase
            # =============================
            else:
              px, py = 0, 0
              drawing_mode = False 

        
           
    combined = cv2.addWeighted(frame,0.7,canvas,0.3,0)

    cv2.imshow("Finger Color Drawing Board", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()