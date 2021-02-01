%==========================================================================
% 1) Please cite the paper (K. Gu, G. Zhai, X. Yang, and W. Zhang, "Hybrid 
% no-reference quality metric for singly and multiply distorted images," 
% IEEE Trans. Broadcasting, vol. 60, no. 3, pp. 555-567, Sept. 2014.)
% 2) If any question, please contact me through guke.doctor@gmail.com; 
% gukesjtuee@gmail.com. 
% 3) Welcome to cooperation, and I am very willing to share my experience.
%==========================================================================

clearvars;
% clc;
%I is an RGB Color Image
% I = imread('i1075.bmp');
file = dir('banded/');
file = file(~[file.isdir]);
NF = length(file);
disp(NF);
score = zeros(NF,1);
TIMECAL   = ones(100,1);
for i = 1:100
    
    in_img = imread(fullfile('banded/', file(i).name));
    disp(i);
    tic
    score(i,1) = SISBLIM_SM(in_img);   % SISBLIM_SM is the original method as per paper
    toc
    p = toc
    TIMECAL(i,1) = p
end
csvwrite('banded.csv', score(:));
csvwrite('Time_cal.csv',TIMECAL(:));