def truncate_string(x,d): return float(str(x)[:-(len(str(x).split('.')[1])-d)])
print(truncate_string(43.672947642, 3))

def truncate_numerical(x,d): return int(x * 10 ** d) / 10 ** d
print(truncate_numerical(2.874751458, 5))

