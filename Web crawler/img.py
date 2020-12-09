import io

import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image

import debuglog

record = debuglog.record_bug()


# r = requests.get("https://www.8newsnow.com/wp-content/uploads/sites/59/2020/10/Chauvin-14-1.jpg?w=1600&h=900&crop=1")
# https://www.ventanaws.org/uploads/6/7/1/3/67132355/screen-shot-2020-08-27-at-8-11-48-am_orig.png


class img_process():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        self.width = 0
        self.height = 0

    def down_img(self, url):
        try:
            r = requests.get(url, headers=self.headers)

            im = Image.open(io.BytesIO(r.content))
            return im
        except:
            record.recordlog()

    def check_img_dim(self, im):
        try:
            self.width, self.height = im.size
            if ((self.width / self.height) < 2.5 or (self.width / self.height) > 0.4):
                return True
            else:
                return False
        except:
            record.recordlog()
            return False

    def img_crop(self, im):
        min_pix = min(self.width, self.height)
        left = round((self.width - min_pix) / 2)
        top = round((self.height - min_pix) / 2)
        x_right = round(self.width - min_pix) - left
        x_bottom = round(self.height - min_pix) - top
        right = self.width - x_right
        bottom = self.height - x_bottom
        im = im.crop((left, top, right, bottom)).resize((100, 100))
        np_im = np.array(im)
        np_im = np_im.dumps()
        return np_im

    def show_img(self, np_image):

        plt.imshow(np_image)
        plt.show()

# x=img_process()
# img=x.down_img("https://gray-kktv-prod.cdn.arcpublishing.com/resizer/KyFzmhXM4Bkt-jikQQxATYcWTv4=/1200x675/smart/cloudfront-us-east-1.images.arcpublishing.com/gray/VJF3MQKCQBAT3MWJYSRR5A3ITE.jpg")
# if x.check_img_dim(img):
#    npimg=x.img_crop(img)
#    x.show_img(npimg)
# else:
#    x=np.array(0)
