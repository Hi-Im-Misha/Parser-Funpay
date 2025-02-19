import random
import string

def read_words_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

words_list = read_words_list(r'Git_project\generator\words_list.txt')

def generate_login(min_length=6, max_length=12, min_words=1, max_words=None):
    max_words = max_words or len(words_list)
    
    login_length = random.randint(min_length, max_length)
    words_count = random.randint(min_words, max_words)
    selected_words = random.sample(words_list, min(words_count, len(words_list)))
    

    total_words_length = sum(len(word) for word in selected_words)
    

    if total_words_length > max_length:
        selected_words = selected_words[:max_length]
        total_words_length = sum(len(word) for word in selected_words)
    
    login_length -= total_words_length
    
    characters = string.ascii_letters + string.digits
    login = ''.join(random.choice(characters) for _ in range(login_length))
    
    for word in selected_words:
        position = random.randint(0, len(login))
        login = login[:position] + word + login[position:]
    
    login_length = len(login) 
    

    for _ in range(random.randint(1, max(1, min(login_length, login_length // 2)))):
        position = random.randint(0, len(login))
        login = login[:position] + random.choice(string.digits) + login[position:]
    
    login = login.replace(' ', '')  
    
    return login[:max_length] 

if __name__ == "__main__":
    generated_login = generate_login()
    print("Сгенерированный логин:", generated_login)
