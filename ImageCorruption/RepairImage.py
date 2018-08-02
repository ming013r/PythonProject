from neupy import algorithms, storage
import os
import numpy
from PIL import Image
import matplotlib.pyplot as plt


def repair():
    targetModel = 'ModelTrained/newModel.pickle'
    if os.path.getsize(targetModel) > 0:

        LM = algorithms.LevenbergMarquardt((9, 20, 1))
        storage.load(LM, targetModel)
        imageArr = getImageArray(0)

        oldNum = 0
        cnt = 0
        arrSize = numpy.size(imageArr,0) * numpy.size(imageArr, 1)
        for x in range(0, numpy.size(imageArr,0) - 2):
            for y in range(0, numpy.size(imageArr, 1) - 2):
                aWindow = getWindow(imageArr, x, y)
                for i in range(0,3):
                    predicted = LM.predict(aWindow)
                    origin = predicted * 255

                    if origin > 255 :
                        origin = 255
                    elif origin < 0:
                        origin = 0
                    imageArr[x + 1][y + 1][i] = origin

                newNum = round(cnt / arrSize*100)
                if newNum != oldNum:
                    print("repair in process : " + str(newNum) + "%")
                oldNum = newNum
                cnt += 1
        print("repair in process : 100%")



        im = Image.fromarray(imageArr)
        im.save("image/repaired.jpg")

        MSEs = getMSE(imageArr)
        print("dirty MSE : " + str(MSEs[0]))
        print("repair MSE : " + str(MSEs[1]))

    else:
        print(str(os.path.getsize(targetModel)))


def getImageArray(type):  #0= dirty,  1=clean, 2= repair

    if type==0:
        img = Image.open("image/dirtyLena.jpg")
    elif type == 1:
        bmpimg = Image.open("image/lena.bmp")
        img  = bmpimg.convert('RGB')
    elif type == 2:
        img = Image.open("image/repaired.jpg")
    arr = numpy.array(img)
    return arr


def getWindow(wholeArr, x, y):
    result = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    index = 0
    for i in range(0,3):
        for j in range(0, 3):
            result[index] = round(wholeArr[x+i][y+j][0] / 255,3)
            index += 1

    return  result

def getMSE(arr_repaired):
    arr_dirty = getImageArray(0)
    arr_clean = getImageArray(1)

    n = (numpy.size(arr_clean,0)-2) * (numpy.size(arr_clean,1)-2)

    error_dirty = 0.0
    error_repair = 0.0
    for x in range(2, numpy.size(arr_clean, 0) - 2):
        for y in range(2, numpy.size(arr_clean, 1) - 2):
            error_dirty += (arr_dirty[x][y][0] - arr_clean[x][y][0]) ** 2
            error_repair += (arr_repaired[x][y][0] - arr_clean[x][y][0]) ** 2

    print("total error(dirty) : "+str(error_dirty))
    print("total error(repaired) : "+str(error_repair))
    print("n = " + str(n))
    result = [(error_dirty**0.5)/n,(error_repair**0.5)/n]
    return result



def showImages():
    originImageRaw = Image.open("image/lena.bmp")
    dirtyOne = Image.open("image/dirtyLena.jpg")
    reOne = Image.open("image/repaired.jpg")

    fig = plt.figure()
    columns = 3
    rows = 1

    fig.add_subplot(rows, columns, 1)
    plt.imshow(originImageRaw)
    fig.add_subplot(rows, columns, 2)
    plt.imshow(dirtyOne)
    fig.add_subplot(rows, columns, 3)
    plt.imshow(reOne)
    plt.show()