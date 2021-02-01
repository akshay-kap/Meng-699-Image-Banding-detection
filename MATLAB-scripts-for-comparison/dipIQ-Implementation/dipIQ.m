function q = dipIQ(img, seed)
% ========================================================================
% DIP Inferred Quality Index (dipIQ)
% Version 1.0
% Copyright(c) 2016 Kede Ma, Wentao Liu, Tongliang Liu, Zhou Wang and
% Dacheng Tao
% All Rights Reserved.
%
% ----------------------------------------------------------------------
% Permission to use, copy, or modify this software and its documentation
% for educational and research purposes only and without fee is hereby
% granted, provided that this copyright notice and the original authors'
% names appear on all copies and supporting documentation. This program
% shall not be used, rewritten, or adapted as the basis of a commercial
% software or hardware product without first obtaining permission of the
% authors. The authors make no representations about the suitability of
% this software for any purpose. It is provided "as is" without express
% or implied warranty.
%----------------------------------------------------------------------
% This is an implementation of dipIQ for opinion-unaware blind image 
% quality assessment (OU-BIQA).
% Please refer to the following paper:
%
% K. Ma et al., "dipIQ: Blind Image Quality Assessment by
% Learning-to-Rank Discriminable Image Pairs" submitted to 
% IEEE Transactions on Image Processing.
%
%
% Kindly report any suggestions or corrections to k29ma@uwaterloo.ca
%
%----------------------------------------------------------------------
%
% Input : (1) img: test image.
%         (2) seed: random seed for patch selection in CORNIA feature
%                   extraction.
% Output: (1) q: quality score.
%
% Usage:
%   Given a test image img
%
%   q = dipIQ(img, 1);
%
%========================================================================
f = cornia_feature(img, seed);
load('./support functions/normalizationParaCORNIA');
f = ( f -  trainMu ) ./ trainStd; 

load ('./support functions/netPara');
paraNum = size(netPara, 2);
for i = 1 : 2 : paraNum - 2
    f = max(0, f * netPara(i).value + netPara(i+1).value');
end
q =  f * netPara(i+2).value + netPara(i+3).value';
