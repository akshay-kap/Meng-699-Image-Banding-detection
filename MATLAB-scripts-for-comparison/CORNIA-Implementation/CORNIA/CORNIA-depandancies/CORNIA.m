function score = CORNIA(img, D, encoder, svm_model, svm_scale, M, P, numPatch)
% img: input image
% D: codebook, a dim-by-Dsize matrix
% encoder: type of encoder
%         - 'soft': for soft-assignment encoding described in [1]
%         - 'soft': for localized soft-assignment encoding
%         - 'hard': for hard-assignment encoding described in [2]
%         - 'sc': for sparse coding based encoding please install [3]
%         - 'llc': for locality-constrained linear coding in [4]
% svm_model: svm model obtained by svmtrain in libsvm [5]
% svm_scale: svm scaling parameter
% M, P: whitening parameters
% numPatch: number of patches extracted from each image
% references:
% [1] P. Ye, J. Kumar, L. Kang and D. Doermann, "Unsupervised Feature Learning Framework for No-reference Image Quality Assessment", IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2012. 
% [2] P. Ye and D. Doermann, "No-Reference Image Quality Assessment using Visual Codebooks", IEEE Trans. on Image Processing, vol.21, no.7, pp.3129-3138, July 2012.
% [3] SPArse Modeling Software, http://spams-devel.gforge.inria.fr/
% [4] Locality-constrained Linear Coding for Image Classification (CVPR'10), http://www.ifp.illinois.edu/~jyang29/LLC.htm
% [5] http://www.csie.ntu.edu.tw/~cjlin/libsvm/ Copyright (c) 2000-2012 Chih-Chung Chang and Chih-Jen Lin All rights reserved.
%--------------------------------------------------------------------------------

% convert to gray-scale image
if size(img,3)~=1,
    img = rgb2gray(img);
end

% patch extraction
[dim, Dsize] = size(D); % dim: dimension of local feature, Dsize: codebook size
BS = sqrt(dim);
patches = im2col(img,[BS,BS]); % one patch per column, sliding window with step size = 1
% for computation and memory problem, we perform downsampling here, sample
% 10000 patches
rng(1)
J = randperm(size(patches,2));
patches = double(patches(:,J(1:min(numPatch,length(J)))));
% normalization
patches = bsxfun(@rdivide, bsxfun(@minus, patches, mean(patches)), sqrt(var(patches)+10));
% whitening
patches = bsxfun(@minus, patches', M) * P; % one sample per row
switch encoder,
    case 'soft',
        % soft encoding
        fv = zeros(1,Dsize*2);
        fv = soft_encoding_func(D, patches);
    case 'hard', 		% to be added
        fv = zeros(1,Dsize);
        fv = hard_encoding_func(D, patches);
    case 'sc', 		
        fv = zeros(1,Dsize*2);
        fv = sc_encoding_func(D, patches, 1.0);
    case 'llc',
        fv = zeros(1,Dsize);
        fv = llc_encoding_func(D, patches);
end
fv = fv'.*svm_scale(:,1)+svm_scale(:,2);
score = svmpredict(1, fv(:)', svm_model);
end

function sc_fv = sc_encoding_func(D, fv, lambda)
% D: one codeword per column
% fv: one instance per row
D = bsxfun(@rdivide, D, sqrt(sum(D.^2)) + 1e-20);
z = sparse_codes(fv, D', lambda);
sc_fv = [max(max(z, 0)), max(-min(z, 0))];   
end

function soft_fv = soft_encoding_func(D, fv)
D = bsxfun(@rdivide, D, sqrt(sum(D.^2)) + 1e-20);
z = fv * D;
z = [max(z,0), max(-z,0)];
soft_fv = max(z);
end


function llc_fv = llc_encoding_func(D, fv)
D = bsxfun(@rdivide, D, sqrt(sum(D.^2)) + 1e-20);
z = LLC_coding_appr(D', fv); % each row is a code
llc_fv = max(z);
end


function cw_hist = hard_encoding_func(D, fv)
M = size(fv,1); % number of patches
N = size(D,2);  % number of codeword
cw_hist = zeros(1,N);
distMx = repmat(sum(D.^2),M,1)-fv*D;
for i = 1:M,
    d = min(distMx(i,:));
    idx = find(distMx==d);
    cw_hist(idx) = cw_hist(idx) + 1/length(idx);
end
end
