%% Author: Vittorio Francescon
%% University of Leeds
%% Script to generate plots for the COMP5400 Coursework 1
%% Q6, plot of first 100 gens


path = "/home/vittorio/comp5400/BEASTOutputScraper/csv_outs/";
preyEND = "PREY.csv";
predatorEND = "PREDATOR.csv";

%%filename = "input from user"

preyFileA = strcat(path, s_name1, "_LONGSIM" , preyEND);
predatorFileA = strcat(path, s_name1, "_LONGSIM", predatorEND); 

preyFileB = strcat(path, s_name2, "_LONGSIM", preyEND);
predatorFileB = strcat(path, s_name2,"_LONGSIM", predatorEND); 

preyFileC = strcat(path, s_name3, "_LONGSIM", preyEND);
predatorFileC = strcat(path, s_name3, "_LONGSIM", predatorEND); 

preyFileD = strcat(path, s_name4, "_LONGSIM", preyEND);
predatorFileD = strcat(path, s_name4, "_LONGSIM", predatorEND); 

input_preyA = readtable(preyFileA);
input_predatorA = readtable(predatorFileA);

input_preyB = readtable(preyFileB);
input_predatorB = readtable(predatorFileB);

input_preyC = readtable(preyFileC);
input_predatorC = readtable(predatorFileC);

input_preyD = readtable(preyFileD);
input_predatorD = readtable(predatorFileD);


t = tiledlayout("flow");

% First Tile is for the preys
nexttile
plot(input_preyA.Generation(1:2000), input_preyA.AvgFitness(1:2000))
hold on
% plot(input_prey.Generation(1:100), input_prey.BestFitness(1:100))
plot(input_preyB.Generation(1:2000), input_preyB.AvgFitness(1:2000))
plot(input_preyC.Generation(1:2000), input_preyC.AvgFitness(1:2000))
plot(input_preyD.Generation(1:2000), input_preyD.AvgFitness(1:2000))
hold off
title('Prey Generation Count vs Fitness')
xlabel('Generation Count')
ylabel('Fitness')
legend("BKEEL", "GWRIGHT", "SMCLAUGHLIN", "VFRANC")

% Second Tile is for the predators
nexttile
plot(input_predatorA.Generation(1:2000), input_predatorA.AvgFitness(1:2000))
hold on
% plot(input_predatorA.Generation, input_predatorA.BestFitness)
plot(input_predatorB.Generation(1:2000), input_predatorB.AvgFitness(1:2000))
plot(input_predatorC.Generation(1:2000), input_predatorC.AvgFitness(1:2000))
plot(input_predatorD.Generation(1:2000), input_predatorD.AvgFitness(1:2000))
hold off
title('Predator Generation Count vs Fitness')
xlabel('Generation Count')
ylabel('Fitness')
legend("BKEEL", "GWRIGHT", "SMCLAUGHLIN", "VFRANC")

