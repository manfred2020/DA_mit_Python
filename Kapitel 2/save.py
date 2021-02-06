# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:09:17 2021

@author: Manfred Hammerl
"""

def save(df):
    speichern = input("Dataframe \n\n{}\n\n als CSV File speichern? j/n ".format(df.head(3)))
    if speichern == "j":
        file = input("\n Filename: ")
        df.to_csv("C:\\Datenfiles\\{}.csv".format(file), index = False) # 'index = False' ist relevant!
        print('File {} wurde gespeichert'.format(file))
    elif speichern == "n":
        print("\n Ok, nicht speichern...")
    else:
        print("\n Ungültige Eingabe!")
        save(df)