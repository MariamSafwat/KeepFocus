import cv2
import numpy as np
import glob
import os


def getmatches(img_path, progImgs):
    """
       it extract features of logos and images and determine the number of the matching features
     Args:
         img_path:path of screenshot image
         progImgs:Dictionary of programs

     returns:
            progs(Dictionary):dictionary contain the number of matches of each program

    """

    img1 = cv2.imread(img_path)

    progs = {}

    for key in progImgs:
        oneprog = progImgs[key]
        data_path = os.path.join(oneprog[3:], '*g')
        files = glob.glob(data_path)
        logos = []
        length = []
        for f1 in files:
            img = cv2.imread(f1)
            logos.append(img)

        for i in logos:
            leng = 0

            # perform SIFT feature detection and description
            sift = cv2.xfeatures2d_pipSIFT.create()
            kp0, des0 = sift.detectAndCompute(i, None)
            kp1, des1 = sift.detectAndCompute(img1, None)

            # Define FLANN-based matching parameters
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            # Define FLANN-based matching
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(des0, des1, k=2)

            # prepare empty mask to draw good matches
            mask_matches = [[0, 0] for i in range(len(matches))]
            for i, (m, n) in enumerate(matches):
                if m.distance < 0.7 * n.distance:
                    mask_matches[i] = [1, 0]
                    leng += 1
            length.append(leng)
        progs[key] = np.max(length)

    return progs

# length=getmatches('../images/Shot1.png','../images/Google')
