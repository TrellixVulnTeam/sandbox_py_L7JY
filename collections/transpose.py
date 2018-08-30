from pprint import pprint as pp

ll = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

pp(ll)

# transpose
pp(list(zip(*ll)))
