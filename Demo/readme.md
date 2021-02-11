Use this folder structure to calculate Deep Banding Index for your images, follow these steps to get Deep Banding Score for HD banded Images:
- Download [`Demo`](Meng-699-Image-Banding-detection/Demo) folder.
- Put the HD images in [`Image Path Folder`](Given_image_path/)
- Run [`DBI Predict File`](predict.py), make sure you have the following dependencies on your device 
  - [`Tensorflow 2.1, numpy, pandas, Open-CV`], and you have [`CNN_Banded Patch classifer`](CNN_classifier/) in the same path as presented in Demo folder.
- open the [`CSV Result File`](banding_score_results.csv) to see the results associated with the HD images present in the [`Image Path Folder`](Given_image_path/). 
