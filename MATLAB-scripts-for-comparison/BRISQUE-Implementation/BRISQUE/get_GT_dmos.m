function [ refined_dmos,refined_order ] = get_GT_dmos( org_dmos,dis_pos,dis_num )
%GET_GT_DMOS Summary of this function goes here
%   Detailed explanation goes here
refined_dmos=cell(5,1);
refined_order=cell(5,1);
for i=1:5
    curr_dmos=org_dmos(dis_pos(i):dis_pos(i)+dis_num(i)-1)';
    refined_dmos{i}=curr_dmos(curr_dmos~=0);
    [~,idx]=sort(refined_dmos{i},'ascend');
    temp=zeros(length(idx),1);
    temp(idx)=(1:length(idx))';
    refined_order{i}=temp;
end

end

