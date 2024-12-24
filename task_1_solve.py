import json
import numpy as np

matrix = np.load('/home/whytech/lab_2/tasks/first_task.npy')

size = matrix.size

matrix_props = {
    'sum': 0,
    'avg': 0,
    'sumMD': 0,
    'avgMD': 0,
    'sumSD': 0,
    'avgSD': 0,
    'max': 0,
    'min': 0
}

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):

        item = matrix[i][j]
        matrix_props['sum'] += item

        if i == j:
            matrix_props['sumMD'] += item

        if j == matrix.shape[1] - i - 1:
            matrix_props['sumSD'] += item

        if matrix_props['max'] < item:
            matrix_props['max'] = item
        
        if matrix_props['min'] > item:
            matrix_props['min'] = item

matrix_props['avg'] = matrix_props['sum'] / size
matrix_props['avgMD'] = matrix_props['sumMD'] / matrix.shape[0]
matrix_props['avgSD'] = matrix_props['sumSD'] / matrix.shape[0]

norm_matrix = matrix / matrix_props['sum']

for key in matrix_props.keys():
    matrix_props[key] = float(matrix_props[key])

with open('/home/whytech/lab_2/results/task_1_solve.json', 'w', encoding='utf-8') as file:
    json.dump(matrix_props, file, indent=1)

np.save('/home/whytech/lab_2/results/task_1_solve.npy', norm_matrix)