#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 
#valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que 
#desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
#se o número informado pertence ou não a sequência.

#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente 
#definido no código;


# Encontrando o termo que fica em determinado lugar na sequência de fibonacci
# Necessário definir três variáveis
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

# Se o item for 1 ou 2, printar na tela 1, já que não é possível a aplicação da regra, não tem penúltimo elemento (1, 1, 2)
if (n==1) or (n==2):
    print("1")
#caso não seja 1 ou 2, será aplicada a regra abaixo
else:
    #a variável se inicia em 3, já que passam os dois valores iniciais da sequencia (inicia a contagem no elemento 3)
    count=3
    while count <= n:
        termo = ultimo + penultimo #fórmula fibonacci
        penultimo = ultimo 
        ultimo = termo
        count += 1
    print(termo)