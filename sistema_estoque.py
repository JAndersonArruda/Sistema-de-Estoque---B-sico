import pickle

# menu do sistema
dic = {}
try:
  file = open("stoque.json",'rb')
  dic = pickle.load(file)
except Exception as e:
  open("stoque.json","w")

def sistema_estoque():
  print('--**Sistema de Estoque**--')
  print('\t1-Criar')
  print('\t2-Remover')
  print('\t3-Encerrar')
  
  opcao = int(input('Digite uma opção: '))
  return opcao

# opeções do sistema
def criar():
  print('\n-->Opção de Criação:')
  estoq = int(input('\t--->Número do Estoque:'))
  produto = input('\t--->Nome do Produto: ')
  quantidade = int(input('\t--->Quantidade do Produto: '))
  dic[estoq] = {'Produto':produto,'Quantidade':quantidade}
  
  file = open("stoque.json",'wb')
  pickle.dump(dic,file)
  file.close()
  
  return dic[estoq]

def remover():
  print('\n-->Opção de Remoção:')
  retirar = int(input('\t--->Número do Estoque: '))
  
  return dic.pop(retirar)



if __name__ == "__main__":
    cond = True
    while(cond):
        opcao = sistema_estoque()
        if(opcao == 1):
            resultado = criar()
            print(f'--->Estoque criado com sucesso\n')
        elif(opcao == 2):
            resultado = remover()
            print(f'--->{resultado} revomovido.\n')
        elif(opcao == 3):
            cond = False
            print('\n--Você escolheu encerrar o programa--')
        else:
            print('\n--Opção Inválida--')

    print(f"\n\t--------------------------ESTOQUE------------------------\n\n{dic}\n")
    # for listDic in dic :
    #     print(listDic)