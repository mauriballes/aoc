'''
First Half Challenge
'''
def biggest_calories_count(biggest = float('inf')):
  input_file = open('./input.txt', 'r')
  calories_bag = 0
  biggest_calories_bag = 0

  for calorie in input_file:
    if calorie != "\n":
      calories_bag += int(calorie)
    else:
      if calories_bag > biggest_calories_bag and calories_bag < biggest:
        biggest_calories_bag = calories_bag
      calories_bag = 0

  input_file.close()
  return biggest_calories_bag


'''
Second Half Challenge
'''
def biggest_calories_top(n = 3):
  total = 0
  last_biggest_bag = float('inf')

  for i in range(n):
    calories_bag = biggest_calories_count(last_biggest_bag)
    total += calories_bag
    last_biggest_bag = calories_bag

  return total


if __name__ == '__main__':
  print(biggest_calories_count())
  print(biggest_calories_top())