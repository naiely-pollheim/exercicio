#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

numero_teste = input("Digite um número para verificação: ")
fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
if numero_teste in fibonacci:
    print(f"O número {numero_teste} pertence à sequência.")
else:
    print(f"O número {numero_teste} não pertence à sequência.")

#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

#utilizei o arquivo xml

import xml.etree.ElementTree as ET
tree = ET.parse('dados.xml')
root = tree.getroot()

faturamento_diario = []
dias_no_mes = 0
faturamento_total = 0
dias_acima_da_media = 0

for row in root.findall('row'):
    valor = float(row.find('valor').text)
    if valor != 0:
        faturamento_diario.append(valor)
        dias_no_mes += 1
        faturamento_total += valor

for valor in faturamento_diario:
    if valor > (faturamento_total / dias_no_mes):
        dias_acima_da_media += 1

print(f"Menor faturamento: R$ {min(faturamento_diario)}")
print(f"Maior faturamento: R$ {max(faturamento_diario)}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")


#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f'{estado}: O percentual é igual a {percentual:.2f}%')

#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite uma string: ")
string_invertida = ""

i = len(string) - 1
while i >= 0:
    string_invertida += string[i]
    i -= 1

print("A string invertida é:", string_invertida)