x = input('digite algo')
print('É um número?', x.isnumeric())
print('É um alfanumerico (números e letras)?', x.isalnum())
print('É um alfabético (letras)?', x.isalpha())
print('Está em minúsculo?', x.islower())
print('Está em majusculo?', x.isupper())
print('E somente espaco?', x.isspace())
print('Está capitalizada (Possui maiúsculas e minusculas)', x.istitle())