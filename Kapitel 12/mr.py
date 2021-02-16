# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:01:33 2021

Function:
    mr - multiple response
    
Author:
    Manfred Hammerl

https://github.com/manfred2020

"""

__version__ = "0.1.0, from 16th February 2021"

def mr(df, *col, count = 1, save = False):
    
    """
    NAME:
        mr (multiple response)
    
    DESCRIPTION:
        eine kleine Funktion zur Auswertung von Mehrfachantworten
        
    Parameters:
        df : Dataframe
        col : string
              Variablen, die in die Auswertung einbezogen werden sollen
        count : int, float
                Wert, der gezählt/ausgewertet werden soll
        save : bool
               True: Outputtabelle wird in Zwischenablage kopiert
               False: Outputtabelle wird nicht in Zwischenablage kopiert (default)
    
    Returns:
        Dataframe und Grafik
        
    """
    
    import pandas as pd
    
    columns = [] # leere Liste erstellen
    
    for col in col:
        columns.append(col) # alle eingegebenen Variablen in Liste einfügen
        
    length = len(df.index) # Anzahl der Zeilen im Dataframe ermitteln
    width = len(df.columns) # Anzahl der Variablen im Dataframe ermitteln
    cells = (length*width) # Anzahl der Zellen im Dataframe ermitteln
    
    mr_set = (df[columns] == count).sum(axis = 0).sort_values(ascending = True) # eine Basisauswertung, zwecks der Reihenfolge für alle weiteren
    mrset = mr_set.sum(axis = 0) # Summe der gesamt abgegebenen Antworten ermitteln
    
    finalset = pd.DataFrame({"Anzahl d Nennungen" : mr_set,
                          "Prozent" : ((mr_set/length)*100).round(2),
                          "Prozent d mögl. Nennungen" : ((mr_set/cells)*100).round(2),
                          "Prozent d tatsächl. Nennungen" : ((mr_set/(mrset))*100).round(2)}).fillna(0) # fillna() wegen Division durch 0
        
    style = finalset.style.format({"Anzahl d Nennungen" : "{:.0f}",
                              'Prozent' : '{:.1f}%',
                              "Prozent d mögl. Nennungen" : "{:.1f}%",
                              "Prozent d tatsächl. Nennungen" : "{:.1f}%"})
    
    if save:
        finalset.to_clipboard(decimal = ",")
        print("Ergebnistabelle wurde in die Zwischenablage zur weiteren Verwendung kopiert")
        
    if mrset > 0:
        import matplotlib.pyplot as plt    
        from matplotlib.ticker import FormatStrFormatter    
        ax = finalset[['Prozent d mögl. Nennungen', 'Prozent d tatsächl. Nennungen',
                       'Prozent']].plot.barh(figsize=(8.5,4.5))    
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.f%%'))
        plt.legend(loc='lower right')
    
    from IPython.display import display
    
    return display(style)