#导入所需库文件
import cv2
import numpy as np

def mathc_img(image,Target):
    value = 0.90
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
        ans = [pt, (pt[0] + w, pt[1] + h)]
        #print(ans)
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return ans;

mathc_img("test6.jpg",'test6_face.jpg')
# image = ("test5.jpg")
# Target = ('t41.jpg')
# mathc_img(image, Target)