#%% 
persona = {'nombre': 'Gabriel', 'edad': 30, 'email': 'gvillacis@vilathi.com'}

#print(persona.get('email'))
#print(persona['email'])

for p in persona.keys():
    print(p)
    
for p in persona.values():
    print(p)
    
for k, v in persona.items():
    print(f'{k}:{v}')

persona['ciudad'] = 'Guayaquil'
persona['ciudad'] = 'Quito'

for k, v in persona.items():
    print(f'{k}:{v}')

persona['apellido'] = 'Villacis'

# %%
