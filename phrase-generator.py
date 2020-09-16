print(f'+++++++++++++++++++GENERATING AWFUL POETRY++++++++++++++++++++++')
#  import random from random
import random
# declaring arrays
articulos = ['the', 'an', 'a', 'those', 'that', 'these', 'this']
sujetos = [ 'cat', 'puppy','friend', 'lover', 'woman', 'children', 'parents', 'relatives', 'neighibors' ]
verbos = ['eat', 'loves', 'run away', 'shows', 'picks', 'sit down', 'end up', 'turn out' ]
adverbios = ["ahí", "allí", "aquí", "acá", "delante", "detrás", "arriba", "abajo", "cerca", "lejos", "encima", "fuera", "dentro"]
# Entering required number of awful verses
inp = input('Enter how many awful poetry verses you need: ')
# Iterating until inp number of verses
try:
   for n in range(int(inp)) :
       if random.randint(0,1) == 1 :
           print(f'{n + 1} {random.choice(articulos)} {random.choice(sujetos)} {random.choice(verbos)} {random.choice(adverbios)}')
       else :
           print(f'{n + 1} {random.choice(articulos)} {random.choice(sujetos)} {random.choice(verbos)}')
   pass
except ValueError as  error:
   print('You have not entered a number!.')