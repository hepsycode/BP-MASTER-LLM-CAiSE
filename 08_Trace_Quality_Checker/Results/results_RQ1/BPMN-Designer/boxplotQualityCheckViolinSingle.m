tic

T_GEMINI = readtable('Quality-Checker-GEMINI.csv')
T_GPT4 = readtable('Quality-Checker-GPT4.csv')
T_GPT35 = readtable('Quality-Checker-GPT35.csv')
T_LLAMA3 = readtable('Quality-Checker-LLAMA3.csv')

T_GEMINI_Hall = readtable('Quality-Checker-Hallucination-GEMINI.csv')
T_GPT35_Hall = readtable('Quality-Checker-Hallucination-GPT35.csv')
T_GPT4_Hall = readtable('Quality-Checker-Hallucination-GPT4.csv')
T_LLAMA3_Hall = readtable('Quality-Checker-Hallucination-LLAMA3.csv')

% Hallucination
hall_4_LLAMA3 = table2array(T_LLAMA3_Hall(:,1:1))
hall_4_GPT35 = table2array(T_GPT35_Hall(:,1:1))
hall_4_GPT4 = table2array(T_GPT4_Hall(:,1:1))
hall_4_GEMINI = table2array(T_GEMINI_Hall(:,1:1))

% Levenshtein_Dist = T_GPT4{1:end,2:2}
Levenshtein_Sim_GEMINI = T_GEMINI{1:end,3:3}
Levenshtein_Sim_GPT4 = T_GPT4{1:end,3:3}
Levenshtein_Sim_GPT35 = T_GPT35{1:end,3:3}
Levenshtein_Sim_LLAMA3 = T_LLAMA3{1:end,3:3}

% LCS_Dist = T_GPT4{1:end,4:4}
LCS_Sim_GEMINI = T_GEMINI{1:end,5:5}
LCS_Sim_GPT4 = T_GPT4{1:end,5:5}
LCS_Sim_GPT35 = T_GPT35{1:end,5:5}
LCS_Sim_LLAMA3 = T_LLAMA3{1:end,5:5}

% Damerau_Levenshtein_Dist = T_GPT4{1:end,6:6}
Damerau_Levenshtein_Sim_GEMINI = T_GEMINI{1:end,6:6}
Damerau_Levenshtein_Sim_GPT4 = T_GPT4{1:end,6:6}
Damerau_Levenshtein_Sim_GPT35 = T_GPT35{1:end,6:6}
Damerau_Levenshtein_Sim_LLAMA3 = T_LLAMA3{1:end,6:6}

Jaro_Winkler_Sim_GEMINI = T_GEMINI{1:end,7:7}
Jaro_Winkler_Sim_GPT4 = T_GPT4{1:end,7:7}
Jaro_Winkler_Sim_GPT35 = T_GPT35{1:end,7:7}
Jaro_Winkler_Sim_LLAMA3 = T_LLAMA3{1:end,7:7}

% Jaccard
% jaccard_1 = T{1:end,13:13} 
% jaccard_2 = T{1:end,14:14}
% jaccard_3 = T{1:end,15:15}
jaccard_4_GEMINI = T_GEMINI{1:end,16:16}
jaccard_4_GPT4 = T_GPT4{1:end,16:16}
jaccard_4_GPT35 = T_GPT35{1:end,16:16}
jaccard_4_LLAMA3 = T_LLAMA3{1:end,16:16}

% Sorensen Dice
% sorensen_dice_1 = T{1:end,17:17} 
% sorensen_dice_2 = T{1:end,18:18}
% sorensen_dice_3 = T{1:end,19:19}
sorensen_dice_4_GEMINI = T_GEMINI{1:end,20:20}
sorensen_dice_4_GPT4 = T_GPT4{1:end,20:20}
sorensen_dice_4_GPT35 = T_GPT35{1:end,20:20}
sorensen_dice_4_LLAMA3 = T_LLAMA3{1:end,20:20}

% QGram
% qgram_1 = T{1:end,21:21} 
% qgram_2 = T{1:end,22:22}
% qgram_3 = T{1:end,23:23}
qgram_4_GEMINI = T_GEMINI{1:end,24:24}
qgram_4_GPT4 = T_GPT4{1:end,24:24}
qgram_4_GPT35 = T_GPT35{1:end,24:24}
qgram_4_LLAMA3 = T_LLAMA3{1:end,24:24}

% Cosine
% cosine_1 = T{1:end,9:9}
% cosine_2 = T{1:end,10:10}
% cosine_3 = T{1:end,11:11}
cosine_4_GEMINI = T_GEMINI{1:end,12:12}
cosine_4_GPT4 = T_GPT4{1:end,12:12}
cosine_4_GPT35 = T_GPT35{1:end,12:12}
cosine_4_LLAMA3 = T_LLAMA3{1:end,12:12}

% Levenshtein
figure
% set(gca,'xaxisLocation','top')
%tmp=get(gca,'position');
%set(gca,'position',[tmp(1) tmp(2) 0.5*tmp(3) 0.5*tmp(4)])
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
% subplot(1,8,1,'align');
% boxplot([Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [Levenshtein_Sim_LLAMA3,Levenshtein_Sim_GPT35,Levenshtein_Sim_GPT4,Levenshtein_Sim_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Levenshtein');
xtickangle(90)
ylim([0 1]);
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on


% LCS Similarity
figure
% subplot(1,8,2,'align');
% boxplot([LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [LCS_Sim_LLAMA3,LCS_Sim_GPT35,LCS_Sim_GPT4,LCS_Sim_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('LCS');
xtickangle(90)
ylim([0 1])
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Damerau-Levenshtein Similarity (Hallucination)
%subplot(2,4,3,'align');
%boxplot([Damerau_Levenshtein_Sim_LLAMA3,Damerau_Levenshtein_Sim_GPT35,Damerau_Levenshtein_Sim_GPT4,Damerau_Levenshtein_Sim_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
%xlabel('Damerau-Levenshtein');
%ylim([0 1])
%grid on


% Jaro-Winkler Similarity
figure
% subplot(1,8,3,'align');
% boxplot([Jaro_Winkler_Sim_LLAMA3,Jaro_Winkler_Sim_GPT35,Jaro_Winkler_Sim_GPT4,Jaro_Winkler_Sim_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [Jaro_Winkler_Sim_LLAMA3,Jaro_Winkler_Sim_GPT35,Jaro_Winkler_Sim_GPT4,Jaro_Winkler_Sim_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Jaro-Winkler');
xtickangle(90)
ylim([0 1])
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Jaccard Similarity
figure
% subplot(1,8,4,'align');
% boxplot([jaccard_4_LLAMA3,jaccard_4_GPT35,jaccard_4_GPT4,jaccard_4_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [jaccard_4_LLAMA3,jaccard_4_GPT35,jaccard_4_GPT4,jaccard_4_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Jaccard');
xtickangle(90)
ylim([0 1])
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Sorensen-Dice Similarity
figure
%subplot(1,8,5,'align');
% boxplot([sorensen_dice_4_LLAMA3,sorensen_dice_4_GPT35,sorensen_dice_4_GPT4,sorensen_dice_4_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [sorensen_dice_4_LLAMA3,sorensen_dice_4_GPT35,sorensen_dice_4_GPT4,sorensen_dice_4_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Dice');
xtickangle(90)
ylim([0 1])
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Q-Gram Similarity
figure
% subplot(1,8,6,'align');
% boxplot([qgram_4_LLAMA3,qgram_4_GPT35,qgram_4_GPT4,qgram_4_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [qgram_4_LLAMA3,qgram_4_GPT35,qgram_4_GPT4,qgram_4_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Q-Gram');
xtickangle(90)
ylim([0 1])
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Cosine Similarity
figure
% subplot(1,8,7,'align');
% boxplot([cosine_4_LLAMA3,cosine_4_GPT35,cosine_4_GPT4,cosine_4_GEMINI],'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [cosine_4_LLAMA3,cosine_4_GPT35,cosine_4_GPT4,cosine_4_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'}
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Cosine');
xtickangle(90)
ylim([0 1])
yticks([0 0.2 0.4 0.6 0.8 1])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

% Hallucination
figure
LLM_hall = [hall_4_LLAMA3; hall_4_GPT35; hall_4_GPT4; hall_4_GEMINI];
g = [zeros(length(hall_4_LLAMA3), 1); ones(length(hall_4_GPT35), 1); 2*ones(length(hall_4_GPT4), 1); 3*ones(length(hall_4_GEMINI), 1)];
% subplot(1,8,8,'align');
% boxplot(LLM_hall, g,'Labels',{'LLama3','GPT3.5','GPT4','Gemini'},'Whisker',0.5)
MPG = [hall_4_LLAMA3, hall_4_GPT35, hall_4_GPT4, hall_4_GEMINI];
Origin = {'LLama3','GPT3.5','GPT4','Gemini'};
Origin = cellstr(Origin);
vs = violinplot(MPG, Origin);
set(gca,'fontsize',18)
% title('Hallucination');
xtickangle(90)
ylim([0 2])
yticks([0 0.5 1 1.5 2 2.5 3 3.5 4])
set(findobj(gca,'type','line'),'linew',2);
ax = gca;
set(gca,'GridLineStyle','--');
ax.LineWidth = 1.0;
ax.GridAlpha = 0.5;
grid on

toc