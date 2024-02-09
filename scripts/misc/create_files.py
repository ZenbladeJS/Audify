import os

# Don't forget to replace <user> with the actual name of the user folder
directory_name = "C:/Users/<user>/Desktop/files"

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

file_names = [
    "best_books_2023.dart",
    "best_fiction.dart",
    "best_historical_fiction.dart",
    "best_mystery_&_thriller.dart",
    "best_romance.dart",
    "best_romantasy.dart",
    "best_fantasy.dart",
    "best_science_fiction.dart",
    "best_horror.dart",
    "best_young_adult_fantasy_&_science_fiction.dart",
    "best_young_adult_fiction.dart",
    "best_debut_novel.dart",
    "best_nonfiction.dart",
    "best_memoir_&_autobiography.dart",
    "best_history_&_biography.dart",
    "best_humor.dart"
]

for file_name in file_names:
    file_path = os.path.join(directory_name, file_name)
    with open(file_path, 'w') as file:
        file.write("")

print(f"Directory '{directory_name}' and files created successfully.")