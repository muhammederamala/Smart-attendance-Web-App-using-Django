import cv2
import os

# Set the path to the folder to save the captured image
save_folder = "C:/Users/muham/Music/3/mysite/python/captured"

# Create the save folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

import cv2

# initialize video capture object
cap = cv2.VideoCapture(0)

# create a window to display the video
cv2.namedWindow("Video")

# initialize variables
frame = None
key = -1

while key == -1:  # loop until a key is pressed


    # capture a frame from the video stream
    ret, frame = cap.read()

    # display the frame in the window
    cv2.imshow("Video", frame)

    
    # check if a key is pressed
    key = cv2.waitKey(1)

# release the video capture object
cap.release()

# Save the captured image to disk
save_path = os.path.join(save_folder, "captured_image.jpg")
cv2.imwrite(save_path, frame)

# Close the window
cv2.destroyAllWindows()







        # if request.method == 'POST':
        #     msg = request.POST.get('msg')
        #     if msg:
        #         save_path = os.path.join(save_folder, "captured_image.jpg")
        #         cv2.imwrite(save_path, frame)
        #         print(request.headers)
        #         return render(request,"account/captured.html",{})

