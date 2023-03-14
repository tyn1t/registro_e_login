class Registros:
    
    def __init__(self, nome=None, senha=None):
        self.cadas = False
        self.user_exiten  = False
        self.senha_perfeita = False
        self.nome = nome
        self.senha = senha
    def le_Regis(self): # lê registro  já exiten ou esta cadastrado

        if self.cadas is False:
            self.nome.strip()
    
        with open('Ex\Regis.txt', 'r') as self.cadastrado:

            if self.cadastrado is None:
               self.senha.strip()
            else:
                for use  in self.cadastrado.readlines():
        
                    user, p = use.strip().split(',')
                    if user == self.nome:
                       print("nome do usuário já exiten")
                       self.user_exiten = True
                       break
                if self.cadas is False and self.user_exiten is False:
                   self.senha.strip()
                        
    def Cadastra_user(self):               
        try:
            if self.nome == '' or self.senha is None or (0 > len(self.nome) or 4 <=  len(self.senha)):
                print('Error invalido no registro')
            else:
                if len(self.senha) >= 5 and len(self.senha) <= 12:
                    self.senha_perfeita = True
                    with open('Ex\Regis.txt', 'a') as login:
                        for i in range(1):
                            login.write(f'{self.nome},{self.senha}\n')
                            print('Sucessor... Done')
                            self.cadas = True  
        except:  
            print('tente novamente')

'''Registro email '''               



