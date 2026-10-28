# Exp 2: Frequency reuse - sliders change i and j
# N = i^2 + i*j + j^2, Q = D/R = sqrt(3N)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(8, 8.5))
plt.subplots_adjust(bottom=0.17)

s_i = Slider(plt.axes([0.2, 0.08, 0.6, 0.03]), "i", 0, 4,
             valinit=2, valstep=1)
s_j = Slider(plt.axes([0.2, 0.03, 0.6, 0.03]), "j", 0, 4,
             valinit=1, valstep=1)

def draw(_=None):
    i, j = int(s_i.val), int(s_j.val)
    if i == 0 and j == 0:
        return

    N = i*i + i*j + j*j
    Q = np.sqrt(3*N)
    R = 1.0
    ax.clear()
    cells, keys = [], {}

    for q in range(-12, 13):
        for r in range(-12, 13):
            x, y = np.sqrt(3)*R*(q + r/2), 1.5*R*r
            if np.hypot(x, y) > 10:
                continue
            k = ((q*(i+j) + r*j) % N, (r*i - q*j) % N)
            c = keys.setdefault(k, len(keys))
            cells.append((x, y, c))
            ax.add_patch(RegularPolygon(
                (x, y), 6, radius=R,
                facecolor=plt.cm.gist_rainbow(c/N),
                edgecolor="k", alpha=0.8))
            ax.text(x, y, f"F{c+1}", ha="center", va="center", fontsize=7)

    x0, y0, c0 = next(c for c in cells if c[0] == 0 and c[1] == 0)
    near = min(
        (c for c in cells if c[2] == c0 and c[:2] != (x0, y0)),
        key=lambda c: np.hypot(c[0]-x0, c[1]-y0)
    )
    ax.plot([x0, near[0]], [y0, near[1]], "k-", lw=3)
    ax.text((x0+near[0])/2, (y0+near[1])/2,
            f"D={np.hypot(near[0]-x0, near[1]-y0):.2f}R",
            ha="center", fontweight="bold",
            bbox=dict(facecolor="w", edgecolor="k"))
    ax.set_xlim(-10.5, 10.5)
    ax.set_ylim(-10.5, 10.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(
        f"i={i}, j={j} N={N} Q=D/R=sqrt(3N)={Q:.2f} "
        "(same F = same frequencies)"
    )
    fig.canvas.draw_idle()
    print(f"i={i} j={j} N={N} Q=D/R={Q:.2f} "
          f"each cell gets 1/{N} of channels")

s_i.on_changed(draw)
s_j.on_changed(draw)
draw()
fig.savefig("exp2_reuse.png", dpi=120)
plt.show()
