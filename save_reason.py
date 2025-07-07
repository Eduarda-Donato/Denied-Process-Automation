import pandas as pd
import json

from config import PATH_OUT, JSON_REASON_PATH


data = pd.read_excel(PATH_OUT, sheet_name="BD2")
    
with open(JSON_REASON_PATH, 'r', encoding="utf8") as f:
    data_reason = json.load(f)  

reason_map = {
    obj["eprocesso"]: obj["reason"].replace("reason:","") for obj in data_reason
}

data["Razão do Indeferimento"] = data["Processo"].map(reason_map)

with pd.ExcelWriter(PATH_OUT, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    data.to_excel(writer, sheet_name="BD2", index=False)
