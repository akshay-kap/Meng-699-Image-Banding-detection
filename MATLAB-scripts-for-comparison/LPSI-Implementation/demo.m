clear all
close all
clc

file = dir('banded/');
file = file(~[file.isdir]);
NF = length(file);
disp(NF);
score = zeros(NF,1);
TIMECAL   = ones(100,1);
for i = 1:100
    in_img = imread(fullfile('banded/', file(i).name));
    tic
    score(i,1) = LPSI(in_img,1,4);
    toc
    p = toc
    TIMECAL(i,1) = p
    disp(i);
end

csvwrite('LPSI.csv', score(:));
csvwrite('Time_cal.csv',TIMECAL(:));