import sys

PassInput = None
PassCorrect = 'Ch4ng3 th1s'

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


PassInput = text_prompt("[>] Password:  ")
if PassCorrect == PassInput:
  print('Correct Password!')
else:
  print('Incorrect Password!')
  sys.exit()
