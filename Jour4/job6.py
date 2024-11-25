def code(langage):
    if langage == 'Javascript':
        return 'Tu es un web developpeur'
    elif langage == 'Python':
        return 'Tu es un developpeur IA'
    elif langage == 'Java':
        return 'Tu es un developpeur logiciel'
    elif langage == 'ReactJS':
        return 'Tu es un developpeur mobile'
    else:
        return 'Un jour je serais le meilleur developpeur...'
    
print(code('Python'))