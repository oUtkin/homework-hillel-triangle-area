# just a few words to get into context
print('Let\'s calculate an area of your triangle. Please tell me...')

# asking user info that needed to calculate area of triangle
a = float(input('the length of the first side: '))
b = float(input('now the length of the second side: '))
c = float(input('finally, the last side: '))

# using p separately because we need it more than 1 time in formula
p = (a + b + c) / 2

print(f'Hmmm... Looks like an area is {(p * (p - a) * (p - b) * (p - c)) ** 0.5} ')
