import face_recognition
import cv2
import numpy as np

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

known_face_encodings =[
    [-0.11737007,0.09398738,0.08061674,-0.10376798,-0.06242224,-0.03534065,0.06116991,0.061529,0.13080612,-0.01502033,0.18686752,-0.05197452,-0.21744959,0.00817739,-0.01787218,0.11963195,-0.14015152,-0.05588456,-0.13729185,-0.10075728,0.10297147,0.01787619,-0.10708677,0.08344228,-0.16513251,-0.25169775,-0.00699815,-0.04273918,0.01923096,-0.10537145,0.06843796,0.02571003,-0.15480986,-0.04479665,0.00739286,0.10459743,0.02531855,-0.09611222,0.15817514,0.03681623,-0.12100871,0.11894009,0.07790545,0.30624425,0.12329871,0.07721074,0.04747076,-0.03353719,0.22186558,-0.30069768,0.08006005,0.07810674,0.11799125,0.04996569,0.11516438,-0.17053509,0.03357625,0.14552933,-0.24187011,0.08743379,0.04359606,-0.02158156,-0.01044436,-0.12603275,0.13412647,0.0678445,-0.12404589,-0.06957103,0.12890793,-0.10002488,-0.00428964,0.06896459,-0.07125992,-0.11113932,-0.24024694,0.15950969,0.43229899,0.17546491,-0.1430701,-0.00985174,-0.09802588,0.00310345,0.05062109,-0.02711225,-0.08389975,-0.08125073,-0.09062928,0.07748556,0.20963944,0.03651736,-0.0093345,0.18395339,0.06864394,-0.05337671,-0.07739259,-0.00987546,-0.1825269,0.02881331,-0.04801668,0.01176142,0.05959442,-0.10388655,0.02502168,0.07329396,-0.26986095,0.1460602,-0.01050322,-0.04378461,-0.01331311,0.09471048,-0.14307338,0.04238858,0.11869317,-0.26470304,0.15966038,0.16898561,0.03550394,0.10609386,0.06036742,0.03707332,0.04496833,0.00278265,-0.10065699,-0.11472514,0.07076274,0.00045766,0.08409072,0.04318789]
    ]
known_face_names = ['Younis']
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    small_frame = frame

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = face_encoding

            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # best_match_index = np.argmin(face_distances)
            # if matches[best_match_index]:
            #     name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        face_distance_const = 1.0 
        width_px_const = 75


        font = cv2.FONT_HERSHEY_DUPLEX
        width = right - left
        height = abs(top - bottom)
        avg = (width+height)/2
        distance = (-0.0217*width + 2.6275)
        print(distance,avg,height,width,left,top,right,bottom)
        print(name)
        cv2.putText(frame, str(distance), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
