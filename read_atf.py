import json


def read_atf(process_path):
    with open(process_path, 'r', encoding='utf-8') as f:
        processes = json.load(f)

    atf_process = [process["atf"] for process in processes]

    return atf_process