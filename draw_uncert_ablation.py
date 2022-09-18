import os
import numpy as np
import matplotlib.pyplot as plt


data_root = './results/uncert/0221'

gt_xyz_list = []
pred_xyz_list = []
uncert_xyz_list = []

with open(os.path.join(data_root, 'GT.txt'), 'r') as f:
    for line in f.readlines():
        data = line.strip().split(' ')
        gt_xyz_list.append([float(data[3]), float(data[7]), float(data[11])])

with open(os.path.join(data_root, 'Ours.txt'), 'r') as f:
    for line in f.readlines():
        data = line.strip().split(' ')
        pred_xyz_list.append([float(data[3]), float(data[7]), float(data[11])])

with open(os.path.join(data_root, 'Uncert.txt'), 'r') as f:
    for line in f.readlines():
        data = line.strip().split(' ')
        uncert_xyz_list.append([float(data[0]), float(data[1]), float(data[2])])

gt_xyz_np = np.array(gt_xyz_list)
pred_xyz_np = np.array(pred_xyz_list)
uncert_xyz_np = np.array(uncert_xyz_list)

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(221, xlabel='x', ylabel='z')
ax1.plot(gt_xyz_np[:,0], gt_xyz_np[:,2], color='gray', linestyle='--', label='GT')
ax1.plot(pred_xyz_np[:,0], pred_xyz_np[:,2],label='pred')
ax1.set_title('scene-0221', fontsize=12, color='black')
ax1.patch.set_facecolor('lavender')
ax1.patch.set_alpha(0.8)
ax1.grid(None, color='ghostwhite', linewidth=1.5)
ax1.legend(loc='best')

x = np.linspace(0, gt_xyz_np.shape[0], gt_xyz_np.shape[0])

for idd in range(3):
    ax = fig.add_subplot(int('22{}'.format(idd+2)), xlabel='x', ylabel='uncert')
    uax = np.mean(uncert_xyz_np[:, idd])
    yax = np.linspace(uax, uax, gt_xyz_np.shape[0])
    plt.plot(x, gt_xyz_np[:,idd], color='gray', linestyle='--', label='GT')
    plt.plot(x, pred_xyz_np[:,idd], label='pred')
    plt.plot(x, uncert_xyz_np[:,idd], color='red',linestyle='-', label='uncert')
    plt.plot(x, yax, color='green',linestyle='-.', label='uncert_avg')
    ax.set_title('scene-0221', fontsize=12, color='black')
    ax.patch.set_facecolor('lavender')
    ax.patch.set_alpha(0.8)
    ax.grid(None, color='ghostwhite', linewidth=1.5)
    ax.legend(loc='best')
plt.show()

