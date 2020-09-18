__author__ = "Ever Favio Argollo Ticona"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ever Favio Argollo Ticona"
__email__ = "everfavioat@gmail.com"
__status__ = "Finished"

#  import random from random

import random
import pyfiglet
from googletrans import Translator

translator = Translator()
# declarando arrays de datos

print(pyfiglet.figlet_format("Generador de Frases"))
articulos = ['the', 'an', 'a', 'those', 'that', 'these', 'this']
sujeto = [ 'cat', 'puppy','friend', 'lover', 'woman', 'children', 'parents', 'relatives', 'neighibors' ]
sujetos = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "like all these people", "Supermen"]
verbos = ['eat', 'kick', 'give', 'treat', 'meet with', 'create', 'hack', 'configure', 'spy on', 'retard', 'meow on', 'flee from', 'try to automate', 'explode']
infinitivos = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]
# Introduce la cantidad de frases que deseas generar
inp = input('Introduce la cantidad de frases que deseas generar: ')
# Iterando las veces definidas en inp
try:
   for n in range(int(inp)) :
       if random.randint(0,1) == 1 :
           phrase = (f'{n + 1} {random.choice(articulos)} {random.choice(sujeto)} {random.choice(verbos)} {random.choice(infinitivos)}')
           result = (translator.translate((phrase), src='en', dest='es'))
           print(result.text)
       else :
           phrase = (f'{n + 1} {random.choice(sujetos)} {random.choice(verbos)} {random.choice(infinitivos)}')
           result = (translator.translate((phrase), src='en', dest='es'))
           print(result.text)
   pass
except ValueError as  error:
   print('Debes introducir un número!.')