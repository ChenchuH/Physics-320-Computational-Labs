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

plt.scatter(x,y, color='blue', label='PV/NT')
plt.axhline(y=1, color='red', linestyle='--', label='PV/NT = 1')
plt.xlabel('Temperature')
plt.ylabel('PV/NT')
plt.title('Scatter Plot of PV/NT vs Temperature')
plt.legend()
plt.savefig('PV_NT_vs_Temperature.png',dpi=300, bbox_inches="tight")
plt.show()