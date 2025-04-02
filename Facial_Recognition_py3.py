import cv2
import numpy as np
import os
from pathlib import Path

curr_path = os.path.dirname(os.path.realpath(__file__))
print(curr_path)

directory_in_str = str(curr_path) + "\\Input"
output_directory = str(curr_path) + "\\Output"

# Create directories if they don't exist
os.makedirs(directory_in_str, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

all_faces = []

pathlist = Path(directory_in_str) 
for path in pathlist.iterdir():
    path_in_str = str(path)
    
    # Only process image files
    if not path_in_str.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        continue
        
    print(f"Processing image: {path_in_str}")
    
    # Load image
    image = cv2.imread(path_in_str)
    if image is None:
        print(f"Failed to load image: {path_in_str}")
        continue
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cascPath = str(curr_path) + "\\Haar_Cascades\\haarcascade_frontalface_default.xml"
    
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    # Detect faces in image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("Found " + str(len(faces)) + " faces.")

    count = 0

    for (x, y, w, h) in faces:

        w = max(w, h)
        h = max(w, h)

        count += 1
        
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 2)
        blank_image = np.zeros((h, w, 3), np.uint8)

        for i in range(0, w):
            for j in range(0, h):
                blank_image[j][i] = gray[y + j][x + i]
                
        face_resize = cv2.resize(blank_image, (48, 48), 3)

        all_faces.append(face_resize)


colour_list = []

output_file = open(output_directory + "\\output_file.txt", "w")
for i in range(0, len(all_faces)):

    file_string = ""

    for j in range(0, 48):
        for k in range(0, 48):
            file_string += str(all_faces[i][j][k][0]) + " "

    file_string = file_string.strip()

    output_file.write(file_string + "\n")
    
    cv2.imwrite(output_directory + "\\face_" + str(i) + ".jpg", all_faces[i])

cv2.waitKey(0)
