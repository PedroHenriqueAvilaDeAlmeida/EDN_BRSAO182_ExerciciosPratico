#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Calculadora Exercício Prático 1 - Pedro Henrique Ávila de Almeida - 19-05-2025 v1

def calculadora():
    print("=== Calculadora PH BRASO182 ===")

    while True:
        try:
            operacao = input("Escolha o tipo da operação (+, -, *, /): ")
            
            if operacao not in ['+', '-', '*', '/']:
                print("Operação inválida. Use um desses operadores: +, -, * ou /.")
                continue

            n1 = float(input("Entre com o seu primeiro número: "))
            n2 = float(input("Entre com o seu segundo número: "))

            if operacao == '+':
                resultado = n1 + n2
            elif operacao == '-':
                resultado = n1 - n2
            elif operacao == '*':
                resultado = n1 * n2
            elif operacao == '/':
                if n2 != 0:
                    resultado = n1 / n2
                else:
                    print("Infelizmente deu Erro: Divisão por zero não é permitida.")
                    continue  # volta para o início do loop

            print(f"Resultado: {resultado}")
            break  # sai do loop após uma operação bem-sucedida

        except ValueError:
            print("Erro: Acho que se enganou. Digite apenas números!")

# Exec a calculadora
calculadora()


# In[ ]:





# In[ ]:





# In[ ]:




