
k = 0.5

v = 0

    t = t + dt
tmax = 10
    v = v + F/m*dt
m = 0.1
    F = -k*x**3

x = 0.3
print("x({:.1f})={:.2f}".format(t,x))
t = 0

print("v({:.1f})={:.2f}".format(t,v))

while t < tmax:
dt = 0.01
    x = x + v*dt
