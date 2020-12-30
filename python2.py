import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from textwrap import wrap

file = "palkka_muutos.xlsx"
data = pd.read_excel(file)
df = data.T
headers = df.iloc[0]
new_df  = pd.DataFrame(df.values[1:], columns=headers)
lista = ["muutos Q1->Q2","muutos Q2->Q3", "muutos Q1->Q3"]

ind = ['Yhteensä', 'Toimialat yhteensä, yksityiset sektorit',
       'Toimialat yhteensä, julkiset sektorit',
       'Maatalous, metsätalous ja kalatalous', 'Koko teollisuus', 'Teollisuus',
       'Rakentaminen',
       'Kauppa, kuljetus ja varastointi, majoitus- ja ravitsemistoiminta',
       'Informaatio ja viestintä', 'Rahoitus- ja vakuutustoiminta',
       'Kiinteistöalan toiminta',
       'Ammatillinen, tieteellinen ja tekninen toiminta, hallinto- ja tukipalvelutoiminta',
       'Julkinen hallinto, koulutus, terveys- ja sosiaalipalvelut',
       'Taiteet, viihde ja virkistys; muut palvelut']

labels = [ '\n'.join(wrap(l, 20)) for l in ind ]
palkki1 = data["2020Q2"].tolist()
palkki2 = data["2020Q3"].tolist()
r = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

leveys = 1
figure(num=None, figsize=(8, 12), dpi=80, facecolor='w',  edgecolor='k')
fig, ax = plt.subplots()
fig.subplots_adjust(left=0.4)
plt.barh(r, palkki1, color='y', edgecolor='white', label = "muutos Q1->Q2")
plt.barh(r, palkki2, left=palkki1, color='#6c3376', edgecolor='white', label = "muutos Q2->Q3")

plt.yticks(r, labels, fontsize=6)
plt.ylabel("toimialat")
plt.xlabel("Palkkojen muutos toimialoittain [%]")
plt.annotate('Suomen virallinen tilasto (SVT): Neljännesvuositilinpito [verkkojulkaisu].ISSN=1797-9749. Helsinki: Tilastokeskus [viitattu: 30.12.2020].', (0,0), (-100,-32), fontsize=6,
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.legend()
plt.show()

plt.savefig("Figure_7.png", bbox_inches='tight')
