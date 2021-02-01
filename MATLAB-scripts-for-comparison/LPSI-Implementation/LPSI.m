function [ score ] = LPSI( varargin )
%WLBP Summary of this function goes here
%   Detailed explanation goes here
narginchk(1,3);

image=varargin{1};
[h,w,ch]=size(image);
if ch>1
    image=double(rgb2gray(image));
else
    image=double(image);
end
a=mapminmax(image(:)',0,1);
d_image=reshape(a,h,w);
image=d_image;

if nargin==1
    spoints=[-1 -1; -1 0; -1 1; 0 -1; -0 1; 1 -1; 1 0; 1 1];
    neighbors=8;
end

if (nargin == 2) && (length(varargin{2}) == 1)
    error('Input arguments');
end

if (nargin > 2) && (length(varargin{2}) == 1)
    radius=varargin{2};
    neighbors=varargin{3};
    
    spoints=zeros(neighbors,2);

    % Angle step.
    a = 2*pi/neighbors;
    
    for i = 1:neighbors
        spoints(i,1) = -radius*sin((i-1)*a);
        spoints(i,2) = radius*cos((i-1)*a);
    end
end

if (nargin > 1) && (length(varargin{2}) > 1)
    spoints=varargin{2};
    neighbors=size(spoints,1);
end

% Determine the dimensions of the input image.
[ysize,xsize] = size(image);
miny=min(spoints(:,1));
maxy=max(spoints(:,1));
minx=min(spoints(:,2));
maxx=max(spoints(:,2));

% Block size, each LBP code is computed within a block of size bsizey*bsizex
bsizey=ceil(max(maxy,0))-floor(min(miny,0))+1;
bsizex=ceil(max(maxx,0))-floor(min(minx,0))+1;

% Coordinates of origin (0,0) in the block
origy=1-floor(min(miny,0));
origx=1-floor(min(minx,0));

% Minimum allowed size for the input image depends
% on the radius of the used LBP operator.
if(xsize < bsizex || ysize < bsizey)
  error('Too small input image. Should be at least (2*radius+1) x (2*radius+1)');
end

% Calculate dx and dy;
dx = xsize - bsizex;
dy = ysize - bsizey;

% Fill the center pixel matrix C.
C = image(origy:origy+dy,origx:origx+dx);
d_C = double(C);

% Initialize the result matrix with zeros.
CLBP_S=zeros(dy+1,dx+1);

%Compute the LBP code image
D=cell(neighbors,1);
for i = 1:neighbors
  y = spoints(i,1)+origy;
  x = spoints(i,2)+origx;
  % Calculate floors, ceils and rounds for the x and y.
  fy = floor(y); cy = ceil(y); ry = round(y);
  fx = floor(x); cx = ceil(x); rx = round(x);
  % Check if interpolation is needed.
  if (abs(x - rx) < 1e-6) && (abs(y - ry) < 1e-6)
    % Interpolation is not needed, use original datatypes
    N = d_image(ry:ry+dy,rx:rx+dx);
    D{i} = N >= d_C;   
  else
    % Interpolation needed, use double type images 
    ty = y - fy;
    tx = x - fx;

    % Calculate the interpolation weights.
    w1 = (1 - tx) * (1 - ty);
    w2 =      tx  * (1 - ty);
    w3 = (1 - tx) *      ty ;
    w4 =      tx  *      ty ;
    % Compute interpolated pixel values
    N = w1*d_image(fy:fy+dy,fx:fx+dx) + w2*d_image(fy:fy+dy,cx:cx+dx) + ...
        w3*d_image(cy:cy+dy,fx:fx+dx) + w4*d_image(cy:cy+dy,cx:cx+dx);
    D{i} = N >= d_C;     
  end  
end
% compute CLBP_S and CLBP_M
for i=1:neighbors
  % Update the result matrix.
  CLBP_S = CLBP_S + D{i};
end
lbp_map = CLBP_S == 0;
% compute local variance
c = 2e-4;
alpha = 5;
if neighbors==8
    h = fspecial('average',[3,3]);
elseif neighbors==4
    h = [0 1 0;1 1 1;0 1 0];
end
h = h/sum(sum(h));
mu = filter2(h,d_image,'valid');
mu_sq = mu.*mu;
weight = abs(filter2(h, d_image.*d_image, 'valid') - mu_sq);
weight = weight + ones(size(lbp_map))*c; 
score = sum(sum(lbp_map./weight))/length(lbp_map(:)); 
score = score/(score+alpha);

end