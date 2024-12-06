tic

T_Artifacts = readtable('matlab_RQ2_Artifacts.csv') % Artifacts
T_Conn = readtable('matlab_RQ2_Connecting_objects.csv') % Connecting_Objects
T_Flow = readtable('matlab_RQ2_Flow_Object.csv')  % Flow_Objects
T_Swim = readtable('matlab_RQ2_Swim_Lane.csv')  % Swim_Lane

% Precision D1
Precision_D1_Artifacts = T_Artifacts{1:end,6:6}
Precision_D1_Conn = T_Conn{1:end,6:6}
Precision_D1_Flow = T_Flow{1:end,6:6}
Precision_D1_Swim = T_Swim{1:end,6:6}

% Precision D2.R
Precision_D2R_Artifacts = T_Artifacts{1:end,15:15}
Precision_D2R_Conn = T_Conn{1:end,15:15}
Precision_D2R_Flow = T_Flow{1:end,15:15}
Precision_D2R_Swim = T_Swim{1:end,15:15}

% Precision D2.S
Precision_D2S_Artifacts = T_Artifacts{1:end,24:24}
Precision_D2S_Conn = T_Conn{1:end,24:24}
Precision_D2S_Flow = T_Flow{1:end,24:24}
Precision_D2S_Swim = T_Swim{1:end,24:24}

% Recall D1
Recall_D1_Artifacts = T_Artifacts{1:end,7:7}
Recall_D1_Conn = T_Conn{1:end,7:7}
Recall_D1_Flow = T_Flow{1:end,7:7}
Recall_D1_Swim = T_Swim{1:end,7:7}

% Recall D2.R
Recall_D2R_Artifacts = T_Artifacts{1:end,16:16}
Recall_D2R_Conn = T_Conn{1:end,16:16}
Recall_D2R_Flow = T_Flow{1:end,16:16}
Recall_D2R_Swim = T_Swim{1:end,16:16}

% Recall D2.S
Recall_D2S_Artifacts = T_Artifacts{1:end,25:25}
Recall_D2S_Conn = T_Conn{1:end,25:25}
Recall_D2S_Flow = T_Flow{1:end,25:25}
Recall_D2S_Swim = T_Swim{1:end,25:25}

% F1 D1
F1_D1_Artifacts = T_Artifacts{1:end,8:8}
F1_D1_Conn = T_Conn{1:end,8:8}
F1_D1_Flow = T_Flow{1:end,8:8}
F1_D1_Swim = T_Swim{1:end,8:8}

% F1 D2.R
F1_D2R_Artifacts = T_Artifacts{1:end,17:17}
F1_D2R_Conn = T_Conn{1:end,17:17}
F1_D2R_Flow = T_Flow{1:end,17:17}
F1_D2R_Swim = T_Swim{1:end,17:17}

% F1 D2.S
F1_D2S_Artifacts = T_Artifacts{1:end,26:26}
F1_D2S_Conn = T_Conn{1:end,26:26}
F1_D2S_Flow = T_Flow{1:end,26:26}
F1_D2S_Swim = T_Swim{1:end,26:26}

%%%%%%%%%%%%%%%%%%% PRECISION %%%%%%%%%%%%%
figure
set(gca,'xaxisLocation','top')
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
subplot(1,9,1,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Precision_D1_Artifacts,Precision_D1_Conn,Precision_D1_Flow,Precision_D1_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
%pos = get(gcf, 'Position');
%set(gcf, 'Position',pos-[0 0 0 300])
set(gca,'fontsize',10)
title('D1 - Precision');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
% yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Precision D2.R
subplot(1,9,2,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Precision_D2R_Artifacts,Precision_D2R_Conn,Precision_D2R_Flow,Precision_D2R_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',10)
title('D2.R - Precision');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

subplot(1,9,3,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Precision_D2S_Artifacts,Precision_D2S_Conn,Precision_D2S_Flow,Precision_D2S_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',10)
title('D2.S - Precision');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

%%%%%%%%%%%%%%%%%%% Recall %%%%%%%%%%%%%
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
subplot(1,9,4,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Recall_D1_Artifacts,Recall_D1_Conn,Recall_D1_Flow,Recall_D1_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
%pos = get(gcf, 'Position');
%set(gcf, 'Position',pos-[0 0 0 300])
set(gca,'fontsize',10)
title('D1 - Recall');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Precision D2.R
subplot(1,9,5,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Recall_D2R_Artifacts,Recall_D2R_Conn,Recall_D2R_Flow,Recall_D2R_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',10)
title('D2.R - Recall');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

subplot(1,9,6,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Recall_D2S_Artifacts,Recall_D2S_Conn,Recall_D2S_Flow,Recall_D2S_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',10)
title('D2.S - Recall');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

%%%%%%%%%%%%%%%%%%% F1 %%%%%%%%%%%%%
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
subplot(1,9,7,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [F1_D1_Artifacts,F1_D1_Conn,F1_D1_Flow,F1_D1_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
%pos = get(gcf, 'Position');
%set(gcf, 'Position',pos-[0 0 0 300])
set(gca,'fontsize',10)
title('D1 - F1');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Precision D2.R
subplot(1,9,8,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [F1_D2R_Artifacts,F1_D2R_Conn,F1_D2R_Flow,F1_D2R_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',10)
title('D2.R - F1');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

subplot(1,9,9,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [F1_D2S_Artifacts,F1_D2S_Conn,F1_D2S_Flow,F1_D2S_Swim];
Origin = {'A','C','F','S'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',10)
title('D2.S - F1');
%xtickangle(45)
xlim([0 5]);
ylim([0 100]);
%yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on