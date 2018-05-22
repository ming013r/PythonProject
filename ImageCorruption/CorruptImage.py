
from PIL import Image
from numpy import array
from random import randint
import numpy




##################Image Process################
def SaveImageFromArray(arr):
    img = Image.fromarray(arr)
    img.save("outTestImage.png")
def corrput(x,y,z,arr,flag):
    nval=arr[x][y][z]
    if(flag==0):
        nval+=100
        if(nval>=255):
            arr[x][y][z]=255
        else:
            arr[x][y][z]=nval
    else:
        nval-=100
        if(nval<=0):
            arr[x][y][z]=0
        else:
            arr[x][y][z]=nval



def main():

    img = Image.open("testImg.png")
    arr = numpy.array(img)
    originArr = numpy.array(img)

    for i in range(0,1000):
        randX=randint(0,459)
        randY=randint(0,832)
        randZ=randint(0,3)

        corrput(randX,randY,randZ,arr,i%2)
    im = Image.fromarray(arr)
    im.save("outTestImage.png")

    #this is checking
    #cnt=0
    # for i in range(460):
    #     for j in range(833):
    #         for k in range(4):
    #             oVal=originArr[i][j][k]
    #             nVal=arr[i][j][k]
    #
    #             if(nVal!=oVal):
    #                 cnt+=1
    #                 print(str(cnt)+".the differnce : Origin["+str(oVal)+"], New["+str(nVal)+"]")
    #



if __name__ == '__main__':
    main()