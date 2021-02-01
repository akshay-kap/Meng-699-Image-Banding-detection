clearvars; close all; clc
imD = imread('test_fake_24.png');
imD2 = imread('test_true_10.png');

Num_Run=10;
tic
for i=1:1:Num_Run
    score2 = LPSI(imD2,1,4);
    score1 = LPSI(imD,1,4);
end
Avg_Time=toc/(Num_Run*2);

disp(['Average Time per Image in Seconds: ' num2str(round(Avg_Time,4)) ' Seconds']);