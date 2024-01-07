import statistics

#1 - Aplicar a media
print(statistics.mean([1,2,3,4,5,6]))

#2 - Aplicar a mediana
print(statistics.median([1,2,3,4,4,5]))

#3 - Aplicar a moda
print(statistics.mode([1,2,3,4,4,5,6,7]))

#4 - Desvio padrão
"""
Medida de dispersão do conjunto, ou seja, uma medida 
que indica quão uniformes são os dados do conjunto.

- Quanto mais próximo de 0, significa que os dados
do conjunto estão menos dispersos
"""
print(statistics.stdev([1.1,1.5,2,2.5,3,3.5,4,4.5]))