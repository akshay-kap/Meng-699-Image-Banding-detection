
clear;
clc;

load LIVEMD_result
cc(1) = abs(corr(LIVEMD_sisblim_sm, LIVEMD_dmos,'type','spearman'));
cc(2) = abs(corr(LIVEMD_sisblim_sfb,LIVEMD_dmos,'type','spearman'));
cc(3) = abs(corr(LIVEMD_sisblim_wm, LIVEMD_dmos,'type','spearman'));
cc(4) = abs(corr(LIVEMD_sisblim_wfb,LIVEMD_dmos,'type','spearman'));
cc

load MDID_result
cc(1) = abs(corr(MDID_sisblim_sm, MDID_dmos,'type','spearman'));
cc(2) = abs(corr(MDID_sisblim_sfb,MDID_dmos,'type','spearman'));
cc(3) = abs(corr(MDID_sisblim_wm, MDID_dmos,'type','spearman'));
cc(4) = abs(corr(MDID_sisblim_wfb,MDID_dmos,'type','spearman'));
cc
