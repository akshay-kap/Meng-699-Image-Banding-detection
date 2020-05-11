import os
import subprocess
from subprocess import check_output


def step():
	#step 3
    inputfilepath="./mp4"
    outputfilepath="./org"
    files=os.listdir(inputfilepath)
    for name in files:
        try:
            cmd="ffmpeg -i {0} -vf fps=0.2 {1}".format(inputfilepath+"/"+name,outputfilepath+"/%06d_"+name[:4]+".png") 
            check_output(cmd, shell=True).decode()
            print(cmd)
        except:
            pass
    print("shukar hai!")
    print("step  completed")



if __name__ == "__main__":
	step()








