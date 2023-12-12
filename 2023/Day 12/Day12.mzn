% This does not import a library from MiniZinc, it's importing a function that exists in the solver itself.
include "alldifferent.mzn";
include "disjunctive.mzn";
include "count.mzn";
include "strictly_increasing.mzn";

% Input variables
int: max_value;
int: length_groups;
int: length_measurements;
% Addition for part b: We set the max value in the group to limit search space.
array[1..length_groups] of 1..max_value: groups;
array[1..length_measurements] of 1..3: measurements;

% Decision variables, limited to only values that are possible.
array[1..length_measurements] of var 1..2: solution;
array[1..length_groups] of var 1..length_measurements: start_index;

% Either the state in the solution is the same as in the measurements, or the measurement is unclear.
constraint forall(i in 1..length_measurements)(solution[i] == measurements[i] \/ measurements[i] == 3);
% Every group starts at a index, the next index has to be at least the size of the group and a gap away.
% Also enforces that all groups are ordered.
constraint forall(i in 1..length_groups-1)(start_index[i] + groups[i] < start_index[i+1]);
% For every group, there has to be a continious range of broken machines
constraint forall(i in 1..length_groups, j in 0..(groups[i]-1))(solution[start_index[i] + j] == 2);
% For everything in the solution, either machine is working, or it's part of a group.
constraint forall(i in 1..length_measurements)(solution[i] == 1 \/ exists(j in 1..length_groups)(i >= start_index[j] /\ i < (start_index[j] + groups[j])));

% Performance with only the constraints above this line wasn't great for B. So im adding more here!
% A weaker constraint (but this can be useful for solvers!) every start index is lower than the next.
constraint forall(i in 1..length_groups-1)(start_index[i] < start_index[i+1]);
% A weaker constraint (but this can be useful for solvers!) every start index is higher than the last.
constraint forall(i in 2..length_groups)(start_index[i] > start_index[i-1]);
% An inverted constraint, Every group starts at a index, the last index has to be at least the size of the group and a gap away.
constraint forall(i in 2..length_groups)(start_index[i] - groups[i-1] > start_index[i-1]);
% If it's in the start_index list its broken;
constraint forall(i in 1..length_groups)(solution[start_index[i]] == 2);
% All start_index values are different.
constraint alldifferent(start_index);
% Every machine before the first group is working
constraint forall(i in 1..start_index[1] where i < start_index[1])(solution[i] == 1); 
% Every machine before a group is working
constraint forall(i in 1..length_groups where start_index[i] > 1)(solution[start_index[i] - 1] == 1); 
% Every machine after a group is working (except the last group, as that might be out of bounds.)
constraint forall(i in 1..(length_groups-1))(solution[(start_index[i] + groups[i])] == 1); 
% Do not allow overlap between groups. I don't think this helps.
constraint forall(i in 1..length_groups)(disjunctive([start_index[i]], [groups[i]]));
% There should be exactly the amount of broken machines as there is indicated in groups
constraint count(solution, 2, sum(groups));
% There should be exactly the amount of working machiens as there is indicated in groups
constraint count(solution, 1, (length_measurements - sum(groups)));
constraint strictly_increasing(start_index);
% These should be pretty strong in limiting the constraints. I got out of bed to add them.
% Essentially, the start index is at least later or earlier than all groups after or before.
constraint forall(i in 2..length_groups)(start_index[i] >= i + sum([x in groups | x in 1..i]));
constraint forall(i in 1..(length_groups-1))(start_index[i] <= length_measurements - sum([x in groups | x in i..length_measurements]) - (length_groups - i));

% Solve to satisfy the constraints. 
solve satisfy;




