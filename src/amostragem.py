import pandas as pd
import random
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit


# Criar uma função para obter uma amostra aleatória simples
def amostra_aleatoria_simples(dataset, amostra):
    """
    Amostra aleatória, sem repetição, com parâmetro replace-false,
    em sample. Para obter a mesma amostra, a seed, que aqui é o random_state,
    deve ser igual a um número.
    """
    return dataset.sample(n = amostra, random_state=1)


def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step = intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica



def amostragem_agrupamento(dataset, numero_grupos):
    intervalo = len(dataset) // numero_grupos

    grupos = []
    id_grupo = 0
    contagem = 0
    for _ in dataset.iterrows():
        grupos.append(id_grupo)
        contagem += 1
        if contagem > intervalo:
            contagem = 0
            id_grupo += 1

    dataset['grupo'] = grupos
    random.seed(1)
    #grupo_selecionado = random.randint(0, numero_grupos)
    grupo_selecionado = random.randint(0, numero_grupos - 1) #Atualizado 16/10/2023
    return dataset[dataset['grupo'] == grupo_selecionado]


def amostragem_estratificada(dataset, percentual, atributo):
    split = StratifiedShuffleSplit(test_size=percentual, random_state=1)
    for _, y in split.split(dataset, dataset[atributo]):
        df_y = dataset.iloc[y]
    return df_y


def amostragem_reservatorio(dataset, amostras):
    stream = []
    for i in range(len(dataset)):
        stream.append(i)

    i = 0
    tamanho = len(dataset)

    reservatorio = [0] * amostras
    for i in range(amostras):
        reservatorio[i] = stream[i]

    while i < tamanho:
        j = random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i += 1

    return dataset.iloc[reservatorio]