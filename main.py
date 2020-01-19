"""
  Автор: Уляшев Артур, группа №p42551
  Ссылка на сайт-портфолио: https://underherzen.github.io/index.html
  
"""

def find_sum(numbers=[], target=0):
  """ 
    first argument is list of elements, second is target
    returns list of indexes of 2 elements if sum of them is equal to target
    first element less or equals to the second
    example: [1,3] but not [3,1]
    else []
  """
  for index in range(len(numbers)-1):
    for x in range(index+1, len(numbers)):
      if (numbers[index] + numbers[x] == target):
        return [x, index] if x < index else [index, x]
  return []

assert(find_sum([1,2,3,4], target=6) == [1,3])
print('1st test passed')
assert(find_sum([1,2,3,4], target=5) == [0,3])
print('2nd test passed')
assert(find_sum([5,4,8,1,2], target=6) == [0,3])
print('3rd test passed')
assert(find_sum([1,2,3,4], target=6) == [1,4])
print('shouldn`t be printed')
# find_sum([1,2,3], target=3)