%% Author: Vittorio Francescon
%% University of Leeds
%% Script to generate plots for the COMP5400 Coursework 1


%filename = "filename.csv"

input_file = readtable(filename);
generation = input_file.(1);
avg_fit = input_file.(2);
best_fit = input_file.(3);

figure
plot(input_file.Generation, input_file.AvgFitness)
hold on
plot(input_file.Generation, input_file.BestFitness)
hold off
title('Generation Count vs Fitness')
xlabel('Generation Count')
ylabel('Fitness')
legend("Avg Fitness", "Best Fitness")