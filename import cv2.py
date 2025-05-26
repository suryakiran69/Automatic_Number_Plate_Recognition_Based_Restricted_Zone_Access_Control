import cv2
import pytesseract
import serial as s
import time
arduino = s.Serial('COM5', 9600)
time.sleep(1)

# Configure tesseract path if required (for Windows users)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the frame
    text = pytesseract.image_to_string(gray, config='--psm 6')

    # Filter out only alphabets and numbers, ignoring spaces
    filtered_text = ''.join(filter(str.isalnum, text))

    # Display the filtered text on the frame
    cv2.putText(frame, filtered_text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the output frame
    cv2.imshow('Camera Feed - Alphabets and Numbers Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print ('value is '+filtered_text)
        try:
            arduino.write((filtered_text + '\n').encode())
        except:
            print('port not opened')
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows+
arduino.close()
cap.release()
cv2.destroyAllWindows()