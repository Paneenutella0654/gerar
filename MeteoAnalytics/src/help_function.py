import pandas as pd

import pandas as pd

def read_csv_to_json(filepath):
    try:
        df = pd.read_csv(filepath)

        if df.empty:
            return {"error": "Il file CSV è vuoto"}
        
        data = df.to_dict(orient='records')  # Lista di dizionari, una per riga
        
        return {"data": data}  # Puoi modificare la chiave "data" se preferisci
    except Exception as e:
        return {"error": f"Errore nella lettura del file CSV: {str(e)}"}
