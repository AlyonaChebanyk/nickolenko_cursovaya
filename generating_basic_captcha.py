from claptcha import Claptcha
import numpy as np
import matplotlib.pyplot as plt

alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets = alphabets.upper()
font = "GothamPro.ttf"
# For each of the 4 characters determine randomly whether its a digit or alphabet
char_num_ind = list(np.random.randint(0,2,4))
text = ''
for ind in char_num_ind:
  if ind == 1:
    # for indicator 1 select character else number
    loc = np.random.randint(0,26,1)
    text = text + alphabets[np.random.randint(0,26,1)[0]]
  else:
    text = text + str(np.random.randint(0,10,1)[0])
c = Claptcha(text, font)
text, image = c.image
plt.imshow(image)
plt.show()