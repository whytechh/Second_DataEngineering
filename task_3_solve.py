import os
import json
import msgpack

with open('/home/whytech/lab_2/tasks/third_task.json', 'r', encoding='utf-8') as file:
    items = json.load(file)

items_dict = {}

for item in items:

    name = item['name']
    price = item['price']

    if name not in items_dict:
        items_dict[name] = {
            'name': name,
            'max_price': price,
            'avg_price': price,
            'count': 1,
            'min_price': price
        }
    else:
        stat = items_dict[name]
        
        if stat['max_price'] < price:
            stat['max_price'] = price

        if stat['min_price'] > price:
            stat['min_price'] = price
        
        stat['avg_price'] += price
        stat['count'] += 1

for name in items_dict:
    stat = items_dict[name]
    stat['avg_price'] /= stat['count']

to_save = list(items_dict.values())

with open('/home/whytech/lab_2/results/task_3_solve.json', 'w', encoding='utf-8') as file:
    json.dump(to_save, file, ensure_ascii=False, indent=1)

with open('/home/whytech/lab_2/results/task_3_solve.msgpack', 'wb') as file:
    msgpack.dump(to_save, file)

json_size = os.path.getsize('/home/whytech/lab_2/results/task_3_solve.json')
msgpack_size = os.path.getsize('/home/whytech/lab_2/results/task_3_solve.msgpack')

print(f'json = {json_size}')
print(f'msgpack = {msgpack_size}')
print(f'diff = {json_size - msgpack_size}')