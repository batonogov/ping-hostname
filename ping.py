import socket, os, csv


doc = 'data.csv' # Исходные данные
# Необходимые для нашей задачи данные из исходных данных
помещение = [] # 0
подключенное_устройство = [] # 1
марка = [] # 2
модель = [] # 3
ip = [] # 9
hostname = [] # 15

with open(doc) as f:
    reader = csv.reader(f)
    for row in reader:
        помещение.append(row[0])
        подключенное_устройство.append(row[1])
        марка.append(row[2])
        модель.append(row[3])
        ip.append(row[9])
        hostname.append(row[15])

x = 0
result = {}
while x < len(hostname):
    response = os.system('ping -c 1 ' + hostname[x])
    if response == 0:
        if socket.gethostbyname(hostname[x]) == ip[x]:
            result[ip[x]] = hostname[x] + ';' + помещение[x] + ';' + подключенное_устройство[x] + ';' + марка[x] + ';' + модель[x] + ';' + 'ip адрес совпадает'
        else:
            result[ip[x]] = hostname[x] + ';' + помещение[x] + ';' + подключенное_устройство[x] + ';' + марка[x] + ';' + модель[x] + ';' + 'ip адрес не совпадает'
    else:
        result[ip[x]] = hostname[x] + ';' + помещение[x] + ';' + подключенное_устройство[x] + ';' + марка[x] + ';' + модель[x] + ';' + 'недосутпен'
    x += 1

with open('ping_hostname.csv', 'w') as file:
    for key, val in result.items():
        file.write('{};{}\n'.format(key, val))
