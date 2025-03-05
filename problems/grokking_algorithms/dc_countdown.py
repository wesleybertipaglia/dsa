'''
Count down by given a number
'''

def countdown(i):
  print(i)
  if (i <= 0):
    return
  countdown(i-1)    
        
def test():
    print(countdown(-8))
    print(countdown(10))
    print(countdown(255))

test()
