def time_to_text(n):
    heures = n // 60
    minutes = n % 60
    return f"{heures} heure(s) et {minutes} minute(s)"

print(time_to_text(133))