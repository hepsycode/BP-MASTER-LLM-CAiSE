tic

T_GOT4o_Hall = readtable('Hallucination-GPT4o_first_word.csv')
T_GPT35_Hall = readtable('Hallucination-GPT3.5_first_word.csv')
T_GPT4_Hall = readtable('Hallucination-GPT4_first_word.csv')
T_LLAMA3_Hall = readtable('Hallucination-LLAMA3-70B_first_word.csv')
T_MISTRAL_Hall = readtable('Hallucination-Mistral-Large_first_word.csv')

% Hallucination
hall_4_MISTRAL = table2array(T_MISTRAL_Hall(:,5:5))
hall_4_LLAMA3 = table2array(T_LLAMA3_Hall(:,5:5))
hall_4_GPT35 = table2array(T_GPT35_Hall(:,5:5))
hall_4_GPT4 = table2array(T_GPT4_Hall(:,5:5))
hall_4_GOT4o = table2array(T_GOT4o_Hall(:,5:5))

figure
set(gca,'xaxisLocation','top')

% Hallucination
subplot(1,4,1,'align');
LLM_hall = [hall_4_MISTRAL; hall_4_LLAMA3; hall_4_GPT35; hall_4_GPT4; hall_4_GOT4o];
g = [zeros(length(hall_4_MISTRAL), 1); ones(length(hall_4_LLAMA3), 1); 2*ones(length(hall_4_GPT35), 1); 3*ones(length(hall_4_GPT4), 1); 4*ones(length(hall_4_GOT4o), 1)];
% boxplot(LLM_hall, g,'Labels',{'LLama3','GPT-3.5','GPT-4','GPT-4o'},'Whisker',0.5)
MPG = [hall_4_MISTRAL, hall_4_LLAMA3, hall_4_GPT35, hall_4_GPT4, hall_4_GOT4o];
Origin = {'Mistral','LLama3','GPT-3.5','GPT-4','GPT-4o'};
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',12)
title('Total Events');
xlim([0 6]);
xtickangle(45)
ylim([0 4])
% yticks([0 0.5 1 1.5 2 2.5 3 3.5 4])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

T_GOT4o_Hall_Sec = readtable('Hallucination-GPT4o_second_word.csv')
T_GPT35_Hall_Sec = readtable('Hallucination-GPT3.5_second_word.csv')
T_GPT4_Hall_Sec = readtable('Hallucination-GPT4_second_word.csv')
T_LLAMA3_Hall_Sec = readtable('Hallucination-LLAMA3-70B_second_word.csv')
T_MISTRAL_Hall_Sec = readtable('Hallucination-Mistral-Large_second_word.csv')

% Hallucination
hall_4_MISTRAL_Sec = table2array(T_MISTRAL_Hall_Sec(:,4:4))
hall_4_LLAMA3_Sec = table2array(T_LLAMA3_Hall_Sec(:,4:4))
hall_4_GPT35_Sec = table2array(T_GPT35_Hall_Sec(:,4:4))
hall_4_GPT4_Sec = table2array(T_GPT4_Hall_Sec(:,4:4))
hall_4_GOT4o_Sec = table2array(T_GOT4o_Hall_Sec(:,4:4))

% Hallucination
subplot(1,4,2,'align');
LLM_hall = [hall_4_MISTRAL_Sec; hall_4_LLAMA3_Sec; hall_4_GPT35_Sec; hall_4_GPT4_Sec; hall_4_GOT4o_Sec];
g = [zeros(length(hall_4_MISTRAL_Sec), 1); ones(length(hall_4_LLAMA3_Sec), 1); 2*ones(length(hall_4_GPT35_Sec), 1); 3*ones(length(hall_4_GPT4_Sec), 1); 4*ones(length(hall_4_GOT4o_Sec), 1)];
% boxplot(LLM_hall, g,'Labels',{'LLama3','GPT-3.5','GPT-4','GPT-4o'},'Whisker',0.5)
MPG = [hall_4_MISTRAL_Sec, hall_4_LLAMA3_Sec, hall_4_GPT35_Sec, hall_4_GPT4_Sec, hall_4_GOT4o_Sec];
Origin = {'Mistral','LLama3','GPT-3.5','GPT-4','GPT-4o'};
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',12)
title('Classes');
xlim([0 6]);
xtickangle(45)
ylim([0 4])
% yticks([0 0.5 1 1.5 2 2.5 3 3.5 4])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

T_GOT4o_Hall_Class = readtable('Hallucination-GPT4o_third_word.csv')
T_GPT35_Hall_Class = readtable('Hallucination-GPT3.5_third_word.csv')
T_GPT4_Hall_Class = readtable('Hallucination-GPT4_third_word.csv')
T_LLAMA3_Hall_Class = readtable('Hallucination-LLAMA3-70B_third_word.csv')
T_MISTRAL_Hall_Class = readtable('Hallucination-Mistral-Large_third_word.csv')

% Hallucination
hall_4_MISTRAL_Class = table2array(T_MISTRAL_Hall_Class(:,4:4))
hall_4_LLAMA3_Class = table2array(T_LLAMA3_Hall_Class(:,4:4))
hall_4_GPT35_Class = table2array(T_GPT35_Hall_Class(:,4:4))
hall_4_GPT4_Class = table2array(T_GPT4_Hall_Class(:,4:4))
hall_4_GOT4o_Class = table2array(T_GOT4o_Hall_Class(:,4:4))

% Hallucination
subplot(1,4,3,'align');
LLM_hall = [hall_4_MISTRAL_Class; hall_4_LLAMA3_Class; hall_4_GPT35_Class; hall_4_GPT4_Class; hall_4_GOT4o_Class];
g = [zeros(length(hall_4_MISTRAL_Class), 1); ones(length(hall_4_LLAMA3_Class), 1); 2*ones(length(hall_4_GPT35_Class), 1); 3*ones(length(hall_4_GPT4_Class), 1); 4*ones(length(hall_4_GOT4o_Class), 1)];
% boxplot(LLM_hall, g,'Labels',{'LLama3','GPT-3.5','GPT-4','GPT-4o'},'Whisker',0.5)
MPG = [hall_4_MISTRAL_Class, hall_4_LLAMA3_Class, hall_4_GPT35_Class, hall_4_GPT4_Class, hall_4_GOT4o_Class];
Origin = {'Mistral','LLama3','GPT-3.5','GPT-4','GPT-4o'};
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',12)
title('Attributes');
xlim([0 6]);
xtickangle(45)
ylim([0 4])
% yticks([0 0.5 1 1.5 2 2.5 3 3.5 4])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

T_GOT4o_Hall_Attrs = readtable('Hallucination-GPT4o_fourth_word.csv')
T_GPT35_Hall_Attrs = readtable('Hallucination-GPT3.5_fourth_word.csv')
T_GPT4_Hall_Attrs = readtable('Hallucination-GPT4_fourth_word.csv')
T_LLAMA3_Hall_Attrs = readtable('Hallucination-LLAMA3-70B_fourth_word.csv')
T_MISTRAL_Hall_Class = readtable('Hallucination-Mistral-Large_fourth_word.csv')

% Hallucination
hall_4_MISTRAL_Attrs = table2array(T_MISTRAL_Hall_Class(:,4:4))
hall_4_LLAMA3_Attrs = table2array(T_LLAMA3_Hall_Attrs(:,4:4))
hall_4_GPT35_Attrs = table2array(T_GPT35_Hall_Attrs(:,4:4))
hall_4_GPT4_Attrs = table2array(T_GPT4_Hall_Attrs(:,4:4))
hall_4_GOT4o_Attrs = table2array(T_GOT4o_Hall_Attrs(:,4:4))

% Hallucination
subplot(1,4,4,'align');
LLM_hall = [hall_4_MISTRAL_Attrs; hall_4_LLAMA3_Attrs; hall_4_GPT35_Attrs; hall_4_GPT4_Attrs; hall_4_GOT4o_Attrs];
g = [zeros(length(hall_4_MISTRAL_Attrs), 1); ones(length(hall_4_LLAMA3_Attrs), 1); 2*ones(length(hall_4_GPT35_Attrs), 1); 3*ones(length(hall_4_GPT4_Attrs), 1); 4*ones(length(hall_4_GOT4o_Attrs), 1)];
% boxplot(LLM_hall, g,'Labels',{'LLama3','GPT-3.5','GPT-4','GPT-4o'},'Whisker',0.5)
MPG = [hall_4_MISTRAL_Attrs, hall_4_LLAMA3_Attrs, hall_4_GPT35_Attrs, hall_4_GPT4_Attrs, hall_4_GOT4o_Attrs];
Origin = {'Mistral','LLama3','GPT-3.5','GPT-4','GPT-4o'};
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',12)
title('ADD/SET');
xlim([0 6]);
xtickangle(45)
ylim([0 4])
% yticks([0 0.5 1 1.5 2 2.5 3 3.5 4])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
ax.PositionConstraint = "innerposition";
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

toc