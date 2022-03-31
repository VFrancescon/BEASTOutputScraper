%% Author: Vittorio Francescon
%% University of Leeds
%% Script to generate plots for the COMP5400 Coursework 1
%% Q6, plot of first 100 gens


path = "/home/vittorio/comp5400/BEASTOutputScraper/csv_outs/";
preyEND = "PREY.csv";
predatorEND = "PREDATOR.csv";

%%filename = "input from user"

preyFileA = strcat(path, filename, "A" , preyEND);
predatorFileA = strcat(path, filename, "A", predatorEND); 

preyFileB = strcat(path, filename, "B", preyEND);
predatorFileB = strcat(path, filename,"B", predatorEND); 

preyFileC = strcat(path, filename, "C", preyEND);
predatorFileC = strcat(path, filename, "C", predatorEND); 

input_preyA = readtable(preyFileA);
input_predatorA = readtable(predatorFileA);

input_preyB = readtable(preyFileB);
input_predatorB = readtable(predatorFileB);

input_preyC = readtable(preyFileC);
input_predatorC = readtable(predatorFileC);

t = tiledlayout("flow");

% First Tile is for the preys
nexttile
plot(input_preyA.Generation, input_preyA.AvgFitness)
hold on
% plot(input_prey.Generation(1:100), input_prey.BestFitness(1:100))
plot(input_preyB.Generation, input_preyB.AvgFitness)
plot(input_preyC.Generation, input_preyC.AvgFitness)
hold off
title('Prey Generation Count vs Fitness')
xlabel('Generation Count')
ylabel('Fitness')
legend("Set A", "Set B", "Set C")

% Second Tile is for the predators
nexttile
plot(input_predatorA.Generation, input_predatorA.AvgFitness)
hold on
% plot(input_predatorA.Generation, input_predatorA.BestFitness)
plot(input_predatorB.Generation, input_predatorB.AvgFitness)
plot(input_predatorC.Generation, input_predatorC.AvgFitness)
hold off
title('Predator Generation Count vs Fitness')
xlabel('Generation Count')
ylabel('Fitness')
legend("Set A", "Set B", "Set C")

