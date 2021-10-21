import cv2
import mediapipe as mp

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):

        # Set up vars and AI
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        # Converts the inputted img to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Gets the finger positions from the imgRGB
        self.results = self.hands.process(imgRGB)

        # Checks if theres a hand in the image if there is it will draw the points and lines of the hand
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNumber=0, draw = True):
        lmList = []

        # Gets the finger positions from the img
        self.results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Checks if theres a hand in the image
        if self.results.multi_hand_landmarks:

            # Gets the positions for the handNumber hand
            handLms = self.results.multi_hand_landmarks[handNumber]
            for id, lm in enumerate(handLms.landmark):

                # Converts positions to numpy positions
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

                # If draw is true it will draw the points and lines of the hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return (lmList, img)

def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()