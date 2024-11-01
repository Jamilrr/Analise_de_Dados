# Criar um programa que converta um valor de KM para M.
## Regras 
## 1. O usuário vai inserir o número
## 2. Criar uma função que execute a conversão
## 3. Apresentar para o usuário o valor convertido

print('---Conversor de Km para M---')

km = int(input('Insira o valor em km: '))

## Função para realizar conversão
def Calculo_conversao(km_user):

    calculo = km_user * 1000
    return calculo

resultado = Calculo_conversao(km)
print(f'Resultado em metros:{resultado}')




