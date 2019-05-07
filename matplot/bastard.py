from matplotlib import pyplot as plt


def power(i, num):
    return i**num

# ! This is as far as you got porting the shiffman vid
def linreg(i, num):

    # something = (Sum of (X - meanX) - (Y - meanY))/(Sum of (x - meanX)**2)

    return something

def draw_line(startx, endx, color):
    starty = m * startx + b
    endy = m * endx + b
    plt.plot([startx, endx],[starty,endy], color)

# ? --------------------------------------

# # m and b for the thing
m = 10
b = 0

x = [1,4,5,3]
y = [power(i,3) for i in x]

# ! two draws just to check that having 0 and min(x) is the same line
draw_line(0,max(x), 'g')
draw_line(min(x),max(x), 'r')

plt.plot(x,y, 'ms')

# # making the axis always longer than points
plt.axis([0,max(x)*1.1,0,max(y)*1.1])



plt.show()

