""" any number divisible by three is replaced by the
 word fizz and any divisible by five by the word buzz.
  Numbers divisible by both become fizz buzz.
  """

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    
    else:
        print(i)