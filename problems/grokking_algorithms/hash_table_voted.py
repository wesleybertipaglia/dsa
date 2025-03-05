def check_voter(name, votes):
  if name in votes:
    print("kick them out!")
  else:
    votes[name] = True
    print("let them vote!")

def test():
  votes = {}
  check_voter("tom", votes)
  check_voter("mike", votes)
  check_voter("mike", votes)

test()