from matplotlib.pyplot import plot, show, legend, xlabel, ylabel, title
from math import cos, tan, pi
import pandas as pd
dataframe = pd.read_csv('cleaned/top_5.csv')
dl=dataframe['likes']
def f(x):
    alpha = dl
    v0 = 10
    y0 = 50
    g = 10
    return -0.5*g*x*x/(v0*v0*cos(alpha*pi/180)) + tan(alpha*pi/180)*x + y0
x = [ i/100 for i in range(0,3401) ]
y = [ f(a/100) for a in range(0,3401) ]
plot(x,y,color='orange',label='altitude de l\'objet')
xlabel('distance (en mètre)')
ylabel('altitude (en mètre)')
title('Trajectoire de l\'objet')
legend()
show()