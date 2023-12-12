% Use this editor as a MiniZinc scratch book
% These need to be set, as we don't know how big the input will be.
int: seed_length;
array[1..seed_length] of int: seeds;
int: seed_to_soil_length;
array[1..seed_to_soil_length, 1..3] of int: seed_to_soil;
int: soil_to_fertilizer_length;
array[1..soil_to_fertilizer_length, 1..3] of int: soil_to_fertilizer;
int: fertilizer_to_water_length;
array[1..fertilizer_to_water_length, 1..3] of int: fertilizer_to_water;
int: water_to_light_length;
array[1..water_to_light_length, 1..3] of int: water_to_light;
int: light_to_temperature_length;
array[1..light_to_temperature_length, 1..3] of int: light_to_temperature;
int: temperature_to_humidity_length;
array[1..temperature_to_humidity_length, 1..3] of int: temperature_to_humidity;
int: humidity_to_location_length;
array[1..humidity_to_location_length, 1..3] of int: humidity_to_location;

set of int: seed_choices = 1..seed_length;
var 0..1000000000000: seed;
var 0..1000000000000: soil;
var 0..1000000000000: fertilizer;
var 0..1000000000000: water;
var 0..1000000000000: light;
var 0..1000000000000: temperature;
var 0..1000000000000: humidity;
var 0..1000000000000: location;

constraint exists(i in seed_choices)(seed = seeds[i]);
constraint exists(i in 1..seed_to_soil_length)(seed_to_soil[i, 2] < seed /\ seed < (seed_to_soil[i, 2] + seed_to_soil[i, 3]) /\ soil = seed_to_soil[i, 1] + seed - seed_to_soil[i, 2])
\/ (forall(i in 1..seed_to_soil_length)((seed_to_soil[i, 2] > seed \/ seed > (seed_to_soil[i, 2] + seed_to_soil[i, 3])) /\ soil = seed));

constraint exists(i in 1..soil_to_fertilizer_length)(soil_to_fertilizer[i, 2] < soil /\ soil < (soil_to_fertilizer[i, 2] + soil_to_fertilizer[i, 3]) /\ fertilizer = soil_to_fertilizer[i, 1] + soil - soil_to_fertilizer[i, 2])
\/ (forall(i in 1..soil_to_fertilizer_length)((soil_to_fertilizer[i, 2] > soil \/ soil > (soil_to_fertilizer[i, 2] + soil_to_fertilizer[i, 3])) /\ fertilizer = soil));

constraint exists(i in 1..fertilizer_to_water_length)(fertilizer_to_water[i, 2] < fertilizer /\ fertilizer < (fertilizer_to_water[i, 2] + fertilizer_to_water[i, 3]) /\ water = fertilizer_to_water[i, 1] + fertilizer - fertilizer_to_water[i, 2])
\/ (forall(i in 1..fertilizer_to_water_length)((fertilizer_to_water[i, 2] > fertilizer \/ fertilizer > (fertilizer_to_water[i, 2] + fertilizer_to_water[i, 3])) /\ water = fertilizer));

constraint exists(i in 1..water_to_light_length)(water_to_light[i, 2] < water /\ water < (water_to_light[i, 2] + water_to_light[i, 3]) /\ light = water_to_light[i, 1] + water - water_to_light[i, 2])
\/ (forall(i in 1..water_to_light_length)((water_to_light[i, 2] > water \/ water > (water_to_light[i, 2] + water_to_light[i, 3])) /\ light = water));

constraint exists(i in 1..light_to_temperature_length)(light_to_temperature[i, 2] < light /\ light < (light_to_temperature[i, 2] + light_to_temperature[i, 3]) /\ temperature = light_to_temperature[i, 1] + light - light_to_temperature[i, 2])
\/ (forall(i in 1..light_to_temperature_length)((light_to_temperature[i, 2] > light \/ light > (light_to_temperature[i, 2] + light_to_temperature[i, 3])) /\ temperature = light));

constraint exists(i in 1..temperature_to_humidity_length)(temperature_to_humidity[i, 2] < temperature /\ temperature < (temperature_to_humidity[i, 2] + temperature_to_humidity[i, 3]) /\ humidity = temperature_to_humidity[i, 1] + temperature - temperature_to_humidity[i, 2])
\/ (forall(i in 1..temperature_to_humidity_length)((temperature_to_humidity[i, 2] > temperature \/ temperature > (temperature_to_humidity[i, 2] + temperature_to_humidity[i, 3])) /\ humidity = temperature));

constraint exists(i in 1..humidity_to_location_length)(humidity_to_location[i, 2] < humidity /\ humidity < (humidity_to_location[i, 2] + humidity_to_location[i, 3]) /\ location = humidity_to_location[i, 1] + humidity - humidity_to_location[i, 2])
\/ (forall(i in 1..humidity_to_location_length)((humidity_to_location[i, 2] > humidity \/ humidity > (humidity_to_location[i, 2] + humidity_to_location[i, 3])) /\ location = humidity));

solve minimize location;