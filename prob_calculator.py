import copy
import random
from collections import Counter

class Hat:
  def __init__(self, **kwargs):
    self.contents = []

    for color, nb in kwargs.items():
      self.contents += [color]*nb

  def draw(self, n):
    output = []
    m = len(self.contents)

    if n >= m:
      output = self.contents
      self.contents = []
    else:
      for i in range(n):
        m    -= 1
        k     = random.randint(0,m)
        color = self.contents.pop(k)
        output.append(color)

    return output

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  c = 0
  for i in range(num_experiments):
    res = Counter(copy.deepcopy(hat).draw(num_balls_drawn))
    b   = 1

    for color,num in expected_balls.items():
      if (not color in res) or (res[color] < num):
        b = 0
        break
    c += b

  return c/num_experiments
