'''
First Half Challenge
'''
def rucksack_priorities():
  input_file = open('./input.txt', 'r')
  priorities = 0

  for rucksacks in input_file:
    length = len(rucksacks)
    first_rucksack = rucksacks[0:int(length/2)]
    second_rucksack = rucksacks[int(length/2):length]
    
    for char in first_rucksack:
      if char in second_rucksack:
        ascii_value = ord(char)
        priority = ascii_value - 96 if ascii_value > 96 else ascii_value - 38
        priorities += priority
        break

  input_file.close()
  return priorities


'''
Second Half Challenge
'''
def rucksack_priorities_group():
  input_file = open('./input.txt', 'r')
  priorities = 0
  count_groups = 0
  groups = []

  for rucksacks in input_file:
    count_groups += 1
    groups.append(rucksacks)
    if count_groups < 3:
      continue

    for char in groups[0]:
      if char in groups[1] and char in groups[2]:
        ascii_value = ord(char)
        priority = ascii_value - 96 if ascii_value > 96 else ascii_value - 38
        priorities += priority
        groups = []
        count_groups = 0
        break

  input_file.close()
  return priorities


if __name__ == '__main__':
  print(rucksack_priorities())
  print(rucksack_priorities_group())