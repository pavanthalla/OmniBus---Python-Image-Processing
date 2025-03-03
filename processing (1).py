import cv2
def process(img_path):
    face_cascade = cv2.CascadeClassifier(r'C:\Users\pradyumna\Desktop\corona\haarcascade_frontalface_default.xml')
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return len(faces)