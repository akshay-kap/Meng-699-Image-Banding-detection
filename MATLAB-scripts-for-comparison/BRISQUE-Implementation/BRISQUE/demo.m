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
    score(i,1) = brisquescore(in_img);
    toc
    p = toc
    TIMECAL(i,1) = p
    disp(score(i,1));
end
csvwrite('BRISQUE.csv', score(:));
csvwrite('Time_cal.csv',TIMECAL(:));