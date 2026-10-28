# Exp 1: EM spectrum & wireless bands (log-scale chart)
import matplotlib.pyplot as plt

bands = [  # (name, start Hz, end Hz, use)
    ("ELF/VLF", 3e3, 3e4, "Submarine"),
    ("LF", 3e4, 3e5, "Navigation"),
    ("MF", 3e5, 3e6, "AM Radio"),
    ("HF", 3e6, 3e7, "Shortwave"),
    ("VHF", 3e7, 3e8, "FM, TV"),
    ("UHF", 3e8, 3e9, "GSM, 4G, TV"),
    ("SHF", 3e9, 3e10, "Wi-Fi, 5G, Sat"),
    ("EHF", 3e10, 3e11, "mmWave 5G"),
    ("Infrared", 3e11, 4e14, "Remote"),
    ("Visible", 4e14, 8e14, "Light"),
    ("UV", 8e14, 3e16, "Sterilise"),
    ("X-ray", 3e16, 3e19, "Medical"),
    ("Gamma", 3e19, 1e21, "Nuclear"),
]

fig, ax = plt.subplots(figsize=(13, 4))
ax.set_xscale("log")
ax.set_xlim(1e3, 1e21)

for i, (name, f1, f2, use) in enumerate(bands):
    ax.barh(0, f2 - f1, left=f1,
            color=plt.cm.rainbow(i / len(bands)), edgecolor="k")
    ax.text((f1 * f2) ** 0.5, 0, f"{name}\n{use}",
            ha="center", va="center", fontsize=7, rotation=90)

for f, name, h in [
    (9e8, "GSM 900", 0.85),
    (2.4e9, "Wi-Fi/BT 2.4G", 0.65),
    (5e9, "Wi-Fi 5G", 0.85),
]:
    ax.annotate(name, (f, 0.5), (f, h), ha="center", fontsize=7,
                arrowprops=dict(arrowstyle="->"))

ax.set_yticks([])
ax.set_ylim(-0.6, 1.1)
ax.set_xlabel("Frequency (Hz) - log scale")
ax.set_title("Electromagnetic Spectrum & Wireless Bands")
plt.tight_layout()
plt.savefig("exp1_spectrum.png", dpi=150)
plt.show()
print("Saved chart as exp1_spectrum.png")
