% These need to be set, as we don't know how big the input will be.
int: rows;
int: cols = 3;
set of int: set_rows = 1..rows;
set of int: set_cols = 1..cols;
array[set_rows, set_cols] of int: input;

% The number of how many dice we have
var int: before_red_dice;
var int: before_blue_dice;
var int: before_green_dice;
var int: after_red_dice;
var int: after_blue_dice;
var int: after_green_dice;
set_rows: switch = 88;
var set of int: before_switch = 1..switch;
var set of int: after_switch = switch..rows;

constraint result = max(before_red_dice + before_blue_dice + before_green_dice, after_red_dice + after_green_dice + after_blue_dice);
constraint forall(i in before_switch)((input[i,1] <= before_blue_dice /\ input[i,2] <= before_red_dice /\ input[i,3] <= before_green_dice));
constraint forall(i in after_switch)((input[i,1] <= after_blue_dice /\ input[i,2] <= after_red_dice /\ input[i,3] <= after_green_dice));


var int: result;
solve minimize result;