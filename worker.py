from task import add

try:
    result = add.delay(4, 6)
    print(f'Task result: {result.get(timeout=10)}')
except Exception as e:
    print(e)

# python3 worker.py