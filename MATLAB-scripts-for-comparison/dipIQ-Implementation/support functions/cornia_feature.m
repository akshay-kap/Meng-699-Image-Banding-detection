function fv = cornia_feature(img, seed)
% A lightweight feature extraction code of CORNIA 
% By Kede Ma Aug., 2016
%
% references:
% [1] P. Ye, J. Kumar, L. Kang and D. Doermann, "Unsupervised Feature Learning Framework for No-reference Image Quality Assessment", IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2012. 
% [2] P. Ye and D. Doermann, "No-Reference Image Quality Assessment using Visual Codebooks", IEEE Trans. on Image Processing, vol.21, no.7, pp.3129-3138, July 2012.
%--------------------------------------------------------------------------------
% load codebook
load('CSIQ_codebook_BS7.mat','codebook0');
D = codebook0;
% load whitening parameter
load('CSIQ_whitening_param.mat','M','P');
numPatch = 10000;
% convert to gray-scale image
if size(img,3)~=1,
    img = rgb2gray(img);
end
% patch extraction
[dim, Dsize] = size(D); % dim: dimension of local feature, Dsize: codebook size
BS = sqrt(dim);
patches = im2col(img,[BS, BS]); % one patch per column, sliding window with step size = 1
% for computation and memory problem, we perform downsampling here, sample
% 10000 patches
rng(seed);
J = randperm(size(patches,2));
patches = double(patches(:,J(1:min(numPatch,length(J)))));
% normalization
patches = bsxfun(@rdivide, bsxfun(@minus, patches, mean(patches)), sqrt(var(patches)+10));
% whitening
patches = bsxfun(@minus, patches', M) * P; % one sample per row
% soft encoding
fv = soft_encoding_func(D, patches);
end


function soft_fv = soft_encoding_func(D, fv)
D = bsxfun(@rdivide, D, sqrt(sum(D.^2)) + 1e-20);
z = fv * D;
z = [max(z,0), max(-z,0)];
soft_fv = max(z);
end






