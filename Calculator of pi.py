
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import time

#n是无限级数展开项数
print('Hi! This is a program to calculate the approximate value of pi')
n=int(input( 'n是无限级数展开项数\n'+'Please enter n:'))
time_start=time.time()
sum_i=0
for i in range(1,n+1):
    sum_i=(sum_i+(-1)**(i-1)/(2*i-1))
    
    sum=4*sum_i
    x_values = i
    y_values = sum
    plt.scatter(x_values, y_values, s=5)

plt.title('Calculation of pi', fontsize=24)
plt.xlabel('Value of n',fontsize=20)
plt.ylabel('Value of sum',fontsize=20)

time_end=time.time()
time=time_end-time_start
print('The approximate value of pi=', end='')
print(sum)

print('Time used:',end=' ')
print(time,end='')
print('s')

print('Here is the graph how the sum approaches to pi')
plt.show()
