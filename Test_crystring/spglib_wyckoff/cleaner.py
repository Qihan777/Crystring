import numpy as np
import pandas as pd

def cleaner(data:dict):
    d = {}
    current_key = None
    for row in data:
        i = row.replace(":"," ").split()
        try:
            int(i[0])
            current_key = f"{i[0]} {i[1]}"
            d[current_key] = i
        except ValueError:
            d[current_key] += i
    return d

if __name__ == '__main__':
    file_path = 'spglib_wyckoff_raw.csv'
    wyckoff_df = pd.read_csv(file_path)

    data_dict = {}
    for row in wyckoff_df.iloc[:, 0]:
        if not str(row).startswith(":"):
            i = row.replace(":", " ").split()
            current_key = f"{i[0]}, {' '.join(i[1:])}"

            data_dict[current_key] = []
        else:
            data_dict[current_key].append(row)

    clean_data = []
    for i in data_dict.keys():
        tempdata = cleaner(data_dict[i]).values()
        for k in tempdata:
            k += [i]
            joined_elements = ' '.join(k[3:-1])
            k = k[:3] + [joined_elements] + k[-1:]
            clean_data.append(k)

    df = pd.DataFrame(np.array(clean_data),
                      columns=["Multiplicity", "Wyckoff letter", "Sitesymmetry", "Coordinates", "info"])

    df[['Hall number', 'Info']] = df['info'].str.split(',', expand=True, n=1)
    df.drop('info', axis=1, inplace=True)

    df.to_csv("spglib_wyckoff.csv", index=False)