import_file = "allow_list.txt"

# abre e lê o arquivo da allow list
with open(import_file, "r") as file:
    ip_addresses = file.read()

    
# converte a string de IPs em uma lista
ip_addresses = ip_addresses.split()

# lista de IPs que devem ser revogados
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# itera sobre a lista de remoção para filtrar a allow list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# converte a lista de volta para string com quebras de linha
ip_addresses = "\n".join(ip_addresses)

# reescreve o arquivo com a lista atualizada
with open(import_file, "w") as file:
    file.write(ip_addresses)
