
import re

def validar_nome_completo(nome):
    if len(nome) <= 5:
        return False
    
    if ' ' not in nome:
        return False
    
    padrao = r'^[\D]{5,50}$'
    resultado = re.search(padrao, nome)
    if resultado:
        return True
    else:
        return False

def validar_cpf(cpf='70520481240'):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False
    if D(cpf, 10) and D(cpf, 11):
        return True
    else:
        return False
        

    


def D(cpf:str, d=10) ->bool:
    if d==10:
        os_9_d =  cpf[:9]
    else:
       os_9_d =  cpf[1:] 
    Lc = [int(j)for j in os_9_d]
    lm = list(reversed([i for i in range(2, 11)]))
    segundo_list  = [Lc[i] * lm[i] for i in range(9)]
    soma = sum(segundo_list)

    div, resto = soma // 11, soma % 11 
    if resto == 0 or resto == 1:
        d10 = 0
    else:
        d10 = 11 - resto

    if d==10:
        if int(cpf[9]) != d10:
            return False

    elif int(cpf[10]) != d10:
            return False

    return True



