#!/usr/bin/env python
# coding: utf-8

# In[5]:


def calc_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

conta = float(input("Digite o valor total da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta desejada: "))

valor_gorjeta = calcular_gorjeta(conta, porcentagem)

print(f"\nValor da conta: R$ {conta:.2f}")
print(f"Gorjeta ({porcentagem}%): R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {conta + valor_gorjeta:.2f}")


# In[ ]:




