
def login():
    nome = input('nome :')
    senha = input('Senha :')
    if nome is None and senha is None:
        print('Erro no login tente novamente ok')
    else:
        with open('regis.txt', 'r', encoding='utf-8') as username:
            for user in username.readlines():
                try:
                    user1, password = user.strip().split(',')
                    if user1 == nome:
                        if password == senha:
                            print('Sucessor Login...')
                except:
                    print("Usuário não existe")


