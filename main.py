import random
import math
random.seed(1)

producers = 10000
prey = 100
predators = 1

repeats = 100

for i in range(0, repeats):
    print(str(producers) + ", " + str(prey) + ", " + str(predators))
    new_producers = 0
    new_prey = 0
    new_predators = 0
#    for m in range(0, producers):
#        if (random.randint(1, 3) >= 2):
#            new_producers = new_producers + 2
#        else:
#            new_producers = new_producers + 1
    new_producers = producers + (90*(1+math.sin(i * (math.pi/40))))


    for n in range(0, prey):
        if (prey == 0):
            q_score = 0.001
        else:
            q_score = new_producers/prey
        rand_score = random.randint(1, 10)
        if (q_score > 10):
            if (rand_score < 3):
                new_prey = new_prey + 1
                new_producers = new_producers - 1
            else:
                new_prey = new_prey + 2
                new_producers = new_producers - 2
        elif (q_score <= 10 and q_score > 1):
            if (rand_score < 3):
                # Dies, does not pass on.
                new_prey = new_prey
            elif (rand_score > 7):
                # Reproduces
                new_prey = new_prey + 2
                new_producers = new_producers - 2
            else:
                new_prey = new_prey + 1
                new_producers = new_producers - 1
        elif (q_score <= 1 and q_score > 0):
            if (rand_score < 2):
                # Survives.
                new_prey = new_prey + 1
                new_producers = new_producers - 1
            else:
                new_prey = new_prey

    for p in range(0, predators):
        if (new_prey == 0):
            q_score = 0.001
        else:
            q_score = new_prey/predators
        rand_score = random.randint(1, 10)
        if (q_score > 10):
            if (rand_score < 3):
                new_predators = new_predators + 1
                new_prey = new_prey - 1
            else:
                new_predators = new_predators + 2
                new_prey = new_prey - 2
        elif (q_score <= 10 and q_score > 1):
            if (rand_score < 3):
                # Dies, does not pass on.
                new_predators = new_predators
            elif (rand_score > 7):
                # Reproduces
                new_predators = new_predators + 2
                new_prey = new_prey - 2
            else:
                new_predators = new_predators + 1
                new_prey = new_prey - 1
        elif (q_score <= 1 and q_score > 0):
            if (rand_score < 2):
                # Survives.
                new_predators = new_predators + 1
                new_prey = new_prey - 1
            else:
                new_predators = new_predators
        else:
            new_predators = new_predators
    #new_producers = producers
    prey = new_prey
    predators = new_predators
    producers = new_producers
