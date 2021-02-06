These files explain how quantized frames are extracted from 10 second HD videos of size 1920 x 1080.
The bit depth reduction is applied in Luma and chroma channels by following ways:
1. 8 bit Luma channel bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth.
 __Refer__ [`L6_Single_Step.py`](L6_Single_Step.py)
2. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and 5 bit channel depth respectively, and then both channels are scaled up again as 8 bit depth channels.
 __Refer__ [`L6_UV_5 Single_step.py`](L6_UV_5 Single_step.py)
3. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and then both channels are scaled up again as 8 bit depth channels.
 __Refer__ [`L6_UV_6_Single_Step.py `](L6_UV_6_Single_Step.py)
4. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and 5 bit channel depth, and then both channels are scaled up again as 8 bit depth channels., this step of bit reduction is performed twice.
 __Refer__ [`L6_Double_Step.py`](L6_Double_Step.py)
5. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth, this step of bit reduction is performed twice.
 __Refer__ [`L6_UV_6_Double_Step.py `](L6_UV_6_Double_Step.py)
6. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and then both channels are scaled up again as 8 bit depth channels, this step of bit reduction is performed twice.
 __Refer__ [`L6_UV_5 Double_step.py`](L6_UV_5 Double_step.py)


