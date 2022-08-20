import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_data(folders):
    list_df = []
    for folder in folders:
        files = os.listdir(folder)

        df = []
        for file in files:
            file_path = os.path.join(folder, file)
            file_open = open(file_path, "r")
            data = pd.read_csv(file_open, sep=';')

            year = file[-8:-4]
            data['Ano'] = int(year)

            df.append(data)

        df = pd.concat(df, axis=0, ignore_index=True)
        list_df.append(df)

    return list_df

folders = os.listdir()
folders.pop(-1)

data = get_data(folders)

# resultados
gp_0 = data[0].groupby(['Ano'])[['Categoria 0','Categoria 1','Categoria 2','Categoria 3',
                            'Categoria 4','Categoria 5','Categoria 6']].sum()

gp_1 = data[1].groupby(['Ano'])[['Categoria 0','Categoria 1','Categoria 2','Categoria 3',
                            'Categoria 4','Categoria 5','Categoria 6']].sum()

x_axis = np.arange(len(gp_0.index))

plt.figure(1)
plt.plot(x_axis, gp_0['Categoria 4'], label = '4')
plt.plot(x_axis, gp_0['Categoria 5'], label = '5')
plt.plot(x_axis, gp_0['Categoria 6'], label = '6')
plt.xticks(x_axis, gp_0.index)
plt.xlabel("Ano")
plt.ylabel("Número de exames")
plt.title("Número de exames BIRADS 4, 5 e 6")
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x_axis, (gp_0.sum(axis=1)), label='n° de exames')
plt.plot(x_axis, (gp_1.sum(axis=1)), label='n° de pacientes')
plt.xticks(x_axis, gp_0.index)
plt.xlabel("Ano")
plt.ylabel("Número de exames")
plt.title("Número de mamografias por ano")
plt.legend()
plt.show()

print(gp_0)

