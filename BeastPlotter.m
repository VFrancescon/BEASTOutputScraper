%% Author: Vittorio Francescon
%% University of Leeds
%% Script to generate plots for the COMP5400 Coursework 1

input_file = readtable("output.csv");
generation = input_file.(1);
avg_fit = input_file.(2);
best_fit = input_file.(3);

plot(input_file.Generation, input_file.AvgFitness)
hold on
plot(input_file.Generation, input_file.BestFitness)
hold off

legend("Avg Fitness", "Best Fitness")