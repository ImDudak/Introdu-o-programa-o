user = input("Digite o username: ") 
password = input("Digite a senha: ")
while password == user:
  password = input("Digite uma senha diferente do username: ")
else:
  print("Dados salvos com sucesso.")