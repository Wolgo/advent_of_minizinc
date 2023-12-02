% These need to be set, as we don't know how big the input will be.
int: rows;
int: cols = 3;
set of int: set_rows = 1..rows;
set of int: set_cols = 1..cols;
array[set_rows, set_cols] of int: input;
array[set_rows] of var bool: possible;

% The number of how many dice we have
int: dice;
set of int: max_dice = 1..dice;
var max_dice: red_dice;
var max_dice: blue_dice;
var max_dice: green_dice;

constraint dice = red_dice + blue_dice + green_dice;
constraint forall(i in set_rows)(possible[i] = (input[i,1] <= blue_dice /\ input[i,2] <= red_dice /\ input[i,3] <= green_dice));
constraint result = count(possible, 1);

var int: result;
solve maximize result;