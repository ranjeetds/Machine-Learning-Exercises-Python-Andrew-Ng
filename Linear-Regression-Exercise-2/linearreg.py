import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Reading Input from .dat files
x = pd.read_csv('ex2x.dat', header=None)
x = np.array(x)
y = pd.read_csv('ex2y.dat', header=None)
y = np.array(y)

# Initializing theta with zero values
theta = np.zeros(2)

#y=theta[0]+theta[1]x hence adding column containing 1 to x to find theta0
c = []
for i in range(len(y)):
	c.append(1)

c = np.array(c)
c.resize(len(y),1) 
x = np.hstack((c,x)).T

#Plottong scatter plot
plt.plot(x[1,:],y,'o')

m = len(y)
alpha = 0.07
iterations = 1500
theta = np.array(theta)
theta.resize(len(theta),1)

#Gradient Descent method
for i in range(iterations):	
	thetamed = np.transpose(np.dot((np.dot(np.transpose(theta),x)-np.transpose(y)),np.transpose(x))*(alpha/m))
	theta = theta - thetamed

#Plotting fitted y line on scatter plot
new_y = theta[0]+(theta[1]*x)
plt.plot(x,new_y)

#Predicting height for given age
theta = np.array(theta)
theta.resize(len(theta),1)
new_x = float(raw_input("Please enter age for which you want to predict height"))
c1 = 1
new_x = np.hstack((c1,new_x)).T
print np.dot(np.transpose(theta),new_x)

#Accuracy
sigma = np.sqrt(np.sum(np.square(np.dot(np.transpose(theta),x)-y))/m)
print sigma 

#Display plot
plt.show()
