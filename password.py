import hashlib

def is_valid_height(password):
    if len(password) < 8:
        print("Erreur: Le mot de passe doit contenir au moins 8 caractères.")
        return False
    return True

def is_valid_maj(password):
    for char in password:
        if char.isupper():
            return True
    print("Erreur: Le mot de passe doit contenir au moins une majuscule.")
    return False

def is_valid_min(password):
    for char in password:
        if char.islower():
            return True
    print("Erreur: Le mot de passe doit contenir au moins une minuscule.")
    return False

def is_valid_digit(password):
    for char in password:
        if char.isdigit():
            return True
    print("Erreur: Le mot de passe doit contenir au moins un chiffre.")
    return False

def is_valid_special(password):
    for char in password:
        if not char.isalnum():
            return True
    print("Erreur: Le mot de passe doit contenir au moins un caractère spécial.")
    return False

if __name__ == "__main__":
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def main():
        while True:
            password = input("Veuillez choisir un mot de passe: ")
            if is_valid_height(password) and is_valid_maj(password) and is_valid_min(password) and is_valid_digit(password) and is_valid_special(password):
                hashed_password = hash_password(password)
                print("Mot de passe valide.")
                print(f"Mot de passe haché: {hashed_password}")
                break

    if __name__ == "__main__":
        main()