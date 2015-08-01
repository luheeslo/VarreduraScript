# Varredura Script #

Script que a partir de um IP público como entrada, detecta a rede que o IP está inserido e faz uma varredura em todos os hosts desssa rede utilizando o whois e o nmap. Os dados são escritos no arquivo hosts_data.txt. A entrada também aceita um range de IPs, evitando executar o whois.