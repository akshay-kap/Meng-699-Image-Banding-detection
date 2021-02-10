This folder contains the source files used for generating semi-automatic labelled dataset, CNN_classifier training files and prediction file which can be used for generating Deep Banding index for any image. 
- **XML to CSV:** the mask generated for HD images of size 1920x1080 were stored in XML files, these XML files contain information about the rectangular masking coordinates.
These rectangular masking coordinates were generated using [`LabelImg`](https://github.com/tzutalin/labelImg).
  - Refer [`XML_to_CSV`](xml_to_csv.py) for the code used to convert XML files region infomation to CSV files.
- **Patches Generation:** The patches are generated using heuristic rules from HD images and the obatined csv file about banded, non banded region information.
  - Refer [`Patche Generation From HD Images`](Generating_patches_from_HD_images.py)
  - The image below shows how these patches are extratced from a HD image.     
     ![](Patches_Generation.png)
- **CNN Classifier Training**: The CNN Classifier is trained using the [`EDIT Patches Dataset Link`](https://github.com/tzutalin/labelImg).
  - Refer [`Training Script`](train.py) for CNN_classifier Training for Banded vs NonBanded classification tasks.
- **Calculating Scores Using Deep Banding Index**: Deep Banding Index is calculated using CNN_model Classifer and the methodology described in the [`DBI paper Add Link`](). 
  - Refer [`Deep Banding Index Prediction Script`](predict.py) for using DBI for out of sample image.
    - Dependencies are [`OpenCV, numpy, tensorflow -2.1, pandas`] 
 - **Generating Banding Visualizations**: The script [`Deep Banding Map Generation`](Deep_Banding_Map.py) explains the working of Deep Banding Index by generating Deep Banding Maps for HD images.
  - For a typical Quantized Image as:
  <br>
   ![`Sample Quantized Image`](000001_0091.png)
  - The following Deep Banding Map is generated using Deep Banding index methodology for above Image:
   <br>
   ![`Deep Banding Mask Generated`](000001_0091.png_Deep_Banding_Mak.jpg)
