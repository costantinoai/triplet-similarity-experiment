import re

in_path = 'test/test_results/triplets/dataset'

print(re.search(r'(mat|txt|csv|npy)$', in_path))