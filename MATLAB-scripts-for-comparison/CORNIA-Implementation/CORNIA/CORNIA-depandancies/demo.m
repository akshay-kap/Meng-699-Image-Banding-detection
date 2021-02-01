clear all;
close all;
clc;
% addpath(genpath('./libsvm-3.12/matlab/')); % No need to define this separately if entire folder added to path
% img = rgb2gray(open_bitfield_bmp('E:\CR-IQA\NR-IQA\Used in CR-IQA Work\CORNIA Code\corniaDependency\img215.bmp'));
% img = imread('Dist.jpg');
% load codebook
load('CSIQ_codebook_BS7.mat','codebook0');
load('LIVE_soft_svm_model.mat','soft_model','soft_scale_param');
% load whitening parameter
load('CSIQ_whitening_param.mat','M','P');

svm_model = soft_model;
svm_scale = soft_scale_param;

file = dir('banded/');
file = file(~[file.isdir]);
NF = length(file);
disp(NF);
score = zeros(NF,1);
Time_yes = ones(100,1)
for i = 1:100
    tic
    in_img = imread(fullfile('banded/', file(i).name));
    disp(i);
    score(i,1) = CORNIA(in_img, codebook0, 'soft', svm_model, svm_scale, M, P, 10000);
    disp(p)
    p = toc 
    Time_yes (i,1) = p
end
csvwrite("Time_yes.csv", Time_yes(:));
csvwrite('CORNIA.csv', score(:));