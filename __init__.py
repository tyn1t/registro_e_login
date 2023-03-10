from Registro import Registros
from login import login
def valida_int(mensagen, min, max):
    try:
        valor = int(input(mensagen))
        if valor >= min and valor <= max:
            return valor
        else: 
            return f'valor esta abaixo do min ou cima do max'
    except:
        print('Error')
        

if __name__ =="__main__":
    while True:
        print("""
            0 - sair
            1 - login
            2 - Registro
    """)
        op = valida_int('Escolha:',0,2)
        if op == 0:
            break
        elif op == 1:
            LOGIN = login()
            if LOGIN:
                print('BEM Vindo')
        elif op == 2:
            R = Registros()
            R.le_Regis()
            R.Cadastra_user()
        
        