import os

os.chdir(
    "/Users/nicolasahar/Desktop/ECs/2015-2016/Computing for Medicine (Apr 2016)/Assignments/Assignment 2 (due July 29)/Project Outline")


# Exercise 4 - Part 5
def process_line(line):
    """ (str) -> (str, str, number)

    Process one line of data from a data file (in the same format as
    cities.txt) to extract the first city's name, the second city's name, and the
    distance.  Return these values in a tuple..

    Parameters:
        line-- a single line from a data file, in the format specified in the
               project handout (first city:second city distance)
    Return value:
        (first, second, distance), where first is the name of the first city,
        second is the name of the second city, and distance is the distance
    """

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


## Test for process_line:
# print(process_line("A:B 3"))
# print(process_line("some city:B 2"))
# print(process_line("A:other city 5"))

# Exercise 4 - Part 4
# Note: deleted starter function "get_distances" as it was the same as same as 'build_distances". If need it, donwload original starter code.
def build_distances(lines):
    """ Read distances between cities from the lines read from data,
    which is in the same format as cities.txt, and
    return a dictionary structure that contains all of this information.


    Parameters:
        lines -- a list of lines read in from data in the same format as
                 cities.txt
    Return value:
        a dictionary whose keys are city names and whose values are lists of
        pairs of the form (city_name, distance).
        The cities must be sorted in alphabetical order.
        (Note: sorted([("B", 3), ("A", 2)]) returns [('A', 2), ('B', 3)]

    Side-effects:
        None

    Examples:
    # The second line below violates style guidelines (it is too long) because
    # this is required for doctest to work properly.
    >>> build_distances(lines)  # assuming lines are the lines of cities.txt
    >>> build_distances(open("cities.txt").readlines())  # assuming the data file from the handout
    {'Toronto': [('New York', 3), ('Mexico City', 7), ('San Francisco', 6)], 'San Francisco': [('Washington', 5), ('Mexico City', 3), ('Toronto', 6)], 'New York': [('Toronto', 3), ('Washington', 2)], 'Washington': [('New York', 2), ('San Francisco', 5)], 'Mexico City': [('San Francisco', 3), ('Toronto', 7)]}
    """

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


# Test Cases for build_distances (without calling process_line function)

# print(build_distances([("A", "B", 3)]))
# result= {"A":[("B", 3)], "B": [("A",3)]}
# print(result == build_distances([("A", "B", 3)]))

# print(build_distances([("A", "B", 3), ("C","A",4)]))
# result = {"A":[("B", 3), ("C", 4)], "B": [("A",3)], "C":[("A", 4)]}
# print(result == build_distances([("A", "B", 3), ("C","A",4)]))

# Test Cases for build_distance (with valling(process_line)
# print(build_distances(["A:B 3"]))

# print(build_distances(["A:B 2\n", "B:C 3\n"]))
# result = {'A': [('B', 2)], 'B': [('A', 2), ('C', 3)], 'C': [('B', 3)]}
# print(result == build_distances(["A:B 2\n", "B:C 3\n"]))

# actual = print(build_distances(['Toronto:New York 3\n', 'New York:Washington 2\n','Washington:San Francisco 5\n', 'San Francisco:Mexico City 3\n','Toronto:Mexico City 7\n', 'Toronto:San Francisco 6\n']))
# result = {'Mexico City': [('San Francisco', 3), ('Toronto', 7)], 'New York': [('Toronto', 3), ('Washington', 2)], 'San Francisco': [('Mexico City', 3), ('Toronto', 6), ('Washington', 5)], 'Toronto': [('Mexico City', 7), ('New York', 3), ('San Francisco', 6)], 'Washington': [('New York', 2), ('San Francisco', 5)]}
# print(actual == result)

# Exercise 4 - Part 1
def get_closest(unvisited):
    """ Returns a tuple from list unvisited that has the shortest distance
    (return the first such tuple in case of ties).  Assumes unvisited is not
    empty.

    Parameters:
        unvisited-- a list of (city_name, distance) pairs
    Return value:
        the first tuple in unvisited whose distance is minimum
    Side-effects:
        None

    Examples:
    >>> get_closest([('A', 3)])
    ('A', 3)
    >>> get_closest([('A', 3), ('B', 2)])
    ('B', 2)
    >>> get_closest([('A', 3), ('C', 4)])
    ('A', 3)
    >>> get_closest([('A', 3), ('B', 2), ('C', 4), ('D', 2)])
    ('B', 2)
    """
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


## Test Cases for get_closest
# print(get_closest([('A', 3)]))
# print(get_closest([('A', 3), ('B', 2)]))
# print(get_closest([('A', 3), ('C', 4)]))
# print(get_closest([('A', 3), ('B', 2), ('C', 4), ('D', 2)]))

# Exercise 4 - Part 2
def find_city(city, city_list):
    """ Return the index of the first tuple that contains city in city_list, or
    -1 if city does not appear in city_list.

    Parameters:
        city-- the name of a city to look for (a string)
        city_list-- a list of tuples of the form (city_name, distance)
    Return value:
        the index of the first tuple in city_list that contains city; -1 if no
        tuple in city_list contains city
    Side-effects:
        None

    Examples:
    >>> find_city('A', [('A', 2)])
    0
    >>> find_city('A', [('B', 3), ('C', 2)])
    -1
    >>> find_city('A', [('B', 3), ('C', 2), ('A', 2)])
    2
    >>> find_city('C', [('B', 3), ('C', 2), ('A', 2), ('C', 4)])
    1
    """

    for i in range(len(city_list)):
        if city_list[i][0] == city:
            return i
            break

    return -1


## Test Cases for find_city
# print(find_city('A', [('A', 2)]))
# print(find_city('A', [('B', 3), ('C', 2)]))
# print(find_city('A', [('B', 3), ('C', 2), ('A', 2)]))
# print(find_city('C', [('B', 3), ('C', 2), ('A', 2), ('C', 4)]))

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


##Test Case
# distances = build_distances(open("cities_2.txt").readlines()) #same as dict below
# distances = {'D': [('C', 1), ('A', 9)], 'A': [('B', 4), ('D', 9)], 'B': [('A', 4), ('C', 2)], 'C': [('B', 2), ('D', 1)]}
# unvisited = [("A", 0)] #this is the destination city
# visited = []

# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))

##Actual Case
# distances = build_distances(open("cities.txt").readlines())
# unvisited = [('Toronto', 0)] #this is the destination city
# unvisited = [('New York', 0)]
# unvisited = [('Washington', 0)]
# unvisited = [('San Francisco', 0)]
# unvisited = [('Mexico City', 0)]
# visited = []

# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))
# print(visit_next(visited, unvisited, distances))

'''
    """ Move the next closest city from the unvisited list to the visited list.
    Update the distances in the unvisited list if a shorter path exists to one
    of the unvisited cities, as described in the handout.  Assumes that the
    unvisited list is non-empty.

    Parameters:
        visited-- a list of tuples for cities that have been "visited", i.e.,
            their minimum distance to the city of origin is known, and their
            neighbours already belong to the visited or unvisited list
        unvisited-- a list of tuples for cities that have not yet been visited
        distances-- a dictionary of direct flight lengths between cities,
                    such as what is returned by get_distances()
    Return value:
        None
    Side-effects:
        - the first city C whose distance is minimum in unvisited is removed
          from unvisited and added to visited
        - neighbours of C that did not already belong to either list are added
          to unvisited (with their distance from C)
        - neighbours of C that were already in unvisited have their distance
          updated, if going through C leads to a shorter total distance

    Examples:
    # This needs to be tested much more thoroughly than the few cases below, to
    # take into account all the possible situations that could come up.
    >>> distances = get_distances(open("cities.txt").readlines())
    >>> unvisited = [('Toronto', 0)]
    >>> visited = []
    >>> visit_next(visited, unvisited, distances)
    >>> visited
    [('Toronto', 0)]
    >>> unvisited
    [('New York', 3), ('Mexico City', 7), ('San Francisco', 6)]
    >>> visit_next(visited, unvisited, distances)
    >>> visited
    [('Toronto', 0), ('New York', 3)]
    >>> unvisited
    [('Mexico City', 7), ('San Francisco', 6), ('Washington', 5)]
    >>> visit_next(visited, unvisited, distances)
    >>> visited
    [('Toronto', 0), ('New York', 3), ('Washington', 5)]
    >>> unvisited
    [('Mexico City', 7), ('San Francisco', 6)]
    """

    # Step 1:
    # Find the city to move from the unvisited list to the visited list, and
    # move it.


    ############################################################################

    # Step 2:
    # Find every neighbour of the that was moved to visited and update each
    # one's distance as approrpiate
    # Loop through every neighbour:
        # For each neighbour, there are three cases to consider:
            # ...(a) neighbour is already visited: do nothing
            # ...(b) neighbour is already unvisited: update its distance
            # ...(c) neighbour is not even unvisited: add it to unvisited
'''


# Exercise 5 - Markus (use E5_Tester)
def visit_all(city, distances):
    unvisited = [(city, 0)]
    visited = []

    for i in range(len(distances)):
        visit_next(visited, unvisited, distances)

    s_visited = sorted(visited)
    return s_visited

    '''Return the list of shortest distances from city city to every city in
    the dictionary distances. This is accomplished by repeatedly calling
    visit_next inside a while loop.


    Arguments:
            distances-- a dictionary of direct flight lengths between cities,
            such as what is returned by get_distances()

    >> distances = get_distances(open("cities.txt").readlines())
    >> visit_all('Toronto', distances)
    [('Mexico City', 7),
     ('New York', 3),
     ('San Francisco', 6),
     ('Toronto', 0),
     ('Washington', 5)]

    '''


##Test Case:
# distances = {'D': [('C', 1), ('A', 9)], 'A': [('B', 4), ('D', 9)], 'B': [('A', 4), ('C', 2)], 'C': [('B', 2), ('D', 1)]}
# print(visit_all("A", distances))
# print(visit_all("B", distances))
# print(visit_all("C", distances))
# print(visit_all("D", distances))

# Actual Case:
# distances = build_distances(open("cities.txt").readlines())
# print(visit_all("Toronto", distances))
# print(visit_all("New York", distances))
# print(visit_all("Washington", distances))
# print(visit_all("San Francisco", distances))
# print(visit_all("Mexico City", distances))

# Exercise 4 - Part 3
def get_all_cities(distances):
    '''Return a list of all the cities that appears in the dictionary
    distances, which was returned by build_distances. The cities are to be
    sorted in alphabetic order

    >> distances = {'Washington': [('New York', 2), ('San Francisco', 5)],
                    'Toronto': [('New York', 3)]}
    >> get_all_cities(distances)

    ['New York', 'San Francisco', 'Toronto', 'Washington']
    '''

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


## Test Case for get_all_cities
# distances = {'Washington': [('New York', 2), ('San Francisco', 5)],
#             'Toronto': [('New York', 3)]}
# print(get_all_cities(distances))

# Exercise 5 - not in E5_tester but complete anyways
def get_all_dists(distances):
    dict = {}
    for city in distances:
        dict[city] = visit_all(city, distances)

    return dict

##Actual Case
#distances = build_distances(open("cities.txt").readlines())
#print(get_all_dists(distances))

# Check if output of get_all_dists matches expected output
# print(get_all_dists(distances) == {'Mexico City': [('Mexico City', 0),('San Francisco', 3),('Toronto', 7),('Washington', 8),('New York', 10)],'New York': [('New York', 0),('Washington', 2),('Toronto', 3),('San Francisco', 7),('Mexico City', 10)],'Toronto': [('Toronto', 0),('New York', 3),('Washington', 5),('San Francisco', 6),('Mexico City', 7)],'San Francisco': [('San Francisco', 0),('Mexico City', 3),('Washington', 5),('Toronto', 6),('New York', 7)],'Washington': [('Washington', 0),('New York', 2),('San Francisco', 5),('Toronto', 5),('Mexico City', 8)]})

'''
    Return a dictionary all_dists whose keys are cities which appear in
    the argument distances
    (either as source cities or destination cities) and whose values are the
    shortest path distance to every other city (i.e., the values are return
    values of visit_all


    Arguments:
            distances-- a dictionary of direct flight lengths between cities,
            such as what is returned by build_distances()


    >> distances = build_distances(open("cities.txt").readlines())
    >> get_all_dists(distances)
        {'Mexico City': [('Mexico City', 0),
        ('San Francisco', 3),
        ('Toronto', 7),
        ('Washington', 8),
        ('New York', 10)],
        'New York': [('New York', 0),
        ('Washington', 2),
        ('Toronto', 3),
        ('San Francisco', 7),
        ('Mexico City', 10)],
        'Toronto': [('Toronto', 0),
        ('New York', 3),
        ('Washington', 5),
        ('San Francisco', 6),
        ('Mexico City', 7)],
        'San Francisco': [('San Francisco', 0),
        ('Mexico City', 3),
        ('Washington', 5),
        ('Toronto', 6),
        ('New York', 7)],
        'Washington': [('Washington', 0),
        ('New York', 2),
        ('San Francisco', 5),
        ('Toronto', 5),
        ('Mexico City', 8)]}
'''

distances_cities_txt = {'Mexico City': [('San Francisco', 3), ('Toronto', 7)],
                        'New York': [('Toronto', 3), ('Washington', 2)],
                        'San Francisco': [('Mexico City', 3), ('Toronto', 6), ('Washington', 5)],
                        'Toronto': [('Mexico City', 7), ('New York', 3), ('San Francisco', 6)],
                        'Washington': [('New York', 2), ('San Francisco', 5)]}    
    
    
distances_difficult = {"A": [('B', 1), ('D', 5)],
                       "B": [('A', 1), ('C', 1), ('D', 3)],
                       "C": [('B', 1), ('D', 1)],
                       "D": [('A', 5), ('B', 3), ('C', 1)]}
    
    
    

distances = distances_cities_txt
unvisited = [('Toronto', 0)]
visited = []
visit_next(visited, unvisited, distances)

if visited == [('Toronto', 0)]:
    print("Test 1 passed")
    
if unvisited == [('Mexico City', 7), ('New York', 3), ('San Francisco', 6)]:
    print("Test 2 passed")
    
visit_next(visited, unvisited, distances)
if visited == [('Toronto', 0), ('New York', 3)]:
    print("Test 3 passed")

if unvisited == [('Mexico City', 7), ('San Francisco', 6), ('Washington', 5)]:
    print("Test 4 passed")

visit_next(visited, unvisited, distances)

if visited == [('Toronto', 0), ('New York', 3), ('Washington', 5)]:
    print("Test 5 passed")

if unvisited == [('Mexico City', 7), ('San Francisco', 6)]:
    print("Test 6 passed")

visit_next(visited, unvisited, distances)

if visited == [('Toronto', 0), ('New York', 3), ('Washington', 5), ('San Francisco', 6)]:
    print("Test 7 passed")
    
visit_next(visited, unvisited, distances)
    
if visited ==  [('Toronto', 0), ('New York', 3), ('Washington', 5), ('San Francisco', 6), ('Mexico City', 7)]:
    print("Test 8 passed")
    
###########################################################################################################################
    
if visit_all("Toronto", distances)  ==  [('Mexico City', 7), ('New York', 3), ('San Francisco', 6), ('Toronto', 0), ('Washington', 5)]:
    print("Test 9 passed")

else:
    print("Test 9 failed")
    
if visit_all("New York", distances)  ==  [('Mexico City', 10), ('New York', 0), ('San Francisco', 7), ('Toronto', 3), ('Washington', 2)]:
    print("Test 10 passed")

else:
    print("Test 10 failed")

if visit_all("San Francisco", distances) == [('Mexico City', 3), ('New York', 7), ('San Francisco', 0), ('Toronto', 6), ('Washington', 5)]:
    print("Test 11 passed")

else:
    print("Test 11 failed")

if visit_all("Mexico City", distances) == [('Mexico City', 0), ('New York', 10), ('San Francisco', 3), ('Toronto', 7), ('Washington', 8)]:
    print("Test 12 passed")

else:
    print("Test 12 failed")

if visit_all("Washington", distances) == [('Mexico City', 8), ('New York', 2), ('San Francisco', 5), ('Toronto', 5),  ('Washington', 0)]:
    print("Test 13 passed")

else:
    print("Test 13 failed")
###########################################################################################################################    
if visit_all('A',  distances_difficult) == [('A', 0), ('B', 1), ('C', 2), ('D', 3)]:
    print("Test 14 passed")
