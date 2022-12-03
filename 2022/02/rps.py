'''
First Half Challenge
'''
def rock_paper_scissors_game_result(opponent_play, play):
  """
  Lose: 0
  Draw: 3
  Win: 6

  Translate plays to numbers
  Rock: 1
  Paper: 2
  Scissors: 3

  Ways to Wins
  Opponent: 1
  Me: 2

  Opponent: 2
  Me: 3

  Opponent: 3
  Me: 1
  """

  LOSE = 0
  DRAW = 3
  WIN = 6

  if play == opponent_play:
    return DRAW
  elif play == opponent_play + 1 or play == opponent_play - 2:
    return WIN
  else: 
    return LOSE

def rock_paper_scissors_score():
  input_file = open('./input.txt', 'r')
  score = 0
  result_points = {
    'A': 1, 'B': 2, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3
  }

  for rps_match in input_file:
    op_play_score = result_points[rps_match[0]]
    me_play_score = result_points[rps_match[2]]
    game_score = rock_paper_scissors_game_result(op_play_score, me_play_score)
    score += game_score + me_play_score

  input_file.close()
  return score


'''
Second Half Challenge
'''
def rock_paper_scissors_game_result_with_strategy(opponent_play, result):
  LOSE = 0
  DRAW = 3
  WIN = 6
  
  if result == DRAW:
    return opponent_play
  elif result == WIN:
    return (opponent_play % 3) + 1
  else: # if result == LOSE
    return 3 if opponent_play == 1 else opponent_play - 1

def rock_paper_scissors_score_with_strategy():
  input_file = open('./input.txt', 'r')
  score = 0
  result_points_strategies = {
    'A': 1, 'B': 2, 'C': 3,
    'X': 0, 'Y': 3, 'Z': 6
  }

  for rps_match in input_file:
    op_play_score = result_points_strategies[rps_match[0]]
    game_score = result_points_strategies[rps_match[2]]
    me_play_score = rock_paper_scissors_game_result_with_strategy(op_play_score, game_score)
    score += game_score + me_play_score

  input_file.close()
  return score


if __name__ == '__main__':
  print(rock_paper_scissors_score())
  print(rock_paper_scissors_score_with_strategy())
