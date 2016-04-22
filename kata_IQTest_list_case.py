# This program evaluates the evenness of numbers in a sting and returns the position of the "odd" number
# Examples:
# iqTest(" 2 2 7 6 ") => 3
# iqTest(" 1 3 7 14 10") => 4

# Evaluates the evenness of number in a string
# iqTest receives numbers as a string and returns an integer
def iqTest(numbers):
  # convert string to a list without empty spaces
  numbers = list(numbers.split())
  # create lists for odd and even values
  odd = []
  even = []
  # separate odd and even numbers
  for index in range(0,len(numbers)):
    number = int(numbers[index])
    if number%2 == 0:
      even.append((number, index))
    else:
      odd.append((number, index))
  #check which list is bigger (than 1)
  if len(even) > len(odd):
    result = odd[0][1]
  else:
    result = even[0][1]
  #add one to give position
  return result + 1

def main():
  result = iqTest(" 1 3 7 14 10")
  print "=>", result

if __name__ == '__main__':
  main()
