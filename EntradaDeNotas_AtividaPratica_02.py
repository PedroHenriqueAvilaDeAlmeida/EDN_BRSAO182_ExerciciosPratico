#!/usr/bin/env python
# coding: utf-8

# In[4]:


def ler_nota():
    while True:
        entrada = input("Digite a nota (Entre: 0-10) ou 'fim' para finalizar: ").strip().lower()
        if entrada == 'fim':
            return None
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota fora do intervalo permitido (0-10). Tente novamente.")
        except ValueError:
            print("Essa entrada não é válida. Digite um número ou 'fim'.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def registrar_notas():
    print(" Registrar Notas da Turma")
    notas = []

    while True:
        nota = ler_nota()
        if nota is None:
            break
        notas.append(nota)

    if notas:
        media = calcular_media(notas)
        print(f"\nTotal de notas armazenadas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi digitada.")

# Exec o programa
registrar_notas()


# In[ ]:




