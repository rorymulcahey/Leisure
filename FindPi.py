# estimate pi
import math
import random
import sys

sys.stdout = open('FindPi.txt', 'w')
total_iters = 10000000


class FindPi:
    def __init__(self, iterations):
        self.x_Val = 0
        self.y_Val = 0
        self.num_iterations = iterations

    def create_random_values(self):
        self.x_Val = random.uniform(0.0, 1.0)
        self.y_Val = random.uniform(0.0, 1.0)

    def distance_formula(self):
        return math.sqrt(self.x_Val*self.x_Val + self.y_Val*self.y_Val)

    def estimate_pi(self):
        value = 0
        for x in range(0, int(self.num_iterations)):
            self.create_random_values()
            if self.distance_formula() < 1:
                value += 1
        return value*4/self.num_iterations


if __name__ == '__main__':
    current_iter = 0
    while current_iter < total_iters:
        current_iter += total_iters/10
        Find_pi = FindPi(current_iter)
        pi_val = Find_pi.estimate_pi()
        error = math.fabs(math.pi - pi_val)/math.pi * 100
        print("Current number of iterations = " + str(round(current_iter, 0)))
        print("Current Pi value = " + str(round(pi_val, 5)))
        print("Percent error: " + str(round(error, 5)) + '%')
        print('\n')
