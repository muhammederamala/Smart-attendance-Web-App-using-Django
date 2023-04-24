import face_recognition
import os
import cv2

# Load known faces
known_faces = []
known_names = []

tolerance = 0.5

# Replace this with the path to your folder of known faces
known_faces_folder = "C:/Users/muham/Music/3/mysite/account/static/account/media/known_images"

for file in os.listdir(known_faces_folder):
    image = face_recognition.load_image_file(os.path.join(known_faces_folder, file))
    face_encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(face_encoding)
    known_names.append(os.path.splitext(file)[0])

# Load unknown faces
unknown_faces_folder = "C:/Users/muham/Music/3/mysite/account/static/account/media/captured"

for file in os.listdir(unknown_faces_folder):
    image = face_recognition.load_image_file(os.path.join(unknown_faces_folder, file))
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Iterate over each face in the unknown image
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # See if the face is a match for the known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=tolerance)
        name = "Unknown"

        # If we have at least one match, use the first one
        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        # Draw a box around the face
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with the name below the face
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    # Show the final image
    
    save_folder = "C:/Users/muham/Music/3/mysite/account/static/account/media/processed"

    save_path = os.path.join(save_folder, "processed_image.jpg")
    cv2.imwrite(save_path, image)


    # cv2.imshow('Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
