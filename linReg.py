import matplotlib.pyplot as plt
import numpy as np
import  math
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
plt.xlabel("The value Ist array")
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
z_y_est = [ ]
plt.ylabel("The value Ist array")
plt.scatter(x,y)

n = len((x))
mean_x = np.mean(x)
x_sq = np.multiply(x,x)
mean_x_sq = np.mean(x_sq)

print("mean value of x==", mean_x)
mean_y = np.mean(y)
print("mean value of y==", mean_y)
y_sq = np.multiply(y,y)
mean_y_sq = np.mean(y_sq)
multiply_xy = np.multiply(x, y)
mean_xy = np.mean(multiply_xy)
print(("mean value of xy=", mean_xy))
numerator = 0
denoneator =0
for counter in range(0, n):
    numerator = numerator + ((x[counter]-mean_x)*(y[counter]-mean_y))
    denoneator = denoneator + (x[counter]-mean_x)**2

slop = numerator/denoneator
print("slop===", slop)
intercept = mean_y - slop * mean_x
print(("intercept===", intercept))

for counter1 in range (0, n):
    y_est = slop*x[counter1] + intercept
    z_y_est.append( y_est )
    #print("y estimate value=", z_y_est )
    y_est_mean = np.mean(y_est)
print("the value of mean estimate value", y_est_mean)
sum1 = 0
sum2 = 0

for counter2 in range(0, n):
#  print("y_est[counter2]==", z_y_est[counter2])
  sum1 = sum1 + (z_y_est[counter2] - y_est_mean)**2

  sum2 = sum2 + (y[counter2] - mean_y)**2

print ( "the value of sum1", sum1 )
print("the value of sum2", sum2)

square_r = (sum1/sum2)
print("the value of square r", square_r)
def myfunction(x):

    return slop * x + intercept

mymodel = list(map(myfunction, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
