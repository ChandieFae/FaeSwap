# utils/align_faces.py
import cv2
import dlib
import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

def align_face(image_path, output_path="aligned_face.jpg"):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if not faces:
        raise ValueError("No face detected.")

    for face in faces:
        landmarks = predictor(gray, face)
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        aligned = image[y:y+h, x:x+w]
        cv2.imwrite(output_path, aligned)
        return output_path

    return None
  
 You'll need the shape_predictor_68_face_landmarks.dat from the dlib model zoo.
