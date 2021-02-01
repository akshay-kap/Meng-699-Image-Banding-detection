/*****************************************************************************************
*    Unsupervised Feature Learning Framework for No-reference Image Quality Assessment   *
*					         Peng Ye and David Doermann           					     *                   
*     		         Language and Media Processing Laboratory         			         *
*	         University of Maryland Institute For Advanced Computer Studies	             * 
/*****************************************************************************************

Copyright 2012, Peng Ye and David Doermann All Rights Reserved 

Permission to use, copy, modify, and distribute this software and 
its documentation for any non-commercial purpose is hereby granted 
without fee, provided that the above copyright notice appear in 
all copies and that both that copyright notice and this permission 
notice appear in supporting documentation, and that the name of 
the author not be used in advertising or publicity pertaining to 
distribution of the software without specific, written prior 
permission. 

THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, 
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR 
ANY PARTICULAR PURPOSE. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR 
ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN 
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING 
OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. 

/**********************************************************************
* 						General information 					 	  *
/**********************************************************************

For questions concerning the code please contact Peng Ye <pengye AT umiacs DOT umd DOT edu>. 

If you find this software useful for your research, please cite the following paper.

@inproceedings{pengye-12-a,
    author = { {P}eng {Y}e and {J}ayant {K}umar and {L}e {K}ang and {D}avid {D}oermann },
    booktitle = { {I}ntl. {C}onf. on {C}omputer {V}ision and {P}attern {R}ecognition ({CVPR} 2012) },
    pages = { 1098-1105 },
    pdffile = { http://lampsrv02.umiacs.umd.edu/pubs/Papers/pengye-12-a/pengye-12-a.pdf },
    otherfile = { http://lampsrv02.umiacs.umd.edu/pubs/Papers/pengye-12-a/cvpr12qualitycorrected.pdf },
    title = { {U}nsupervised {F}eature {L}earning {F}ramework for {N}o-reference {I}mage {Q}uality {A}ssessment },
    year = { 2012 }
}


/**********************************************************************
* 			Usage		 											  *
/**********************************************************************
------------------------------------------
Dependencies :
------------------------------------------
- Please install LibSVM for SVM training and predicting:
	http://www.csie.ntu.edu.tw/~cjlin/libsvm/ 
	Copyright (c) 2000-2012 Chih-Chung Chang and Chih-Jen Lin All rights reserved.

- To use LLC encoding, please install Locality-constrained Linear Coding for Image Classification (CVPR'10), http://www.ifp.illinois.edu/~jyang29/LLC.htm

- To use sparse coding based encoding, please install: SPArse Modeling Software, http://spams-devel.gforge.inria.fr/

	This code has only been tested on 64-bit linux machine.
	
------------------------------------------
Descriptions :
------------------------------------------
CORNIA.m -- compute quality score of a testing image using trained model.
CORNIA_Fv.m -- extract encoded feature for a testing image.
CORNIA_train.m -- training prediction model using libsvm
main.m -- examples of how use the code to compute quality scores of a testing image

CSIQ_codebook_BS7.mat -- codebook of different sizes trained on CSIQ data set http://vision.okstate.edu/?loc=csiq
CSIQ_whitening_param.mat -- whitening parameters obtained on CSIQ data set

LIVE_soft_svm_model.mat -- trained model on LIVE dataset using soft-assignment encoding
