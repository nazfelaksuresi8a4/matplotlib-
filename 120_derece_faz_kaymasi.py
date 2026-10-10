
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 360, 1000)

y1 = 380*np.sin(np.deg2rad(x))
y2 = 380*np.sin(np.deg2rad(x + 120))
y3 = 380*np.sin(np.deg2rad(x + 240))

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="sin(x + 120°)")
plt.plot(x,y3)

plt.xlabel("Açı (derece)")
plt.ylabel("Genlik")
plt.title("120° Faz Farklı Sinüs Dalgaları")
plt.grid(True)
plt.legend()
plt.show()
