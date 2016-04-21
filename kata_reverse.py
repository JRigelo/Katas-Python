#This code reverses a string in a recursive way
def reverse(str):

  if len(str)== 1:
    return str
  else:
    return str[-1] + print_str(str[0:-1])


def main():
  print reverse('My name is')

if __name__ == '__main__':
  main()
