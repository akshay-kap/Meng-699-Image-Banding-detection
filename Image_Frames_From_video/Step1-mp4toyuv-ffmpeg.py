import os
import subprocess
from subprocess import check_output

if __name__ == "__main__":

    # inputfilepath="./../potentials/originals/mp4_2"
    # outputfilepath="./../potentials/originals/yuv_2"
    inputfilepath="./mp4"
    outputfilepath="./yuv"
    files=os.listdir(inputfilepath)
    for name in files:
        cmd="ffmpeg -i {0} -c:v rawvideo -pix_fmt yuv420p {1}".format(inputfilepath+"/"+name,outputfilepath+"/"+name[:-3]+"yuv") 
        check_output(cmd, shell=True).decode()
        print(cmd)
    print("shukar hai!")