student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    pass

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

name_list = input("Enter name: ").upper()
nato_name = [nato_dict[letter] for letter in name_list]
print(nato_name)

