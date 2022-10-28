from sixrandom import attack
from multiprocessing import Process,freeze_support
import os
if __name__ == '__main__':
    freeze_support()
    t1 = Process(target=attack, args=('黃銘信','numonlyT.txt',True,2))
    t1.daemon = True
    t1.start()
    t2 = Process(target=attack, args=('黃銘信','numonlyF.txt',False,2))
    t2.daemon = True
    t2.start()
    print('Running attack on 黃銘信,numonly')
    while True:
        t = open('numonlyT.txt','r')
        f = open('numonlyF.txt','r')
        try:
            if int(t.read()) > int(f.read()):
                f.close()
                t.close()
                t1.terminate()
                t2.terminate()
                break
        except:
            pass
