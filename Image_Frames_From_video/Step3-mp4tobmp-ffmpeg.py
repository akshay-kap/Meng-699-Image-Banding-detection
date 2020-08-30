import os
import subprocess
from subprocess import check_output

if __name__ == "__main__":

    # inputfilepath="./../potentials/originals/mp4_2"
    # outputfilepath="./../potentials/originals/png_sub2"
    inputfilepath="./mp4"
    outputfilepath="./png"
    files=os.listdir(inputfilepath)
    for name in files:
        try:
            cmd="ffmpeg -i {0} -vf fps=0.2 {1}".format(inputfilepath+"/"+name,outputfilepath+"/%06d_"+name[:4]+".png") 
            check_output(cmd, shell=True).decode()
            print(cmd)
        except:
            pass
    print("shukar hai!")