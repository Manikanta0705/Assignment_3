'''Savita and Hamida are friends. What is the probability that both will have 
(i)Different birthdays?
(ii)The same birthday? (ignoring a leap year).
'''

'''SOLUTION:-
 given,
  no of favourable outcomes for different birthdays = DF = 364
no of favourable outcomes for same birthday = SF = 1
total no of days in a year = TD =365
probability of both having different birthdays = p_db =???
probability of both having same birthdays = p_sb =???'''

DF = 364
SF = 1
TD = 365

p_db = DF/TD
p_sb = SF/TD

print('probability of both having different birthdays =', p_db)
print('probability of both having same birthdays =', p_sb)
