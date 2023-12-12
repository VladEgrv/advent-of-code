input_adress = 'print_your_adress'

class InputTransformer:
    """the class transforms the input into the chosen form"""
    def __init__(self):
        pass
    
    def input_to_separate_lists(input_adress):
        with open(input_adress, 'r') as file:
            lines = file.readlines()
        times = [int(num) for num in lines[0].split() if num.isdigit()]
        distances = [int(num) for num in lines[1].split() if num.isdigit()]
        return times, distances

    def input_to_dictionary(input_adress):
        times, distances = InputTransformer.input_to_separate_lists(input_adress)
        input_in_dict = dict(zip(times, distances))
        print(times, distances, input_in_dict)
        return input_in_dict
    
    def input_to_lists(input_adress):
        times, distances = InputTransformer.input_to_separate_lists(input_adress)
        input_in_list = [ [ x, y ] for x, y in zip(times, distances)]
        print(input_in_list)
        return input_in_list
    
    def input_to_total_race(input_adress):
        times, distances = InputTransformer.input_to_separate_lists(input_adress)
        total_time = int(''.join(str(i) for i in times))
        total_distance = int(''.join(str(i) for i in distances))
        return total_time, total_distance
    

def count_ways_to_win_part_1(times, distances):
    counter = 1
    for i in range(0, len(times)):
        temp_counter = 0
        for hold_time in range(0, times[i]):
            speed = hold_time
            travel_time =  times[i] - hold_time
            race_distance = speed * travel_time
            if race_distance > distances[i]:
                temp_counter += 1
        counter *= temp_counter
    print(counter)

def count_ways_to_win_part_2(total_time, total_distance):
    counter = 0
    for hold_time in range(0, total_time):
        speed = hold_time
        travel_time =  total_time - hold_time
        race_distance = speed * travel_time
        if race_distance > total_distance:
            counter += 1
    print(counter)
        

times, distances = InputTransformer.input_to_separate_lists(input_adress)
total_time, total_distance = InputTransformer.input_to_total_race(input_adress)
count_ways_to_win_part_1(times, distances)
count_ways_to_win_part_2(total_time, total_distance)
