# Exp 7: Multipath fading - many reflected paths as receiver moves
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
f, c = 900e6, 3e8
lam = c / f                         # wavelength at 900 MHz
d = np.linspace(0, 5, 1000)         # receiver moves 5 metres
P = 20                              # number of paths

amp = np.random.rand(P)
ph = 2*np.pi*np.random.rand(P)
ang = 2*np.pi*np.random.rand(P)

# Add all paths as complex signals; each path has a different phase
h = sum(
    amp[k] * np.exp(1j*(ph[k] + 2*np.pi*d/lam*np.cos(ang[k])))
    for k in range(P)
)
rssi = 20*np.log10(np.abs(h) / np.abs(h).mean())

plt.figure(figsize=(9, 4))
plt.plot(d, rssi)
plt.axhline(-10, color="r", linestyle="--", label="deep fade (-10 dB)")
plt.xlabel("Distance moved (m)")
plt.ylabel("Signal level (dB)")
plt.grid(alpha=0.3)
plt.legend()
plt.title("Multipath Fading: 20 reflected paths, 900 MHz")
plt.tight_layout()
plt.savefig("exp7_multipath.png", dpi=150)
plt.show()

print("Max fade depth: %.1f dB, fades below -10 dB: %.1f%% of the time"
      % (rssi.min(), 100*(rssi < -10).mean()))
