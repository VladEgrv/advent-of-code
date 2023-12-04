'''in each game you played, what is the fewest number of cubes
of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. 
If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, 
and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. 
In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?'''

with open('d:\\python\\AOC_input_2.txt', 'r') as file:
    raw_game_list = file.readlines()

counter = 0
map_game_list = {}

def raw_to_map(raw_game_list, map_game_list):
    for string_with_game in raw_game_list:
        num_of_game = int(string_with_game[string_with_game.find(' '):string_with_game.find(':')])
        rounds_of_game = string_with_game[string_with_game.find(':') + 1:].split(";")
        game_list = []
        for round_data in rounds_of_game:
            round_data = round_data.strip()
            round_dict = {}
            colors_data = round_data.split(", ")
            for color_info in colors_data:
                count, color = color_info.split()
                round_dict[color] = int(count)
            game_list.append(round_dict)
        map_game_list[num_of_game] = game_list
    return map_game_list

raw_to_map(raw_game_list, map_game_list)

for key, value in map_game_list.items():
    minimum_set = {'red' : 1, 'green' : 1, 'blue' : 1}
    for run_of_game in value:
        temp_count = 1
        for colour, num in run_of_game.items():
            if colour in minimum_set and minimum_set[colour] < num:
                minimum_set[colour] = num
        for colour, num in minimum_set.items():
            temp_count *= num
    counter += temp_count
print(counter)