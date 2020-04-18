import cv2
import numpy as np
import glob
import os

def getmatches(img_path,logos_path):
    """
       it extract features of logos and images and determine the number of the matching features
     Args:
         img_path:path of screenshot image
         logos_path:path of folder which contain logos

     returns:
            length(list):list contain the number of matches of each logo

    """

    img1 = cv2.imread(img_path)
    length = []


    data_path = os.path.join(logos_path, '*g')
    files = glob.glob(data_path)
    logos = []
    for f1 in files:
        img = cv2.imread(f1)
        logos.append(img)


    for i in logos:
        leng = 0

        #perform SIFT feature detection and description
        sift = cv2.xfeatures2d_SIFT.create()
        kp0, des0 = sift.detectAndCompute(i, None)
        kp1, des1 = sift.detectAndCompute(img1, None)

        #Define FLANN-based matching parameters
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)

        # Define FLANN-based matching
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des0, des1, k=2)

        #prepare empty mask to draw good matches
        mask_matches = [[0, 0] for i in range(len(matches))]

        for i, (m,n) in enumerate (matches):
                if m.distance<0.7*n.distance:
                    mask_matches[i]=[1,0]
                    leng+=1
        length.append(leng)
    return length

def logo_detection(length):
    """
      it detect the application

        Args:
            length(list):number of matches of each logo to the image
        returns:
            dict(dictionary)
    """
    ind = np.argmax(length)
    dict = {'Egybest': 0, 'facebook': 0, 'Google': 0}
    if ind == 0:
        dict['Egybest'] = 1
    elif ind == 1:
        dict['facebook'] = 1
    else:
        dict['Google'] = 1
    return dict

length=getmatches('Shot1.png','../images/logos')
print(logo_detection(length))