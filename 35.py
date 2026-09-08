c ={'a': 10, 'b': 20, 'c': 30}

print(sorted( [ (k, v) for k, v in c.items() ], key=lambda x: x[1], reverse=True))

[('c', 30), ('b', 20), ('a', 10)]