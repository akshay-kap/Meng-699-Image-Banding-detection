
clear;clc;
cnt = 0;
for i = 1:12
img1_name = ['D:\LEARN\LABOR\DATABASE\MDID2013\org' num2str(i,'%.3d') '.png'];
img1 = imread(img1_name);
img1 = double(rgb2gray(img1));
for j = 1:27
cnt = cnt+1
img2_name = ['D:\LEARN\LABOR\DATABASE\MDID2013\img' num2str(cnt,'%.3d') '.png'];
img2 = imread(img2_name);
img2 = double(rgb2gray(img2));
MDID_sisblim_sm(cnt,:)  = sisblim_sm_index(img2);
MDID_sisblim_wm(cnt,:)  = sisblim_wm_index(img2);
MDID_sisblim_sfb(cnt,:) = sisblim_sfb_index(img2);
MDID_sisblim_wfb(cnt,:) = sisblim_wfb_index(img2);
end
end

cc(1) = abs(corr(MDID_sisblim_sm,LIVEMD_dmos,'type','spearman'));
cc(2) = abs(corr(MDID_sisblim_wm, LIVEMD_dmos,'type','spearman'));
cc(3) = abs(corr(MDID_sisblim_sfb,LIVEMD_dmos,'type','spearman'));
cc(4) = abs(corr(MDID_sisblim_wfb,LIVEMD_dmos,'type','spearman'));
cc
