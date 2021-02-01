clearvars; close all; clc
imD = imread('test_fake_24.png');
imD2 = imread('test_true_10.png');
% load codebook
load('CSIQ_codebook_BS7.mat','codebook0');
load('LIVE_soft_svm_model.mat','soft_model','soft_scale_param');
% load whitening parameter
load('CSIQ_whitening_param.mat','M','P');
svm_model = soft_model;
svm_scale = soft_scale_param;

Num_Run=10;
tic
for i=1:1:Num_Run
    score2 = CORNIA(imD2, codebook0, 'soft', svm_model, svm_scale, M, P, 10000);
%     score1 = CORNIA(imD, codebook0, 'soft', svm_model, svm_scale, M, P, 10000);
end
Avg_Time=toc/(Num_Run*2);

disp(['Average Time per Image in Seconds: ' num2str(round(Avg_Time,4)) ' Seconds']);