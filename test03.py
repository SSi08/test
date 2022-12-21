
def hello():
    print('_________________________________________________________')
    side = int(float(input('Enter side of square = ')))
    long = int(float(input('Enter long of square = ')))

    for x in range(side):
      for y in range(long):
        print('* ', end='')
      print('')

    print('_________________________________________________________')
    heigh = int(float(input('Enter heigh of triangle = ')))

    for i in range(0,heigh):
      for j in range(0,heigh-i-1):
        print(end=' ')
      for k in range(0,i+1):
        print('*', end=' ')
      print('')

    print('_________________________________________________________')
    print('...Is that your HOUSE ??')

    for i in range(0,heigh):
      for j in range(0,heigh-i-1):
        print(end=' ')
      for k in range(0,i+1):
        print('*', end=' ')
      print('')

    for x in range(side):
      for y in range(long):
        print('* ', end='')
      print('')

    print('_________________________________________________________')
    numS = int(float(input('Enter number of square = ')))
    numT = int(float(input('Enter number of triangle = ')))
    As = side*long*numS
    At = ((1/2)*heigh*heigh)*numT
    print('_________________________________________________________')
    print('your area of square is ',As)
    print('your area of triangle is ',At)
    print('_________________________________________________________')
    print('...This is your HOUSE')

    for i in range(0,heigh*numT):
      for j in range(0,heigh*numT-i-1):
        print(end=' ')
      for k in range(0,i+1):
        print('*', end=' ')
      print('')

    for x in range(side*numS):
      for y in range(long*numS):
        print('* ', end='')
      print('')
    
hello()