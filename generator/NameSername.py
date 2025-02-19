import random


def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def merge_names(first_names, last_names):
    random_first_name = random.choice(first_names).strip()
    random_last_name = random.choice(last_names).strip()
    return f"{random_first_name} {random_last_name}"

if __name__ == "__main__":
    first_names_file = r"Git_project\generator\names_list.txt"  
    last_names_file = r"Git_project\generator\sername_list.txt"  

    first_names = read_lines_from_file(first_names_file)
    last_names = read_lines_from_file(last_names_file)

    if first_names and last_names:
        random_name = merge_names(first_names, last_names)
        print("Случайное имя и фамилия:", random_name)
    else:
        print("Ошибка: Файлы с именами или фамилиями пусты.")
