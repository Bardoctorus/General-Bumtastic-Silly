~# #! simple mouse interupt method from pyplot docs - 
 # #!added shonky list comp to is to make it plot how I imagine it should
 # #! before it felt like the plot of the clicke dpoints got reversed.
 # #! probably way better ways to do this.

 # TODO add the intterupt to a loop/make

import matplotlib.pyplot as plt
import numpy as np
t = np.arange(100)
plt.plot(t, np.sin(t))
print("Please click")
x = plt.ginput(3)

for iter in x:
    g = [i[0] for i in x]
    t = [i[1] for i in x]
    plt.plot(g,t)


print("clicked", x)

plt.show()


    



