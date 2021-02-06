These files explain how quantized frames are extracted from 10 second HD videos of size 1920 x 1080.
The bit depth reduction is applied in Luma and chroma channels and is applied by following ways:
1. 8 bit Luma channel bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth.
2. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth.
3. 8 bit Chroma channel bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth.
4. 8 bit UV channel bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth, this step of bit reduction is performed twice.
5. 8 bit Chroma channel and Luma bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth, this step of bit reduction is performed twice.
6. 8 bit Chroma channel bit first reduced to 6 bit channel depth and then scaled up again as 8 bit depth, this step of bit reduction is performed twice.
