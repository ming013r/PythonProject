import CorruptImage as corruption
import numpy
import TrainBySlidingWindows as mytrainer
import RepairImage as RepairImage
import time


def main():
    start_Time = time.time()


    corruption.execute(5)
    mytrainer.TraineFromTxt()
    RepairImage.repair()
    RepairImage.showImages()


    print('Finish.')
    end_Time = time.time()
    print("Estimated Time : "+ str(round(end_Time - start_Time)))

if __name__ == '__main__':
        main()
