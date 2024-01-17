import os
import glob
import pandas as pd

#pasta onde estão os csv's
os.chdir("./BRUTO")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combinar todos os arquivos da lista
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

#exportar para csv
combined_csv.to_csv("lucro_liquido.csv", index=False, encoding='utf-8-sig')

