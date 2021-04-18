from random import randint as rand
yes_answers = "SIM_YES_Y_S"
no_ansewrs = "NAO_NÃO_NOP_NO"
result = []
while True:
  inp = input("Você gostaria de jogar o dado?\nSua resposta: ")
  if inp.upper() in yes_answers:
    oup = rand(1,6)
    result.append(oup)
    print(oup,"\n")
    continue
  elif inp.upper() in no_ansewrs:
    print("\nEsperamos que você volte para girar o dado")
    while True:
      if len(result) != 0:
        show_result = input(f"Você deseja ver informações das {len(result)} vezes que você girou o dado?\nSua resposta: ")
      else:
        break
      if show_result.upper() in yes_answers:
        for i in set(result):
          if result.count(i) > 1:
            print(f"{i} caiu {result.count(i)} vezes")
          else:
            print(f"{i} caiu {result.count(i)} vez")
        break
      elif show_result.upper() in no_ansewrs:
        break

    break
  else:
    print("Que tal tentar digitar: 'sim' ou 'não' \n")
    
close = input("press any key to close the program")
