import pandas as pd


def get_indeferidos(path):
    df = pd.read_excel(path, sheet_name="BD2")

    df_indeferidos = df[df["Conclusao"] == "Indeferido"]

    processes = df_indeferidos["Processo"]
    processes = processes.tolist()
    
    return processes
