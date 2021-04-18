from random import randint as rand
random_number = rand(10, 100)
while True:
  try:
    inp = int(input("Chute um número: \n"))
    if inp > random_number:
      print("Você chutou um número que está acima do número correto.")
      continue
    elif inp < random_number:
      print("Você chutou um número que está abaixo do número correto.")
      continue
    else:
      print("Parabéns, você acertou!")
      break
  except ValueError:
    print("Oops, parece que você forneceu um valor inválido, tente fornecedor número inteiro.")

close = input("press any booton to close te program\n")
