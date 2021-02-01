% work flow
function fv = CORNIA_Fv(img, D, encoder, M, P, BS, numPatch)
% normalization
if size(img,3)~=1,
    img = rgb2gray(img);
end

% patch extraction
if nargin<6,
    BS = 5;
end

numBases = size(D,2);

patches = im2col(img,[BS,BS]); % one patch per column, sliding window with step size = 1

% for computation and memory problem, we perform downsampling here, sample 10000 patches
J = randperm(size(patches,2));
patches = double(patches(:,J(1:min(numPatch,length(J)))));
% normalization
patches = bsxfun(@rdivide, bsxfun(@minus, patches, mean(patches)), sqrt(var(patches)+10));
% whitening
patches = bsxfun(@minus, patches', M) * P; % one sample per row
switch encoder,
    case 'soft',
        % soft encoding
        fv = zeros(1,2*numBases);
        fv = soft_encoding_func(D, patches);
    case 'hard', 		
        fv = zeros(1,numBases);
        fv = hard_encoding_func(D, patches);
    case 'sc',
        fv = zeros(1,2*numBases);
        fv = sc_encoding_func(D, patches, 1.0);
    case 'llc',
        fv = zeros(1,numBases);
        fv = llc_encoding_func(D, patches);
end
end

function soft_fv = soft_encoding_func(D, fv)
D = bsxfun(@rdivide, D, sqrt(sum(D.^2)) + 1e-20);
z = fv * D;
z = [max(z,0), max(-z,0)];
soft_fv = max(z);
end

function sc_fv = sc_encoding_func(D, fv, lambda)
% D: one codeword per column
% fv: one instance per row
D = bsxfun(@rdivide, D, sqrt(sum(D.^2)) + 1e-20);
z = sparse_codes(fv, D', lambda);
sc_fv = [max(max(z, 0)), max(-min(z, 0))];   
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