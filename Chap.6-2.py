import matplotlib.pyplot as plt

#Input
m = float(input("Enter the slope(m): "))
b= float(input("Enter the y-intercept (b): "))

#X-Val
x=[i for i in range(-20, 20)]

#y-Val
y = [m * i + b for i in x]

#Plot
plt.plot(x, y, label=f"y = {m}x + {b}")

plt.grid(True)
#x
plt.axhline(y=0, color='k') 
#y
plt.axvline(x=0, color='k')  
plt.axis('square')
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.legend()
#Final plot
plt.show()

