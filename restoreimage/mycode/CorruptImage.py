
from PIL import Image
from random import randint
import numpy


def convertToJpg(file):
    rgb_im = file.convert('RGB')
    return rgb_im


def checkCorrupted(arr, originArr, x, y, z):

    cnt = 0
    for i in range(x):
        for j in range(y):
            originValue = originArr[i][j][0]
            newValue = arr[i][j][0]

            if newValue != originValue:
                cnt += 1
                print(str(cnt)+".the differnce : Origin["+str(originValue)+"], New["+str(newValue)+"]")

    print(arr)
    print(originArr)


def fill(x, y, arr, flag):
    newValue = arr[x][y][0]
    for i in range(0,3):
        if flag == 0:
            newValue += 100
            if newValue >= 255:
                arr[x][y][i] = 255
            else:
                arr[x][y][i] = newValue
        else:
            newValue -= 100
            if newValue <= 0:
                arr[x][y][i] = 0
            else:
                arr[x][y][i] = newValue


def execute(rate):
    img = Image.open("image/lena.bmp")
    jpgImage = convertToJpg(img)
    arr = numpy.array(jpgImage)
    originArr = numpy.array(jpgImage)

    dim_x = numpy.size(arr, 0)
    dim_y = numpy.size(arr, 1)
    dim_z = numpy.size(arr, 2)

    #make sure polluted dots is plural
    times_double = dim_x*dim_y * rate / 100
    times_int = 0
    if round(times_double) % 2 != 0:
        times_int = round(times_double)-1
    else:
        times_int = round(times_double)

    newProcess = 0
    for i in range(0, times_int):
        randX = randint(0, dim_x - 1)
        randY = randint(0, dim_y - 1)
        #fill(randX, randY, arr, i % 2)

        nowProcess = round(i / times_double * 100)
        if newProcess != nowProcess:
            print("Corruption Process : "+str(newProcess) + "%")
        newProcess = nowProcess
    print("Corruption Process : 100%");

    im = Image.fromarray(arr)
    im.save("image/dirtyLena.jpg")
    #checkCorrupted(arr, originArr, dim_x, dim_y, dim_z)

