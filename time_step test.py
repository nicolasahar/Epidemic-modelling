import numpy

def choice(probs, cities, n_sick):
    from numpy.random import choice
    chosen_dests = list(choice(cities, size=n_sick, p=probs))
    return chosen_dests

def change(sick_pop, city, beta, gamma):
    recover = 0
    infected = 0

    n_sick = sick_pop[city]
    probs_recover = [beta, 1 - beta]  # decide randomly whether each individual will recover or remain sick
    probs_infect = [gamma, 1 - gamma]
    options = [1, 0]  # 1 = recover or infect; 0 = not recover or not infext

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

    return sick_pop[city], recover, infected

sick_pop = {"Toronto": 5000}
city = "Toronto"
beta = 0.3
gamma = .6

print(change(sick_pop, city, beta, gamma))

