
from PIL import Image
from random import randint
import numpy


def convertToJpg(file):
    rgb_im = file.convert('RGB')
    return rgb_im


def SaveImageFromArray(arr):
    img = Image.fromarray(arr)
    img.save("outTestImage.png")


def checkCorrupted(arr, originArr):

    cnt = 0
    for i in range(460):
        for j in range(833):
            for k in range(3):
                originValue = originArr[i][j][k]
                newValue = arr[i][j][k]

                if newValue != originValue:
                    cnt += 1
                    print(str(cnt)+".the differnce : Origin["+str(originValue)+"], New["+str(newValue)+"]")


def corrupt(x, y, z, arr, flag):
    newValue = arr[x][y][z]
    if flag == 0:
        newValue += 100
        if newValue >= 255:
            arr[x][y][z] = 255
        else:
            arr[x][y][z] = newValue
    else:
        newValue -= 100
        if newValue <= 0:
            arr[x][y][z] = 0
        else:
            arr[x][y][z] = newValue


def main():
    img = Image.open("testImg.png")
    jpgImage = convertToJpg(img)
    arr = numpy.array(jpgImage)
    originArr = numpy.array(jpgImage)

    for i in range(0, 1000):
        randX = randint(0, 459)
        randY = randint(0, 832)
        randZ = randint(0, 2)

        corrupt(randX, randY, randZ, arr, i % 2)
    im = Image.fromarray(arr)
    im.save("outTestImage.png")


if __name__ == '__main__':
    main()
