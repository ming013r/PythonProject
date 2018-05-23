
from PIL import Image
from random import randint
import numpy


def convertToJpg(file):
    rgb_im = file.convert('RGB')
    return rgb_im


def SaveImageFromArray(arr):
    img = Image.fromarray(arr)
    img.save("outTestImage.png")


def checkCorrupted(arr, originArr, x, y, z):

    cnt = 0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                originValue = originArr[i][j][k]
                newValue = arr[i][j][k]

                if newValue != originValue:
                    cnt += 1
                    print(str(cnt)+".the differnce : Origin["+str(originValue)+"], New["+str(newValue)+"]")


def fill(x, y, z, arr, flag):
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


def execute(rate):
    img = Image.open("testImg.png")
    jpgImage = convertToJpg(img)
    arr = numpy.array(jpgImage)
    originArr = numpy.array(jpgImage)

    dim_x = numpy.size(arr, 0)
    dim_y = numpy.size(arr, 1)
    dim_z = numpy.size(arr, 2)

    #make sure polluted dots is plural
    times_double = arr.size * rate / 100
    times_int = 0
    if round(times_double) % 2 != 0:
        times_int = round(times_double)-1
    else:
        times_int = round(times_double)

    newProcess = 0
    for i in range(0, times_int):
        randX = randint(0, dim_x - 1)
        randY = randint(0, dim_y - 1)
        randZ = randint(0, dim_z - 1)
        fill(randX, randY, randZ, arr, i % 2)

        nowProcess = round(i / times_double * 100)


        if newProcess != nowProcess:
            print(str(newProcess) + "%")
        newProcess = nowProcess


    im = Image.fromarray(arr)
    im.save("outTestImage.png")
    #checkCorrupted(arr, originArr, dim_x, dim_y, dim_z)

