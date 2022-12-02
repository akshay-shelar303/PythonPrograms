mh={'Pune','Nashik','Mumbai'}
jh={'Ranchi','Lohardaga'}

fmh=frozenset(mh)
fjh=frozenset(jh)

india={fmh,fjh}
for st in india:
    for city in st:
        print(city)
