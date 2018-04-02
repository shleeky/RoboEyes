import face_recognition
import cv2


def facereco(img_path):

    known_image = face_recognition.load_image_file("downey.jpg")
    unknown_image = face_recognition.load_image_file(img_path)

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    message = 'unKnown'
    if results == [True]:
        message = 'Downey'
    else:
        known_image = face_recognition.load_image_file("andy.jpg")
        andy_encoding = face_recognition.face_encodings(known_image)[0]
        results = face_recognition.compare_faces([andy_encoding], unknown_encoding)
        if results == [True]:
            message = 'Andy'

    unknown_image = cv2.imread(img_path)
    small_image = cv2.resize(unknown_image, (0, 0), fx=0.25, fy=0.25)
    rgb_pic = small_image[:, :, ::-1]
    face_location = face_recognition.face_locations(rgb_pic)[0]
    # face_encoding = face_recognition.face_encodings(rgb_pic, face_location)[0]
    (top, right, bottom, left) = face_location
    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    top *= 4
    right *= 4
    bottom *= 4
    left *= 4

    # Draw a box around the face
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 0, 255), 2)

    # Draw a label with a name below the face
    cv2.rectangle(unknown_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(unknown_image, message, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imwrite(img_path, unknown_image)
    # cv2.imshow('Video', unknown_image)
    print(message)

    return message

if __name__ == '__main__':
    #res = facereco('upload_img.jpg')
    res = facereco('unlabel.jpg')
    print(res)

