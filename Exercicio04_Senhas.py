#!/usr/bin/env python
# coding: utf-8

# In[7]:


def validar_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("Senha menor do que o esperado")
        return False

    # Verifica se contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        print("Senha não contém número")
        return False

    return True

# Loop principal
while True:
    senha = input("Digite a senha ou 'sair': ")

    if senha.lower() == "sair":
        print("Encerrando...")
        break

    if validar_senha(senha):
        print("Senha válida")
        break
    else:
        print("Senha inválida. Tente novamente.")
                     
                     


    

