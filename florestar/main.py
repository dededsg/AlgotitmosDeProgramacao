import mysql.connector
from mysql.connector import Error

#Cria objeto
class Planta:
  def __init__(self, nome, temperatura, iluminacao, umidade, solo):
    self.nome = nome
    self.temperatura = temperatura
    self.iluminacao = iluminacao
    self.umidade = umidade
    self.solo = solo
  
#####################################

def temperaturaPlanta(temperatura, temperaturaBD):
  temp = temperaturaBD
  if temperatura < temperaturaBD:
    return f'A temperatura está baixa, recomenda-se por a planta em um local com temperatura média de {temp}'
  elif temperatura == temperaturaBD:
    return "A temperatura está perfeita"
  elif temperatura > temperaturaBD:
    return f'A temperatura está elevada, recomenda-se por a planta em um local com temperatura média de {temp}'
  else:
    print("++++ERROR++++")
  
def iluminacaoPlanta(iluminacao, iluminacaoBD):
  if iluminacaoBD == iluminacao:
    return "A iluminação da sua planta está ideal"
  elif iluminacaoBD != iluminacao:
    return f'Recomenda-se mover sua plnata de local de forma a ficar com  iluminção {iluminacaoBD}'
  else:
    print("++++ERROR++++")
      
def umidadePlanta(umidade, umidadeBD):
  if umidade == umidadeBD:
    return f'A umidade da sua planta está adequada.'
  elif umidade != umidadeBD:
    return f'A rega da sua planta não está ideal recomenda regar {umidadeBD} vezes na semana.'
  else:
    print("+++++ERROR+++++")
      
def soloPlanta(solo, soloBD):
  if solo == soloBD:
    return f'O tipo de solo está ideal procure mante-lo assim!'
  elif solo != soloBD:
    return f'O tipo de solo não está ideal procure por a planta na {soloBD}'
  
def rotaVerifica(rota):
  if rota == "S" :
    return True
  elif rota == "N":
    return False
  else:
    return True
###############banco de dados###############


def consultar(connection, nome_planta):
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return None

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM plantas WHERE nome = %s", (nome_planta,))
        planta = cursor.fetchone()
        return planta
    except Error as e:
        print(f"Ocorreu um erro ao executar a consulta: {e}")
        return None
############################

inicio = True
 
while inicio:
   
  verifica = input("Deseja iniciar S ou N: ")
  inicio = rotaVerifica(verifica.upper())

  if inicio:
    nome = (input("Digite o nome da sua planta: "))
    plantadb = (consultar(mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Dededsg@05062005",
          database = "crudpontotrack"
        ), nome))
    if(plantadb != None):  
      temp = int(input("Digite a temperatura do ambiente em que sua planta está: "))
      print("Digite a exposição média ao sol da sua planta")
      ilum = (input("Exposição direta, indireta ou nula: "))
      umid = input("Digita quantas vezes rega a planta na semana: ")
      print("Digite o tipo de solo em que sua planta está")
      solo = input("areia, terra, argila, pedra ou água: ")
      planta = Planta(nome.upper(), temp, ilum.upper(), umid, solo.upper())
      print(planta.temperatura)

      print(" ")
      print("+++++|CULTIVAR|+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print(" ")
    
      temperaturaResult = temperaturaPlanta(planta.temperatura, plantadb[1])
      print(temperaturaResult)
  
      iluminacaoResult = iluminacaoPlanta(planta.iluminacao, plantadb[2])
      print(iluminacaoResult)
  
      umidadeResult = umidadePlanta(planta.umidade, plantadb[4])
      print(umidadeResult)
  
      soloResult = soloPlanta(planta.solo, plantadb[3])
      print(soloResult)
    else:
      print("+++++++++++|Planta não encontrada|+++++++++")

print(" ")
print("+++++|FIM|+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(" ")




  
  