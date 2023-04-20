print ("Qual seu salário?")
salario = float (input())
print ("Insira o valor de uma despesa doméstica sua:")
vlrDesp = float (input())
perc = (vlrDesp * 100) / salario
print ("O o percentual que a despesa representa do seu salário total é de: %.2f%%"% perc)
