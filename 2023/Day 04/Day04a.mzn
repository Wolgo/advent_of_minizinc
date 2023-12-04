% Use this editor as a MiniZinc scratch book
% These need to be set, as we don't know how big the input will be.
int: rows;
int: before;
int: after;
set of int: set_rows = 1..rows;
set of int: set_before = 1..before;
set of int: set_after = 1..after;
array[set_rows, set_before] of int: winning;
array[set_rows, set_after] of int: numbers;
array[set_rows, set_after] of var bool: matching;
array[set_rows] of var int: score;

constraint forall(i in set_rows, j in set_after)(exists(k in set_before)(winning[i,k] == numbers[i,j] /\ matching[i,j] = 1) \/ matching[i,j]=0);
constraint forall(i in set_rows)(score[i] = pow_t(2,(count(row(matching, i), 1)) - 1));

constraint result = sum(score);

var int: result;
solve maximize result;