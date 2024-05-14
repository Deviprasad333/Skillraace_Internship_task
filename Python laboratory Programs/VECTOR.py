from typing import List

def add(v: List, w: List) -> List:
  assert len(v)==len(w)
  return [v_i + w_i for v_i, w_i in zip(v, w)]
v_input = input('Enter numbers for the first vector separated by spaces: ')
v = [float(x) for x in v_input.split()]

w_input = input("Enter numbers for the second vector separated by spaces: ")
w = [float(x) for x in w_input.split()]

result = add(v, w)

print("The sum of the vectors is:", result)