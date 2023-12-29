a={'name':'abc'}
b=a
c=a.copy()
a['name']='xyz'
print(b['name'],c['name'])

#xyz abc
#In reference it will change
#In copy it won't change