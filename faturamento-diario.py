#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

faturamento = [100, 135, 320, 520, 420, 0, 0, 87, 230, 250, 308, 854, 0, 0]
faturamento.sort()
print ("O faturamento ordenado foi: ", faturamento)
soma = sum([100, 135, 320, 520, 420, 0, 0, 87, 230, 250, 308, 854, 0, 0])
media = sum([100, 135, 320, 520, 420, 87, 230, 250, 308, 854,])/10


print("O faturamento total foi: ", soma)
print ("O menor faturamento foi: ", faturamento[0])
print ("O maior faturamento foi: ", faturamento[13])
print ("A média de vendas foi: ", media)
print ("Os valores maiores que a média foram: ", faturamento[13], faturamento[12], faturamento[11])










