# Exercise 6 - Part 1
def get_cities(prob_pairs):
    '''
        Return the list of cities that appear in the list of pairs prob_pairs,
        in the same order that they appear in the list of pairs prob_pairs

        Arguments:
          prob_pairs -- a list of city-distance pairs
    '''
    city_list = []

    for pair in prob_pairs:
        city_list.append(pair[0])

    return city_list

## Test case for get_cities
#prob_pairs = [('New York', 0),('Washington', 2),('Toronto', 3),('San Francisco', 7),('Mexico City', 10)]
#print(get_cities(prob_pairs))

#Exercise 6 - Part 2
def get_probabilities(prob_pairs):
    '''Return the list of probabilities that appear in the list of pairs prob_pairs,
    in the same order that they appear in the list of pairs prob_pairs

    Arguments:
      prob_pairs -- a list of city-distance pairs
    '''
    prob_list = []

    for pair in prob_pairs:
        prob_list.append(pair[1])

    return prob_list

## Test case for get_probabilities
#prob_pairs = [('New York', .1),('Washington', .2),('Toronto', .3),('San Francisco', .2),('Mexico City', .2)]
#print(get_probabilities(prob_pairs))

#Exercise 6 - Part 3
def init_zero_sick_population(cities):
    '''Return a dictionary whose keys are the values in the list cities,
    and whose values are all 0
    
    >> init_zero_sick_population(["TO", "NYC"])
    {"TO": 0, "NYC": 0}
    
    Arguments:
      cities -- a list of strings
    
    '''

    dict = {}

    for city in cities:
        dict[city] = 0

    return dict

## Test Case for init_zero_sick_population
#print(init_zero_sick_population(["TO","NYC"]))


#Exercise 6 - Part 4
def build_transition_probs(all_dists, alpha):
    '''
    Return the dictionary representing the probabilities of moving from all 
    cities to all other cities according to the formula in the handout.
    
    Arguments: 
      all_dists -- a dictionary whose keys are cities, and whose values are
                   lists of city-distance pairs
      alpha     -- a float
    '''

    dict_of_normalized_prob = {}
    #formula 1 - probability of moving from city A to B

    for city1 in all_dists:

        dict_of_probabilities = {}
        sum_of_probabilities = 0

        for i in range(len(all_dists[city1])):

            city2 = all_dists[city1][i][0]
            distance = all_dists[city1][i][1]

            # formula 1 - probability of moving from city 1 to 2
            denominator = (1 + distance)**alpha
            prob_of_moving = 1 / denominator

            sum_of_probabilities += prob_of_moving

            dict_of_probabilities[city2] = prob_of_moving

        # formula 2 - normalized probability of moving
        for city2 in dict_of_probabilities:
            normalized_prob = dict_of_probabilities[city2] / sum_of_probabilities

            if city1 not in dict_of_normalized_prob:
                dict_of_normalized_prob[city1] = [(city2, normalized_prob)]

            else:
                #dict_of_normalized_prob[city1].append((city2, normalized_prob))

                added = False

                for i in range(len(dict_of_normalized_prob[city1])): #to sort in decreasing order by normalized_prob
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

def time_step(sick_pop, transition_probs, alpha, beta, gamma):
    '''
    Change sick_pop to account for one time-step in the simulation
    
    Arguments:
    sick_pop: dictionary of city to num sick
    transition_probs: dictionary city to list of (city, prob of destination)
    
    change sick_pop
    '''

'''
###############################################################################
#Sample run of the simulation    
    
alpha = 2       #larger alpha => smaller likelihood of transition
beta = .3       #recovery probability
gamma = .3      #infection probability

# load the dictionary of distances of direct flights between cities
distances = get_distances(open("cities.txt").readlines())

# build a dictionary of the shortest distances from every city to every other
all_dists = build_distance_dict(distances)

# build a dictionary of probabilities of moving from every city to every other
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
