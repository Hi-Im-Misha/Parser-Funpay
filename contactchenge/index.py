import re

def update_number(filename, original_num, changed_num):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            match = re.search(rf"(\+?){original_num}(\d*)?(\d{{7}})\b", line)
            if match:
                plus_sign = match.group(1)  
                last_7_digits = match.group(3)  
                new_number = f"+{changed_num}{last_7_digits}" if not plus_sign else f"{changed_num}{last_7_digits}"
                
                line = re.sub(rf"{original_num}\d*", new_number, line)  
            
            file.write(line)

filename = '' # File path
original_num = input('Which number should I change? ')
changed_num = input('To which number should I change? ')

update_number(filename, original_num, changed_num)
