#sorted
a = [5, 1, 4, 3]
print(sorted(a)) #[1, 3, 4, 5]
#reverse = True sorting from backwards
print(sorted(a, reverse=True)) #[5, 4, 3, 1]

strs = ['ccc', 'aaaa', 'd', 'bb']
#key= - to specify the sort
#len -  #by length of the data 
print(sorted(strs, key=len)) #['d', 'bb', 'ccc', 'aaaa']

strs = ['aa', 'BB', 'zz', 'CC']
#str.lower - to treat upper and lowercase as same
print(sorted(strs, key=str.lower)) #['aa', 'BB', 'CC', 'zz']

#using own function in key=
def MyFn(s):
    return s[-1] #to sort the list by last letter

strs = ['xc', 'zb', 'yd' ,'wa']
print(sorted(strs, key=MyFn)) #['wa', 'zb', 'xc', 'yd']

#using itemgetter and attrgetter
from operator import itemgetter
grade = [('Freddy', 'Frank', 3),
         ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
print(sorted(grade, key=itemgetter(0, 0, 2)))

