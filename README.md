## DBI (Deep Banding Index)

This is the official **Python Tensorflow** implementations of our ICASSP 2020 paper [*"CAPTURING BANDING IN IMAGES: DATABASE CONSTRUCTION AND
OBJECTIVE ASSESSMENT"*](https://2021.ieeeicassp.org/).


- [1. Brief Introduction](#1-brief-introduction)
  * [1.1 Backgrounds](#11-backgrounds)
  * [1.2 Contributions](#12-contributions)
  * [1.3 Results](#13-results)
  * [1.4 Citation](#14-citation)
- [2. Dataset](#2-dataset)
  * [2.1 Banding Patches Dataset](#21-tcgafocus)
  * [2.2 HD Images Dataset with Banded and NonBanded Region Information](#22-focuspath-full)
- [3. Prerequest](#3-prerequest)
  * [3.1 Environment](#31-environment)
  * [3.2 Packages](#32-packages)
  * [3.3 Pretrained Models](#33-pretrained-models)
- [4. Python Demo for testing a single image](#4-running-the-code)
- [5. Codes for comparing models](#5-codes-for-comparing-models)
- [6. License](#6-license)


### 1. Brief Introduction

#### 1.1 Backgrounds

#### 1.2 Contributions


#### 1.3 Results


#### 1.4 Citation


```

### 2. Dataset

#### 2.1 [HD Images Dataset with Banded and NonBanded region Information](https://zenodo.org/)
  - **Download**: The dataset is available on Zenodo under a Creative Commons Attribution license: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3910757.svg)](https://doi.org/10.5281/zenodo.3910757).

#### 2.2 [Banding Patches Dataset](https://zenodo.org/record/3926181#.Xv4vg3X0kUd)

   - **Download**: The dataset is available on Zenodo under a Creative Commons Attribution license: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3926181.svg)](https://doi.org/10.5281/zenodo.3926181)


### 3. Prerequest

#### 3.1 Environment

The code has been tested on `Ubuntu 18.04` with `Python 3.8` and `cuda 10.2`

#### 3.2 Packages

`tensorflow-gpu=2.1`, `statistics`, `pandas`, `pillow` (or `pillow-simd`)

#### 3.3 Pretrained Models

  - Pretrained models could be found in folder `pretrained_model/`

### 4. Running the code


#### 4.1 Python Demo for testing a single image (heatmap available)

Use [predict.py](`src/predict.py`)

### 5. Codes for comparing models

