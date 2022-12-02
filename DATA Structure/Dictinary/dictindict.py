mh=['pune','Mumbai','Nashik']
jh=['Ranchi','Lohardaga']
India={'Maharastra':mh,'Jharkhand':jh}

st1=['xyz','pqr']
st2=['aaa','bbb']
Nepal={'State-1':st1,'State-2':st2}

World={'Country-1':India,'Country-2':Nepal}
for c,v in World.items():
    print(c)
    for country,st in v.items():
        print(country)
        for city in st:
            print(city)
