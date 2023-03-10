class Registros:
    
    def __init__(self):
        self.cadas = False
        self.user_exiten  = False
        
    def le_Regis(self): # lê registro  já exiten ou esta cadastrado

        if self.cadas is False:
            self.nome = input('Digite seu user: ').strip()
    
        with open('regis.txt', 'r') as self.cadastrado:

            if self.cadastrado is None:
               self.senha = input('digite um Senha: ').strip()
            else:
                for use  in self.cadastrado.readlines():
                    print('ok')              
                    user, p = use.strip().split(',')
                    if user == self.nome:
                       print("nome do usuário já exiten")
                       self.user_exiten = True
                       break
                if self.cadas is False and self.user_exiten is False:
                   self.senha = input('digite um Senha: ').strip()
                        
    def Cadastra_user(self):               
        try:
            if self.nome is None or  self.senha is None or (0 > len(self.nome) and 6 <= len(self.senha)):
                print('Error invalido no registro')
            else:
                if len(self.senha) >= 5 and len(self.senha) <= 12:
                    with open('regis.txt', 'a') as login:
                        for i in range(1):
                            login.write(f'{self.nome},{self.senha}\n')
                            print('Sucessor... Done')
                            self.cadas = True  
        except:  
            print('tente novamente')
                



