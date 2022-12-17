import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 



fileName = "torque.xlsx"
torqueDataFrame = pd.read_excel(fileName)
# print(torqueDataFrame)      # 3440*2

torqueData = np.asarray(torqueDataFrame)
print(torqueData[1])
torque = torqueData[:,1]

# torque = torque[535:]
torque = torque[1500:2500]

# plt.style.use(['science','ieee'])
fig, ax= plt.subplots(figsize=(7,2)) 
ax.plot(torque, 'b-')
ax.set_xlabel("Time Sequence")
ax.set_ylabel("Torque")
# plt.savefig('a.jpg',dpi=600)
plt.show()