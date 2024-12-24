import os
import numpy as np

matrix = np.load('/home/whytech/lab_2/tasks/second_task.npy')

x = []
y = []
z = []

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):

        if matrix[i][j] > 575:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez('/home/whytech/lab_2/results/task_2_solve.npz', x=x, y=y, z=z)
np.savez_compressed('/home/whytech/lab_2/results/task_2_solve_compressed.npz', x=x, y=y, z=z)

first_size =  os.path.getsize('/home/whytech/lab_2/results/task_2_solve.npz')
second_size = os.path.getsize('/home/whytech/lab_2/results/task_2_solve_compressed.npz')

print(f'savez = {first_size}')
print(f'savez_compressed = {second_size}')
print(f'diff = {first_size - second_size}')