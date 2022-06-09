import socket

arquivo = open('hosts.txt', 'r')
saida = open('saida.txt', 'w')

hosts = arquivo.readlines()
i = 0

while i < 3:  ## Definir o número de hosts do teste
  try: 
    ip = socket.gethostbyname(hosts[i].rstrip())
  except:
    saida.writelines(hosts[i].rstrip("\n") + " " + "ERRO AO OBTER IP")
    saida.writelines("\n")
  finally:
    print(ip)
    saida.writelines(hosts[i].rstrip("\n") + ";" + ip)
    saida.writelines("\n")
    i += 1

arquivo.close() 
saida.close()
