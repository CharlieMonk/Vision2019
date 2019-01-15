import numpy as np
import cv2
class FindObject:
    def init(dilate_, objName_):
        self.objName = objName_
        _, self.contours, _ = cv2.findContours(dilate_, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    def getAngle(point):
        # Use the center_point, fov, and width to find the heading (angle to target)
        field_of_view = 65
        pixel_distance = point - frame_width/2
        heading = ((field_of_view/2.0) * pixel_distance)/(frame_width/2)
        print(pixel_distance)
        return int(heading)
    def findObject():
        # Only proceed if contours were found
        if(self.contours != None):
            if(len(contours) > 0):
                # Find the largest contour
                largest_area = 0
                cnt = 0
                for i in range(0, len(contours)):
                    area = cv2.contourArea(contours[i])
                    if(area > largest_area):
                        largest_area = area
                        cnt = contours[i]
                # If the object is cube, use red, if retroreflective, use blue
                if(objName == "cube"):
                    color = (0,0,255)
                elif(objName == "retroreflective"):
                    color = (255,0,0)
                # Extract boundary points of object
                left = tuple(cnt[cnt[:,:,0].argmin()][0])
                right = tuple(cnt[cnt[:,:,0].argmax()][0])
                top = tuple(cnt[cnt[:,:,1].argmin()][0])
                bottom = tuple(cnt[cnt[:,:,1].argmax()][0])

                # Find and print the width of the cube
                self.width = right[0]-left[0]
                # print(objName + ": " + str(width))
                # Use boundary points to find the top left and bottom right corners
                top_left = (left[0], top[1])
                bottom_right = (right[0], bottom[1])

                # Draw a rectangle bounding the object using top left and bottom right points
                cv2.rectangle(bgr_img, top_left, bottom_right, color, 3)
                # Find the center point of the object
                self.center_point = (int((top_left[0]+bottom_right[0])/2), int((top_left[1]+bottom_right[1])/2))

                # Draw circle at the center point
                cv2.circle(bgr_img, center_point, 5, color, -1)
                # Find the angle to the center point
                self.angle = self.getAngle(center_point)
                print(objName + ": " + str(angle))
                # If the program isn't in testing mode, send data to RoboRIO
                if(sendPackets):
                    sendData(angle, width, objName)
                # Show the images
                if(displayImages):
                    cv2.imshow("Mask Image", dilate)   # This should be enabled for debugging purposes ONLY!
                return hsv_img
