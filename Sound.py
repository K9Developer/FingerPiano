import time
import cv2
import rtmidi
import FingerCounterModule

# Sets up the video, finger counter, and the MIDI port
cap = cv2.VideoCapture(0)
fingerM = FingerCounterModule.fingerCounter()
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

# Sets up ginger toggle vars
f1_toggle = False
f2_toggle = False
f3_toggle = False
f4_toggle = False
f5_toggle = False


while True:

    # Counts the fingers that are in the image
    success, img = cap.read()
    fingers, image = fingerM.getFingerCount(img=img)

    # If theres no hand in the picture it sets every finger to the value of 2 to avoid errors
    if fingers == []:
        fingers = [2,2,2,2,2]

    # Checks if the finger is closed
    if fingers[0] == 0:

        # If the toggle is false it will play a note
        if f1_toggle == False:
            f1_toggle = True
            midiout.send_message([0x90, 60, 127])
            for i in range(600):
                if fingers[0] == 1:
                    time.sleep(0.01)
                else:
                    break

    # If the finger is open it will reset the toggle
    else:
        f1_toggle = False

    # Checks if the finger is closed
    if fingers[1] == 0:

        # If the toggle is false it will play a note
        if f2_toggle == False:
            f2_toggle = True
            midiout.send_message([0x91, 62, 127])
            for i in range(600):
                if fingers[1] == 1:
                    time.sleep(0.01)
                else:
                    break

    # If the finger is open it will reset the toggle
    else:
        f2_toggle = False

    # Checks if the finger is closed
    if fingers[2] == 0:

        # If the toggle is false it will play a note
        if f3_toggle == False:
            f3_toggle = True
            midiout.send_message([0x92, 64, 127])
            for i in range(600):
                if fingers[2] == 1:
                    time.sleep(0.01)
                else:
                    break

    # If the finger is open it will reset the toggle
    else:
        f3_toggle = False

    # Checks if the finger is closed
    if fingers[3] == 0:

        # If the finger is open it will reset the toggle
        if f4_toggle == False:
            f4_toggle = True
            midiout.send_message([0x93, 65, 127])
            for i in range(600):
                if fingers[3] == 1:
                    time.sleep(0.01)
                else:
                    break

    # If the finger is open it will reset the toggle
    else:
        f4_toggle = False

    # Checks if the finger is closed
    if fingers[4] == 0:

        # If the finger is open it will reset the toggle
        if f5_toggle == False:
            f5_toggle = True
            midiout.send_message([0x93, 67, 127])
            for i in range(600):
                if fingers[4] == 1:
                    time.sleep(0.01)
                else:
                    break

    # If the finger is open it will reset the toggle
    else:
        f5_toggle = False



    # Shows the image
    image = cv2.flip(image, 1)
    cv2.imshow("Image", image)
    cv2.waitKey(1)

