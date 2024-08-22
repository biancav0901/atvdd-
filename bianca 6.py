if delta < 0: # Raízes complexas
 x1= (-b + cmath.sqrt(delta))/(2*a)
 x2= (-b - cmath.sqrt(delta))/(2*a)
 print('Raizes complexas:',x1,' e ',x2)
 elif delta == 0: # Apenas uma raiz
 x = -b / (2*a)
 print('Uma raiz real:', x)
 else: # Duas raízes
 x1 = (-b + math.sqrt(delta)) / (2*a)
 x2 = (-b - math.sqrt(delta)) / (2*a)
 print('Duas raízes reais:', x1, 'e', x2)