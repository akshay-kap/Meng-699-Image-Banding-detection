import cv2
import numpy as np
import os

class VideoCaptureYUV:
    def __init__(self, filename, size):
        self.height, self.width = size
        self.frame_len = int(self.width * self.height * 3 / 2)
        print(self.frame_len)
        self.f = open(filename, 'rb')
        self.f_new=open("test111.yuv", 'wb+')
        self.shape = (int(self.height*1.5), self.width)

    def quantize(self,y_comp,bits,bdepth=8):
        y_comp=np.uint8(np.rint(y_comp*(pow(2,bits)/pow(2,bdepth))))
        return y_comp
    def quantize_inverse(self,y_comp,bits,bdepth=8):
        y_comp=np.uint8(np.rint(y_comp*(pow(2,bdepth)/pow(2,bits))))
        return y_comp
    def adjust_luminance(self,y_comp,step):
        y_comp=np.clip(y_comp+step,a_min = 2, a_max = 255)
        return y_comp        
    def read_raw(self):
#         raw = self.f.read(2*self.frame_len)
#         yuv = np.frombuffer(raw, dtype=np.uint16)
#         print(np.shape(yuv))
#         yuv = yuv.reshape(self.shape)
        try:
            raw = self.f.read(self.frame_len)
            yuv = np.frombuffer(raw, dtype=np.uint8)
            yuv = yuv.reshape(self.shape)
        except Exception as e:
            print(str(e))
            return False, None
        return True, yuv

    def read(self,lum_step=0):
        ret, yuv = self.read_raw()
        if not ret:
            return ret, yuv
        y=yuv[:1080,:]
        uv=yuv[1080:,:]
        # y=self.adjust_luminance(y,step=lum_step)
        y=self.quantize(y,6,8)
        # uv=self.quantize(uv,5,8)
        y=self.quantize_inverse(y,6,8)
        # uv=self.quantize_inverse(uv,5,8)
        
        yuv=np.concatenate((y,uv),axis=0)

        yuv_mod = yuv.reshape(self.frame_len,)
        print(np.shape(yuv_mod))
        raw_quant = self.f_new.write(bytearray(yuv_mod))
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB_I420)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        # gray=gray = cv2.cvtColor(yuv, cv2.COLOR_BGR2GRAY)
        return ret, rgb


if __name__ == "__main__":
    # path="./../potentials/originals/yuv_2"
    path="./yuv"
    files=os.listdir(path)
    for name in files:
        filename=path+'\\'+name
        # filename="0165_fps30.yuv"
        print(filename)
        # size = (1080, 1920)
        # cap = VideoCaptureYUV(filename, size)
        # fourcc=cv2.VideoWriter_fourcc(*'MP4V')
        # fourcc=0x7634706d
        # fps=int(name[-6:-4])
        # print("hey...",fps)
        
        for lum_step in range(0,1):
            size = (1080, 1920)
            cap = VideoCaptureYUV(filename, size)
            fourcc=cv2.VideoWriter_fourcc(*'MP4V')
            fourcc=0x7634706d
            fps=int(name[-6:-4])
            # print("fps...",fps)
            out=cv2.VideoWriter('./mp4/{0}_6b.mp4'.format(name[:-4]),fourcc,fps,(1920,1080))
            print(lum_step)
            while 1:
                ret, frame = cap.read(lum_step)
                out.write(frame)
                # print(frame)
                if ret:
                    cv2.imshow("frame", frame)
                    cv2.waitKey(1)
                else:
                    break
        break
        
    cv2.destroyAllWindows()