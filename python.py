#Koska en käyttänyt interaktiivisia elementtejä kuvaajissani niin koin helpoimmaksi tuottaa kuvaajat
#Pythonilla tallentaen kuvaajat kuviksi jotka liitin html koodiin. Jos data olisi vaatinut interaktiivisuutta olisin käyttänyt d3.js kirjastoja.

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

file = "stat_excel.xlsx"
data2 = pd.read_excel(file)
df = data2.T
headers = df.iloc[0]
data  = pd.DataFrame(df.values[1:], columns=headers)
lista = ['2016Q1', '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2',
       '2017Q3', '2017Q4', '2018Q1', '2018Q2', '2018Q3', '2018Q4', '2019Q1',
       '2019Q2', '2019Q3', '2019Q4', '2020Q1', '2020Q2', '2020Q3']

figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k')
plt.plot(lista,data['Palkansaajien tehdyt työtunnit (1 000 000 tuntia) yhteensä'], label =  'Palkansaajien tehdyt työtunnit (1 000 000 tuntia) yhteensä')
plt.xlabel('Neljännesvuosi')
plt.ylabel("Tehdyt työtunnit ( 1 000 000 tuntia)")
plt.title('Tehdyt työtunnit ( 1 000 000 tuntia)')
plt.legend()
plt.annotate('Suomen virallinen tilasto (SVT): Neljännesvuositilinpito [verkkojulkaisu].ISSN=1797-9749. Helsinki: Tilastokeskus [viitattu: 30.12.2020].', (0,0), (580,-30), fontsize=6,
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()
plt.savefig("Figure_1.png")


figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k')
plt.plot(lista,data['Yrittäjien tehdyt työtunnit ( 1 000 000 tuntia)'], label ='Yrittäjien tehdyt työtunnit ( 1 000 000 tuntia)')
plt.plot(lista,data['Palkansaajien tehdyt työtunnit, yksityiset sektorit'], label =  'Palkansaajien tehdyt työtunnit, yksityiset sektorit')
plt.plot(lista,data['Palkansaajien tehdyt työtunnit,julkiset sektorit'], label =  'Palkansaajien tehdyt työtunnit, julkiset sektorit')
plt.xlabel('Neljännesvuosi')
plt.ylabel("Tehdyt työtunnit ( 1 000 000 tuntia)")
plt.title('Tehdyt työtunnit ( 1 000 000 tuntia)')
plt.legend()
plt.annotate('Suomen virallinen tilasto (SVT): Neljännesvuositilinpito [verkkojulkaisu].ISSN=1797-9749. Helsinki: Tilastokeskus [viitattu: 30.12.2020].', (0,0), (580,-30), fontsize=6,
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()
plt.savefig("Figure_2.png")


figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k')
plt.plot(lista,data['Yrittäjien tehdyt työtunnit ( 1 000 000 tuntia)'], label ='Yrittäjien tehdyt työtunnit ( 1 000 000 tuntia)')
plt.xlabel('Neljännesvuosi')
plt.ylabel("Tehdyt työtunnit ( 1 000 000 tuntia)")
plt.title('Tehdyt työtunnit ( 1 000 000 tuntia)')
plt.legend()
plt.annotate('Suomen virallinen tilasto (SVT): Neljännesvuositilinpito [verkkojulkaisu].ISSN=1797-9749. Helsinki: Tilastokeskus [viitattu: 30.12.2020].', (0,0), (580,-30), fontsize=6,
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()
plt.savefig("Figure_3.png")

figure(num=None, figsize=(18, 6), dpi=80, facecolor='w', edgecolor='k')
plt.plot(lista,data['Yrittäjät, kotimaa (1000 henkeä) '], label ='Yrittäjät, kotimaa (1000 henkeä)')
plt.xlabel('Neljännesvuosi')
plt.ylabel("Yrittäjät, kotimaa (1000 henkeä) ")
plt.title('Yrittäjät, kotimaa (1000 henkeä) ')
plt.legend()
plt.annotate('Suomen virallinen tilasto (SVT): Neljännesvuositilinpito [verkkojulkaisu].ISSN=1797-9749. Helsinki: Tilastokeskus [viitattu: 30.12.2020].', (0,0), (580,-30), fontsize=6,
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()
plt.savefig("Figure_4.png")
