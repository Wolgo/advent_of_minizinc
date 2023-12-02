% These need to be set, as we don't know how big the input will be.
int: rows;
int: cols;
set of int: set_rows = 1..rows;
set of int: set_cols = 1..cols;
array[set_rows, set_cols] of int: input;

% It's easiest to reason about the first number and the lastnumber seperately.
array [set_rows] of var int: firstNumbers;
array [set_rows] of var int: lastNumbers;

% The 0 is just there to ignore non-numbers in the problem. 
constraint forall(i in set_rows)(exists(j in set_cols)(firstNumbers[i] = input[i,j] /\ input[i,j] != 0 /\ sum(input[i, 1..j]) = input[i,j]));
constraint forall(i in set_rows)(exists(j in set_cols)(lastNumbers[i] = input[i,j] /\ input[i,j] != 0 /\ sum(input[i, j..cols]) = input[i,j])); 

% As the two numbers form a 2-digit number, the first number can simply be multiplied with 10 to achieve this.
constraint result == sum(firstNumbers) * 10 + sum(lastNumbers);

var int: result;
solve satisfy;