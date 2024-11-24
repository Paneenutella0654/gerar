import os
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

def prova_encoding(file_path):

    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Errore generico con encoding {encoding}: {str(e)}")
            continue
    return None

def genera_date_ore(data_inizio, num_ore):
    date_list = []
    data_corrente = data_inizio
    for _ in range(num_ore):
        date_list.append(data_corrente.strftime('%d/%m/%Y %H:%M'))
        data_corrente += timedelta(hours=1)
    return date_list

def concatena_csv_files(cartella_path, testo_colonna1, data_inizio):

    cartella = Path(cartella_path)
    
    dati_files = {}
    max_righe = 0
    
    for file_csv in cartella.glob('*.csv'):
        print(f"\nProcessando file: {file_csv.name}")
        
        df = prova_encoding(file_csv)
        
        if df is not None:
            colonne_richieste = ["ParamNome", "ParamUdm", "Media"]
            if all(colonna in df.columns for colonna in colonne_richieste):
                param_nome = df["ParamNome"].iloc[0]
                param_udm = df["ParamUdm"].iloc[0]
                
                # Salva i dati con un prefisso univoco
                dati_files[param_nome] = {
                    'udm': param_udm,
                    'valori': df["Media"].tolist()
                }
                
                # Aggiorna il numero massimo di righe
                max_righe = max(max_righe, len(df["Media"]))
                
                
            else:
                print(f"{file_csv.name} non contiene tutte le colonne necessarie")
    
    if not dati_files:
        print("Nessun dato valido trovato nei file CSV")
        return None
    

    risultato = pd.DataFrame({
        'Stazione': [testo_colonna1] * max_righe
    })
    
    risultato['Data_Ora'] = genera_date_ore(data_inizio, max_righe)
    
    for param_nome, dati in dati_files.items():
        nome_colonna = f"{param_nome} ({dati['udm']})"
        
        valori = dati['valori'] + [None] * (max_righe - len(dati['valori']))

        risultato[nome_colonna] = valori
    
    return risultato

def main():

    cartella = "C:\\Users\\gerar\\OneDrive\\Desktop\\dati_GIS\\Viggiano"  
    testo_colonna1 = "Nome_Stazione"  
    data_inizio = datetime(2022, 1, 1, 1, 0)  
    
    print(f"Inizio elaborazione dalla cartella: {cartella}")

    df_risultato = concatena_csv_files(cartella, testo_colonna1, data_inizio)
    
    if df_risultato is not None:
        nome_file_output = "risultato_concatenato.csv"
        df_risultato.to_csv(nome_file_output, index=False, encoding='utf-8')
        print(f"\nElaborazione completata. File salvato come: {nome_file_output}")
        print(f"Righe totali: {len(df_risultato)}")
        print("\nPrime righe del risultato:")
        print(df_risultato.head())
        print("\nColonne nel file risultante:")

if __name__ == "__main__":
    main()