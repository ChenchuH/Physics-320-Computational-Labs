import matplotlib.pyplot as plt

x = [1.0222,
0.9055,
0.819,
0.7025,
0.6078,
0.5053,
0.4098]

y = [0.9912355703,
1.035478741,
0.9848107448,
0.9687330961,
0.854266206,
0.8978626558,
0.7995729624]

fig, ax = plt.subplots(figsize=(7, 5))

ax.scatter(
    x,
    y,
    color="blue",
    edgecolor="black",
    s=55,
    label="Measured data",
    zorder=3
)

ax.axhline(
    1,
    color="red",
    linestyle="--",
    linewidth=1.5,
    label="Ideal gas prediction"
)

ax.set_xlabel(r"Temperature, $T$")
ax.set_ylabel(r"Ratio, $PV/NT$")
ax.set_title(r"$PV/NT$ vs. Temperature")

ax.set_xlim(0.35, 1.08)
ax.set_ylim(0.75, 1.08)

ax.grid(True, linestyle=":", alpha=0.7)
ax.legend(loc="upper left")
fig.tight_layout()

fig.savefig(
    "PV_NT_vs_Temperature.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()