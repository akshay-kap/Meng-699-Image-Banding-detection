These files explain how quantized frames are extracted from 10 second HD videos of size 1920 x 1080.
The bit depth reduction is applied in Luma and chroma channels by following ways:
1. 8 bit Luma channel bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth.

2. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and 5 bit channel depth respectively, and then both channels are scaled up again as 8 bit depth channels.
[`L6_UV_5 only step converting to banding images directly 0.2FPS.py`]
3. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and then both channels are scaled up again as 8 bit depth channels.
[`L6_UV_6 converting to banding images directly 0.2FPS.py`]
4. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and 5 bit channel depth, and then both channels are scaled up again as 8 bit depth channels., this step of bit reduction is performed twice.
  [refer `L6 Doube step converting to banding images directly 0.2FPS.py`]
5. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth, this step of bit reduction is performed twice.
[refer `L6_UV_5 Double step converting to banding images directly 0.2FPS.py`]
6. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth, and then both channels are scaled up again as 8 bit depth channels, this step of bit reduction is performed twice.
[ refer `L6_UV_6 Double step converting to banding images directly 0.2FPS.py`]

[`data/FocusPath_full_split1.txt`](data/FocusPath_full_split1.txt)
[`L6 converting to banding images directly 0.2FPS.py`](Meng-699-Image-Banding-detection/Dataset-Generation/Generating-Quantized-frames-from-videos/L6 converting to banding images directly 0.2FPS.py)
