function [svm_model, svm_scale_param] = CORNIA_train(dataTrain, dmos)
% dataTrain: N-by-M matrix, each column consisting of one traning sample, N:dimension of feature, M:number of samples
% dmos: true quality scores for training samples
% scaling
% please install libsvm 

[dataTrain, s1, s2] = scaling_func(dataTrain);
% training
model{ii} = svmtrain(dmos(:), dataTrain', '-s 4 -t 0 -c 1 -n 0.5');
scale_param{ii} = [s1, s2];
% testing on trianing set
% [pred_score, ~, ~] = svmpredict(dmos(:),dataTrain', model{ii});
% corr_pearson = corr(dmos(:),pred_score(:),'type','Pearson')
% corr_spearman = corr(dmos(:),pred_score(:),'type','Spearman')
% get training model and scaling parameters
svm_model = model{2};
svm_scale_param = scale_param{2};

function [fvScale,s1,s2] = scaling_func(data_train)
% Find scaling parameter for each dimension

[N, M] = size(data_train);
fvScale = zeros(N,M);
% scale feature value along each dimenstion to the range [-1,1]
s1 = zeros(N,1);
s2 = zeros(N,1);
for i = 1:N,
    row = data_train(i,:);
    dmax = max(row);
    dmin = min(row);
    % find k, b such that: 1 = k*dmax+b -1 = k*dmin+b
    % if dmax=dmin => k=0,b=0;
    if dmax==dmin,
        k = 0;
        b = 0;
    else
        k = 2/(dmax-dmin);
        b = 1-k*dmax;
    end
    fvScale(i,:) = k*data_train(i,:)+b;
    s1(i) = k;
    s2(i) = b;
end
