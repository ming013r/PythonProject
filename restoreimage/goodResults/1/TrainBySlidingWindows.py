import neupy
import CorruptImage as imageUtil
from PIL import Image
import numpy
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from neupy import algorithms, storage
import pickle
import os


class ImageInfo:
    x=0
    y=0
    z=0
    array=[]

    def __init__(self, iArray):
        self.x = numpy.size(iArray, 0)
        self.y = numpy.size(iArray, 1)
        self.z = numpy.size(iArray, 2)
        self.array = iArray



def retrieveFromTxt():
    trainList = pd.read_csv('txtSrc/trainData.csv').sample(50000)

    dirtylist = numpy.array(trainList)[:,0:9]
    clean_targetlist = numpy.array(trainList)[:,4]

    return [dirtylist, clean_targetlist]

def train(data):
    dirtylist = data[0]
    clean_targetlist = data[1]
    print("traning is running.....")
    lmnet = algorithms.LevenbergMarquardt((9, 30, 1))
    lmnet.train(dirtylist, clean_targetlist,epochs=30)
    storage.save(lmnet,filepath="ModelTrained/newModel.pickle")

def test():
    targetModel = 'ModelTrained/newModel.pickle'
    test_data = numpy.array([0.914,0.631,0.455,0.831,0.671,0.569,0.733,0.671,0.635])
    if os.path.getsize(targetModel) > 0:

        lmnet = algorithms.LevenbergMarquardt((9, 10, 1))

        storage.load(lmnet,targetModel)
        print(lmnet.predict(test_data))

    else:
        print(str(os.path.getsize(targetModel)))



def WriteData(dirtyArray,cleanArray, size_x, size_y, size_z):
    text_file= open("txtSrc/trainData.csv", "w")

    newProcess = 0.0
    nowCnt=0.0
    totalCnt = (size_x-2)*(size_y-2)
    #text_file = open("Output_Clean.txt", "w")
    text_file.writelines("1,2,3,4,5,6,7,8,9,10\n")
    for x in range(0, size_x-2):
        for y in range(0,size_y-2):
            subArr=[]
            eachline = ""
            for i in range(x,x+3):
                for j in range(y,y+3):
                    subArr.append(dirtyArray[i][j][0])
                    newVal = 0.0
                    newVal = round(dirtyArray[i][j][0] / 255, 3)
                    eachline += str(newVal)+","
            eachline += str(round(cleanArray[x+1][y+1][0]/255,3))
            text_file.writelines(eachline+"\n")

            nowProcess = round(nowCnt/totalCnt*100)
            if newProcess != nowProcess:
                print("writing csv : " + str(newProcess) + "%")
            newProcess = nowProcess
            nowCnt += 1
    text_file.close()
    print("writing csv : 100%")


def TraineFromTxt():
    originImageRaw = Image.open("image/lena.bmp")
    dirtyImageRaw = Image.open("image/dirtyLena.jpg")

    originImageFile = imageUtil.convertToJpg(originImageRaw)
    dirtyImageFile = imageUtil.convertToJpg(dirtyImageRaw)

    #new enitiy of image
    originImage = ImageInfo(numpy.array(originImageFile))
    dirtyImage = ImageInfo(numpy.array(dirtyImageFile))

    WriteData(dirtyImage.array,originImage.array, originImage.x,originImage.y,originImage.z)

    traindata = retrieveFromTxt()
    train(traindata)
    #test()















