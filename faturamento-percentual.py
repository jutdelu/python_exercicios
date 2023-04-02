#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
#que cada estado teve dentro do valor total mensal da distribuidora.

faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

soma = sum([67836.43, 36678.66, 29229.88, 27165.48, 19849.53])

print("O valor total do faturamento: ", soma)

saopaulo = 67836.42/soma*100
riodejaneiro = 36678.66/soma*100
minasgerais = 29229.88/soma*100
espiritosanto = 27165.48/soma*100
outros = 19849.53/soma*100

print("O valor do percentual total de SP sobre o faturamento total foi: ", saopaulo)
print("O valor do percentual total de RJ sobre o faturamento total foi: ", riodejaneiro)
print("O valor do percentual total de MG sobre o faturamento total foi: ", minasgerais)
print("O valor do percentual total de ES sobre o faturamento total foi: ", espiritosanto)
print("O valor do percentual total de outros sobre o faturamento total foi: ", outros)