import pandas as pd


def get_denied(path):
    df = pd.read_excel(path, sheet_name="BD2")

    df_denied = df[df["Conclusao"] == "Indeferido"]

    processes = df_denied["Processo"]
    processes = processes.tolist()
    
    return processes
