#Hi there, if you have any feedback on the code,
#feel free to contact me on linkedin
#https://www.linkedin.com/in/tyson-cheah

import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
      self.contents = []
      for key, value in balls.items():
        self.contents = self.contents + [key] * value

    def draw(self, num):
      drawn = []
      if num <= len(self.contents):
          for i in range(num):
            rand = random.choice(self.contents)
            self.contents.remove(rand)
            drawn.append(rand)
          return drawn
      else:
            return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
      new = copy.deepcopy(hat)
      drawn = new.draw(num_balls_drawn)
      for key, value in expected_balls.items():
        if drawn.count(key) < value:
          count += 1
          break
    return 1 - count/num_experiments
