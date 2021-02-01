clc; clear; close all;

%% change directory
% prev_dir = pwd; file_dir = fileparts(mfilename('fullpath')); cd(file_dir);
% addpath(genpath(pwd));

%% dipIQ
% img1 = imread('./test images/1.png');
% q1 = dipIQ(img1, 1);
% 
% img2 = imread('./test images/2.png');
% q2 = dipIQ(img2, 1);
% 
% img3 = imread('./test images/3.png');
% q3 = dipIQ(img3, 1);
% 
% img4 = imread('./test images/4.png');
% q4 = dipIQ(img4, 1);
% 
% figure, 
% subplot(2,2,1), imshow(img1), title(sprintf('dipIQ = %3.3f', q1));
% subplot(2,2,2), imshow(img2), title(sprintf('dipIQ = %3.3f', q2));
% subplot(2,2,3), imshow(img3), title(sprintf('dipIQ = %3.3f', q3));
% subplot(2,2,4), imshow(img4), title(sprintf('dipIQ = %3.3f', q4));

file = dir('banded_data/');
file = file(~[file.isdir]);
NF = length(file);
disp(NF);
score = zeros(NF,1);
TIMECAL   = ones(100,1);
for i = 1:100
    in_img = imread(fullfile('banded_data/', file(i).name));
    disp(i);
    tic
    q = dipIQ(in_img, 1);
    toc
    p = toc
    TIMECAL(i,1) = p
    score(i,1) = q;
end
csvwrite('banded.csv', score(:));
csvwrite('Time_cal.csv',TIMECAL(:));