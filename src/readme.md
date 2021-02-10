
- This folder contains the source files used for generating semi-automatic labelled dataset, CNN_classifier training files and prediction file which can be used for generating Deep Banding index for any image. 
- **XML to CSV:** the mask generated for HD images of size 1920x1080 were stored in XML files, these XML files contain information about the rectangular masking coordinates.
These rectangular masking coordinates were generated using [`LabelImg`](https://github.com/tzutalin/labelImg).
  - Refer [`XML_to_CSV`](xml_to_csv.py) for the code used to convert XML files region infomation to CSV files.
- The patches are generated using heuristic rules from HD images and the obatined csv file about banded, non banded region information.
  - Refer [`Patche Generation From HD Images`](Generating_patches_from_HD_images.py)
  - The image below shows how these patches are extratced from a HD image.     
  -                 ![](Patches_Generation.png)
