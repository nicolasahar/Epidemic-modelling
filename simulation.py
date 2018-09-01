##PART 1 - Dijkstra Starter ##

import os
import numpy

os.chdir("/Users/nicolasahar/Desktop/ECs/2015-2016/Computing for Medicine (Apr 2016)/Assignments/Assignment 2 (due July 29)/Project Outline")

# Exercise 4 - Part 5
def process_line(line):
    list = []
    colon_index = 0

    for i in range(len(line)):
        if line[i] == ":":
            city1 = line[:i]
            list.append(city1)
            colon_index = i

        elif line[i] == " " and line[i + 1].isdigit():
            city2 = line[colon_index + 1:i]
            list.append(city2)

            distance = int(line[i + 1:(len(line) + 1)])
            list.append(distance)
        if len(list) == 3:
            break

    return tuple(list)

# Exercise 4 - Part 4
# Note: deleted starter function "get_distances" as it was the same as same as 'build_distances". If need it, donwload original starter code.
def build_distances(lines):
    dict = {}

    for line in lines:

        processed_line = process_line(line)  # call the helper function "process_line" on all lines
        city1 = processed_line[0]
        city2 = processed_line[1]
        distance = processed_line[2]

        if city1 not in dict:
            dict[city1] = [tuple([city2, distance])]

            if city2 not in dict:
                dict[city2] = [tuple([city1, distance])]
            else:
                dict[city2].append(tuple([city1, distance]))

        else:
            dict[city1].append(tuple([city2, distance]))

            if city2 not in dict:
                dict[city2] = [tuple([city1, distance])]
            else:
                dict[city2].append(tuple([city1, distance]))

    for key in dict:
        alphabetical_list = sorted(dict[key])
        dict[key] = alphabetical_list

    return dict

# actual = print(build_distances(['Toronto:New York 3\n', 'New York:Washington 2\n','Washington:San Francisco 5\n', 'San Francisco:Mexico City 3\n','Toronto:Mexico City 7\n', 'Toronto:San Francisco 6\n']))
# result = {'Mexico City': [('San Francisco', 3), ('Toronto', 7)], 'New York': [('Toronto', 3), ('Washington', 2)], 'San Francisco': [('Mexico City', 3), ('Toronto', 6), ('Washington', 5)], 'Toronto': [('Mexico City', 7), ('New York', 3), ('San Francisco', 6)], 'Washington': [('New York', 2), ('San Francisco', 5)]}
# print(actual == result)

# Exercise 4 - Part 1
def get_closest(unvisited):
    closest = None
    index_closest = None

    for i in range(len(unvisited)):
        if i == 0:
            closest = unvisited[0][1]
            index_closest = 0
        elif unvisited[i][1] < closest:
            closest = unvisited[i][1]
            index_closest = i

    return unvisited[index_closest]

# Exercise 4 - Part 2
def find_city(city, city_list):
    for i in range(len(city_list)):
        if city_list[i][0] == city:
            return i
            break

    return -1

# Exercise 5 - Markus (use E5_Tester)
def visit_next(visited, unvisited, distances):
    # move next closest city from unvisited list to visited list
    closest_city_val = unvisited[0][1]
    closest_city_ind = 0

    for i in range(len(unvisited)):
        # if unvisited[i][1] == 0: # this is not needed, as the first city in unvisted when it is first called will be the destination city (index = 0) at distance 0 (which is already represented in the starting states of the two variables above)
        # closest_city_val = unvisited[i][1]
        # closest_city_ind = i

        if unvisited[i][1] < closest_city_val:
            closest_city_val = unvisited[i][1]
            closest_city_ind = i

    visited.append(unvisited[closest_city_ind])
    unvisited.pop(closest_city_ind)

    # add the neighbours of the city you moved to the unvisited list and update their distances
    neighbour_list = distances[visited[len(visited) - 1][
        0]]  # 1. access the last item in visited (will be the city you just moved (the closest one)) - you need -1 for this; 2. for this city, retrieve all of its neighbours from distance dict
    dist_closest_city_destination = visited[len(visited) - 1][1]

    tuple_to_list = [list(x) for x in
                     neighbour_list]  # problem is that i'm trying to change tuple; need to convert to list then change back to tuple

    for neighbour_city in tuple_to_list:  # looping through each neighbour and considering the 3 cases
        if neighbour_city[0] in [x[0] for x in
                                 visited]:  # if we've already visited that city, we've already found the shortest distance of that city to the destination city, so dont need to add to unvisited and/or update distances
            pass

        elif neighbour_city[0] not in [x[0] for x in
                                       unvisited]:  # if neighbour not in unvisited, append (make sure to update the distance of each neighbour to the destination city)
            neighbour_city[
                1] += dist_closest_city_destination  # adjust distances of new neighbours for distance of closest city to destination city
            unvisited.append(tuple(neighbour_city))
            # problem is that i'm trying to change tuple; need to convert to list then change back to tuple

        else:  # if neighbour in unvisited, compare the distance in unvisited to distance in neighbour - if unvisited is larger, update new distance to the new one
            for i in range(len(unvisited)):
                if unvisited[i][0] == neighbour_city[0] and unvisited[i][1] > neighbour_city[
                    1] + dist_closest_city_destination:
                    unvisited[i] = (neighbour_city[0], neighbour_city[1] + dist_closest_city_destination)

    return "Visited: %s \nUnvisited: %s\n" % (visited, unvisited)

# Exercise 5 - Markus (use E5_Tester)
def visit_all(city, distances):
    unvisited = [(city, 0)]
    visited = []

    for i in range(len(distances)):
        visit_next(visited, unvisited, distances)

    s_visited = sorted(visited)
    return s_visited

# Exercise 4 - Part 3
def get_all_cities(distances):
    city_list = []

    for key in distances:
        if key not in city_list:
            city_list.append(key)

        entry_list = distances[key]
        for entry in entry_list:
            if entry[0] not in city_list:
                city_list.append(entry[0])

    sorted_list = sorted(city_list)

    return sorted_list

# Exercise 5 - not in E5_tester but complete anyways
def get_all_dists(distances):
    dict = {}
    for city in distances:
        dict[city] = visit_all(city, distances)

    return dict

##Actual Case - Final output
#distances = build_distances(open("cities.txt").readlines())
#print(get_all_dists(distances))

# Check if output of get_all_dists matches expected output
#print(get_all_dists(distances) == {'Mexico City': [('Mexico City', 0),('San Francisco', 3),('Toronto', 7),('Washington', 8),('New York', 10)],'New York': [('New York', 0),('Washington', 2),('Toronto', 3),('San Francisco', 7),('Mexico City', 10)],'Toronto': [('Toronto', 0),('New York', 3),('Washington', 5),('San Francisco', 6),('Mexico City', 7)],'San Francisco': [('San Francisco', 0),('Mexico City', 3),('Washington', 5),('Toronto', 6),('New York', 7)],'Washington': [('Washington', 0),('New York', 2),('San Francisco', 5),('Toronto', 5),('Mexico City', 8)]})

##PART 2 - Simulation Starter ##

# Exercise 6 - Part 3
def init_zero_sick_population(cities):
    dict = {}

    for city in cities:
        dict[city] = 0

    return dict

# Final assignment - Part 1 (building the all_dists dict for E6-P4)
def build_shortest_distances():
    distances = build_distances(open("cities.txt").readlines())
    all_dists = get_all_dists(distances)

    return all_dists

# Exercise 6 - Part 4
def build_transition_probs(all_dists, alpha):
    dict_of_normalized_prob = {}

    for city1 in all_dists:

        dict_of_probabilities = {}
        sum_of_probabilities = 0

        for i in range(len(all_dists[city1])):
            city2 = all_dists[city1][i][0]
            distance = all_dists[city1][i][1]

            # formula 1 - probability of moving from city 1 to 2
            denominator = (1 + distance) ** alpha
            prob_of_moving = 1 / denominator

            sum_of_probabilities += prob_of_moving

            dict_of_probabilities[city2] = prob_of_moving

        # formula 2 - normalized probability of moving
        for city2 in dict_of_probabilities:
            normalized_prob = dict_of_probabilities[city2] / sum_of_probabilities

            if city1 not in dict_of_normalized_prob:
                dict_of_normalized_prob[city1] = [(city2, normalized_prob)]

            else:
                # dict_of_normalized_prob[city1].append((city2, normalized_prob))

                added = False

                for i in range(len(dict_of_normalized_prob[city1])):  # to sort in decreasing order by normalized_prob
                    if normalized_prob > dict_of_normalized_prob[city1][i][1]:
                        dict_of_normalized_prob[city1].insert(i, (city2, normalized_prob))
                        added = True
                        break

                if added == False:
                    dict_of_normalized_prob[city1].append((city2, normalized_prob))

    return dict_of_normalized_prob

## Test case for build_transition_probs
#alpha = 2
#all_dists = {'Mexico City': [('Mexico City', 0),('San Francisco', 3),('Toronto', 7),('Washington', 8),('New York', 10)],'New York': [('New York', 0),('Washington', 2),('Toronto', 3),('San Francisco', 7),('Mexico City', 10)],'Toronto': [('Toronto', 0),('New York', 3),('Washington', 5),('San Francisco', 6),('Mexico City', 7)],'San Francisco': [('San Francisco', 0),('Mexico City', 3),('Washington', 5),('Toronto', 6),('New York', 7)],'Washington': [('Washington', 0),('New York', 2),('San Francisco', 5),('Toronto', 5),('Mexico City', 8)]}
#result = print(build_transition_probs(all_dists, alpha))
#expected = {'Mexico City': [('Mexico City', 0.9101374498147844),('San Francisco', 0.056883590613424025),('Toronto', 0.014220897653356006),('Washington', 0.011236264812528202),('New York', 0.007521797105907309)],'New York': [('New York', 0.8350726686715951),('Washington', 0.09278585207462167),('Toronto', 0.052192041791974696),('San Francisco', 0.013048010447993674),('Mexico City', 0.0069014270138148355)],'Toronto': [('Toronto', 0.8878542892195415),('New York', 0.05549089307622134),('Washington', 0.02466261914498726),('San Francisco', 0.018119475290194722),('Mexico City', 0.013872723269055335)],'San Francisco': [('San Francisco', 0.8878542892195415),('Mexico City', 0.05549089307622134),('Washington', 0.02466261914498726),('Toronto', 0.018119475290194722),('New York', 0.013872723269055335)],'Washington': [('Washington', 0.8481675392670158),('New York', 0.09424083769633508),('San Francisco', 0.02356020942408377),('Toronto', 0.02356020942408377),('Mexico City', 0.010471204188481676)]}
#print(expected)

# Exercise 6 - Part 1
def get_cities(prob_pairs):
    city_list = []

    for pair in prob_pairs:
        city_list.append(pair[0])

    return city_list

# Exercise 6 - Part 2
def get_probabilities(prob_pairs):
    prob_list = []

    for pair in prob_pairs:
        prob_list.append(pair[1])

    return prob_list

def choice(probs, cities, n_sick):
    from numpy.random import choice
    chosen_dests = list(choice(cities, size=n_sick, p=probs))

    return chosen_dests

#Actual
#probs = get_probabilities(prob_pairs)
#cities = get_cities(prob_pairs)
#size = sample size

#print(choice(probs, cities, n_sick))

# Final assignment - Part 2
def time_step(sick_pop, transition_probs, alpha, beta, gamma):
    '''
    Change sick_pop to account for one time-step in the simulation

    Arguments:
    sick_pop: dictionary of city to num sick
    transition_probs: dictionary city to list of (city, prob of destination)

    change sick_pop
    '''
    #add all of the destinations for each city for 1 time step to here, so that you can update them AFTER the first loop beelow is completed (otherwise you will have people doublecounted)
    dest_dict = {}

    #Determining next likely move for all people in each city
    for city in transition_probs:
        n_sick = sick_pop[city]

        prob_pairs = transition_probs[city]
        cities = get_cities(prob_pairs)
        probs = get_probabilities(prob_pairs)

        next_move = choice(probs, cities, n_sick) #want to figure out where each person should go to, so size = 1

        for destination in next_move:
            if city not in dest_dict:
                dest_dict[city] = [destination]

            else:
                dest_dict[city].append(destination)

    #Updating sick_pop to account for where sick people are moving
    for city in dest_dict: #update sick_pop for people moving after each time step
        for destination in dest_dict[city]:
            if destination != city: #means that they moved
                sick_pop[city] -= 1
                sick_pop[destination] += 1

    #Determining whether a sick person will recover or infect others in the same city, and updating the sick pop for each city
    for city in transition_probs:

        recover = 0
        infected = 0

        n_sick = sick_pop[city]
        probs_recover = [beta, 1-beta] #decide randomly whether each individual will recover or remain sick
        probs_infect = [gamma, 1-gamma]
        options = [1,0] # 1 = recover or infect; 0 = not recover or not infext

        recover_choice = choice(probs_recover, options, n_sick)
        for sickie in recover_choice:
            if sickie == 1:
                recover += 1

        infected_choice = choice(probs_infect, options, n_sick)
        for sickie in infected_choice:
            if sickie == 1:
                infected += 1

        total_change = infected - recover

        sick_pop[city] += total_change

    return sick_pop

def run_time(runs):
    for i in range(runs):
        results = time_step(sick_pop, transition_probs, alpha, beta, gamma)
        print("Day %s %s" %(i, results))

##CONTROL CODE FOR ENTIRE SIMULATION - BELOW ##

## ADJUST THE FOLLOWING PARAMETERS TO CHANGE THE SIMULATION BEHAVIOUR ##

##Simulation 1: simulation as seen in the assignment handout
#runs = 100 #runs
#alpha = 2 #probability of movement (inveserly proportional)
#beta = .3 #probability of recovery
#gamma = .3 #probability of infection

#Simulation 2: interesting simulation - larger gamma (higher probability of infection - twice as likely to infect than to recover) - mirrors an uncontrolled epidemic
runs = 35 #keep runs low, as time to run is exponential with higher gamma
alpha = 2
beta = .3
gamma = .6

## DO NOT ADJUST THESE PARAMETERS (UNLESS WANT TO CHANGE INPUT AND/OR # INITIAL INFECTED ##
distances = build_distances(open("cities.txt").readlines()) #change folder if you want different input
cities = get_all_cities(distances)

sick_pop = init_zero_sick_population(cities)
sick_pop["Toronto"] = 1
transition_probs = build_transition_probs(build_shortest_distances(), alpha) #steps 1-3

##Calling time_step (individually)
#print(time_step(sick_pop, transition_probs, alpha, beta, gamma))

##Calling run_time (final function for entire program)
print(run_time(runs))

'''
###############################################################################
#Sample run of the simulation

alpha = 2       #larger alpha => smaller likelihood of transition
beta = .3       #recovery probability
gamma = .3      #infection probability

# Step 1: load the dictionary of distances of direct flights between cities
distances = get_distances(open("cities.txt").readlines())

# Step 2: build a dictionary of the shortest distances from every city to every other
all_dists = build_distance_dict(distances)

# Step 3: build a dictionary of probabilities of moving from every city to every other
all_probs = build_transition_prob_dict(all_dists, alpha)

# get a list of all the cities in our simulation
cities = get_all_cities(distances)

# sick_pop is a dictionary of cityname to number of sick inhabitants
# initially every city has 0 sick people
sick_pop = init_zero_sick_population(cities)
# but Toronto has 1 sickie
sick_pop["Toronto"] = 1

# now run the simulation for 100 time steps
for i in range(100):
    time_step(sick_pop, all_probs, beta, gamma)
    print("Day", i, sick_pop)

'''