
import microbit
import random
submarine_life = 5



submarine = {}
life = {}
x = {}
y = {}
def dictionnary(nb_submarine):
  """Specification of the function
  Parameters:
  -----------
  nbr_submarine : the number of submarine for a game (int)
  
  Note:
  -----
  The function will generate a dictionnary with the submarine with his position (x and y) and his life
  """
  nb_sub = nb_submarine
  #nb_sub is used to verify is there rest submarine or not
  for n in range(1, nb_submarine + 1):
    
    submarine[n] = {"life" : submarine_life, "x" : random.randint(0, 4), "y" : random.randint (0, 4)}
    
  print(submarine)  

    
dictionnary(5)

