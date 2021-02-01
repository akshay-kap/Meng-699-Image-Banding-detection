function [Es err imgrec]=arpredict_index(imgin)
imgin=double(imgin);
sr=3;%search range
mr=1;%model range
imgt=padarray(imgin,[sr+mr sr+mr],'symmetric');
imgrec=zeros(size(imgin));
[m n]=size(imgt);
N=(2*sr+1)^2-1;
K=(2*mr+1)^2-1;
A=zeros(N,K+1);

for ii=mr+sr+1:m-sr-mr
for jj=mr+sr+1:n-sr-mr
con=1;
patch0=imgt(ii-mr:ii+mr,jj-mr:jj+mr);
for iii=-sr:+sr
for jjj=-sr:+sr
if iii==0&&jjj==0
continue;
end
patch=imgt(ii+iii-mr:ii+iii+mr,jj+jjj-mr:jj+jjj+mr);
vec=patch(:);
A(con,:)=vec';
con=con+1;
end
end
b=A(:,mr*(2*mr+2)+1);
A2=A;
A2(:,mr*(2*mr+2)+1)=[];
if rcond(A2'*A2)<1e-7
a = ones(K,1)/K;
else
a = A2\b;
end
vec0=patch0(:);
vec0(mr*(2*mr+2)+1)=[];
rec=vec0'*a;
imgrec(ii-sr-mr,jj-sr-mr)=rec;
end
end
err=imgin-imgrec;
xx=-255:255;
y=round(err);

[~,ind] = sort(abs(y(:)),'descend');
thr = 0.06;
z = y(ind(1:round(thr*end)));
[nn ~]=hist(z(:),xx);
p=(1+2*nn)/sum(1+2*nn);
Es = -sum(p.*log2(p));
