import cvlib as cv
import os
from PIL import Image
import glob


def bestface(image_same_name_list):
    pic1 = image_same_name_list[0]
    pic1.show()

    #print(image_same_name_list)


def main():
    print("Hello World!")
    image_list = []

    for file in glob.glob('C:/Users/rasmi/Desktop/RasmiCapstone/newframes/*.jpg'):
        im = Image.open(file)
        image_list.append(im)

    list = ['A', 20]
    print(list)

    count = 0
    image_same_name_list = []

    for ima in image_list:
        image_same_name_list.append(ima)
        count = count + 1
        if (count % 3 == 0):
            bestface(image_same_name_list)
        # ima.save('C:/Users/rasmi/Desktop/RasmiCapstone/replacedpic%d.png' % count,'PNG')
        # count = count + 1


main()
print("Guru99")