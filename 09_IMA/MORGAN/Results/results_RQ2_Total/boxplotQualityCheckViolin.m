tic

T_Data_Total = readtable('results_RQ2.csv') % Artifacts
%T_Conn = readtable('matlab_RQ2_Connecting_objects.csv') % Connecting_Objects
%T_Flow = readtable('matlab_RQ2_Flow_Object.csv')  % Flow_Objects
%T_Swim = readtable('matlab_RQ2_Swim_Lane.csv')  % Swim_Lane

% Precision D1 attrs
Precision_D1_classes = T_Data_Total{1:45,7:7}
Precision_D1_attrs = T_Data_Total{136:180,7:7}

% Precision D2.R
Precision_D2R_classes = T_Data_Total{46:90,7:7}
Precision_D2R_attrs = T_Data_Total{181:225,7:7}

% Precision D2.S
Precision_D2S_classes = T_Data_Total{91:135,7:7}
Precision_D2S_attrs = T_Data_Total{226:270,7:7}

% Recall D1
Recall_D1_classes = T_Data_Total{1:45,8:8}
Recall_D1_attrs = T_Data_Total{136:180,8:8}

% Recall D2.R
Recall_D2R_classes = T_Data_Total{46:90,8:8}
Recall_D2R_attrs = T_Data_Total{181:225,8:8}

% Recall D2.S
Recall_D2S_classes = T_Data_Total{91:135,8:8}
Recall_D2S_attrs = T_Data_Total{226:270,8:8}

% F1 D1
F1_D1_classes = T_Data_Total{1:45,9:9}
F1_D1_attrs = T_Data_Total{136:180,9:9}

% F1 D2.R
F1_D2R_classes = T_Data_Total{46:90,9:9}
F1_D2R_attrs = T_Data_Total{181:225,9:9}

% F1 D2.S
F1_D2S_classes = T_Data_Total{91:135,9:9}
F1_D2S_attrs = T_Data_Total{226:270,9:9}

%%%%%%%%%%%%%%%%%%% PRECISION %%%%%%%%%%%%%
figure
% set(gca,'xaxisLocation','top')
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
% subplot(1,9,1,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Precision_D1_classes,Precision_D2R_classes,Precision_D2S_classes,Precision_D1_attrs,Precision_D2R_attrs,Precision_D2S_attrs];
Origin = {'D1 Classes','D2.R Classes','D2.S Classes','D1 Attrs','D2.R Attrs','D2.S Attrs'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
%pos = get(gcf, 'Position');
%set(gcf, 'Position',pos-[0 0 0 300])
set(gca,'fontsize',13)
%title('Precision');
%xtickangle(45)
xlim([0 7]);
ylim([0 100]);
% yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "outerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

%%%%%%%%%%%%%%%%%%% Recall %%%%%%%%%%%%%
figure
% set(gca,'xaxisLocation','top')
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
% subplot(1,9,1,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [Recall_D1_classes,Recall_D2R_classes,Recall_D2S_classes,Recall_D1_attrs,Recall_D2R_attrs,Recall_D2S_attrs];
Origin = {'D1 Classes','D2.R Classes','D2.S Classes','D1 Attrs','D2.R Attrs','D2.S Attrs'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
%pos = get(gcf, 'Position');
%set(gcf, 'Position',pos-[0 0 0 300])
set(gca,'fontsize',13)
%title('Precision');
%xtickangle(45)
xlim([0 7]);
ylim([0 100]);
% yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "outerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

%%%%%%%%%%%%%%%%%%% Recall %%%%%%%%%%%%%
figure
% set(gca,'xaxisLocation','top')
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
% subplot(1,9,1,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GPT4o],'Labels',{'LLama3','GPT3.5','GPT4','GPT4o'},'Whisker',0.5)
MPG = [F1_D1_classes,F1_D2R_classes,F1_D2S_classes,F1_D1_attrs,F1_D2R_attrs,F1_D2S_attrs];
Origin = {'D1 Classes','D2.R Classes','D2.S Classes','D1 Attrs','D2.R Attrs','D2.S Attrs'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
%pos = get(gcf, 'Position');
%set(gcf, 'Position',pos-[0 0 0 300])
set(gca,'fontsize',13)
%title('Precision');
%xtickangle(45)
xlim([0 7]);
ylim([0 100]);
% yticks([0 0.25 0.5 0.75 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "outerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on