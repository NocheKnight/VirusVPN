import time
import requests
import base64
from colorama import Fore, Back, Style
import os

# 0.1 alpha
# Автор - V1rusTeam(Koder) #
# При копипасте пожалуйста указывайте меня как Автора и не удаляйте эти строки
# Telegram - @ArtemZi, @V1rusCode

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


print(Fore.GREEN + f"Выполняется подключение к серверам, пожалуйста подождите..."+Style.RESET_ALL)

vpn_data = requests.get('http://www.vpngate.net/api/iphone/').text.replace('\r', '')
servers = [line.split(',') for line in vpn_data.split('\n')]

labels = servers[1]
labels[0] = labels[0][1:]
servers = [s for s in servers[2:] if len(s) > 1]
#
desired = [s for s in servers]
found = len(desired)
#Впн, поддерживающие OpenVPN
supported = [s for s in desired if len(s[-1]) > 0]

# Красивое меню

clear()

print(Fore.GREEN + f"    ╔╗  ╔╗                ╔╗  ╔╗╔═══╗╔═╗ ╔╗")
print(Fore.GREEN + f"    ║╚╗╔╝║                ║╚╗╔╝║║╔═╗║║║╚╗║║")
print(Fore.GREEN + f"    ╚╗║║╔╝╔══╗╔══╗╔╗╔╗╔══╗╚╗║║╔╝║╚═╝║║╔╗╚╝║")
print(Fore.GREEN + f"     ║╚╝║ ╚║║╝║║╔╝║║║║║══╣ ║╚╝║ ║╔══╝║║╚╗║║")
print(Fore.GREEN + f"     ╚╗╔╝ ╔║║╗║║║ ║╚╝║╠══║ ╚╗╔╝ ║║   ║║ ║║║")
print(Fore.GREEN + f"      ╚╝  ╚══╝╚═╝ ╚══╝╚══╝  ╚╝  ╚╝   ╚╝ ╚═╝{Style.RESET_ALL}")
print(Fore.BLUE+f"                               a.k.a Anti RosCom")
print(Fore.BLUE+f"╔══════════════════════════════════════════════╗")
print(Fore.BLUE+f"║{Style.RESET_ALL} Created By V1rusTeam a.k.a Koder             {Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║{Style.RESET_ALL} Telegram: https://teleg.run/V1rusCode        {Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║{Style.RESET_ALL} Ver: 0.1 alpha                               {Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"{Fore.BLUE}╠══════════════════════════════════════════════╣")
print(Fore.BLUE+f"║ {Style.RESET_ALL}    " + str(len(supported)) + ' of these servers support OpenVPN' + f"{Fore.BLUE}      ║")

CountryList = []

for i in supported:
    if i[5] not in CountryList:
        CountryList.append(i[5])

n = 1
# 48 пробелов
print(Fore.BLUE+f"║ {Style.RESET_ALL}0. Лучший сервер {Fore.BLUE}                            ║")
for i in CountryList:
    print(Fore.BLUE+f"║ {Style.RESET_ALL}" + str(n) + "." + " " + i + " "*((43-len(i))-len(str(n))) + f"{Fore.BLUE}║")
    n += 1
    time.sleep(0.2)

print(Fore.BLUE+f"╠══════════════════════════════════════════════╣")
print(Fore.BLUE+f"║ {Style.RESET_ALL}Для обновления введите '{Fore.GREEN}7777{Style.RESET_ALL}'{Fore.BLUE}                ║")
time.sleep(0.2)
print(Fore.BLUE+f"║ {Style.RESET_ALL}Если вы хотите сообщить о баге или           {Fore.BLUE}║\n║{Style.RESET_ALL} хотите что-то предложить - введите '{Fore.GREEN}007{Style.RESET_ALL}'   {Fore.BLUE}  ║")
print(Fore.BLUE+f"╚══════════════════════════════════════════════╝")

ui = int(input(f"{Style.RESET_ALL}Введите номер страны: "))


if ui != 0 and ui != 7777 and ui != 777:
    country = CountryList[ui-1]
    desired = [s for s in servers if country.lower() in s[5].lower()]
    found = len(desired)
    print('Found ' + str(found) + ' servers for country ' + country)
elif ui == 7777:
    os.system("cd && rm -rf VirusVPN && git clone https://github.com/V1rusTeam/VirusVPN.git")
    print(Fore.BLUE + f"=====================================\n{Fore.GREEN}[INFO]{Style.RESET_ALL}VirusVPN \nбыл успешно обновлён.\n{Fore.GREEN}[INFO]{Style.RESET_ALL}Через 5 секунд он будет\n автоматически запущен\n{Fore.BLUE}=====================================" + Style.RESET_ALL)
    time.sleep(5)
    os.system("cd && cd VirusVPN && python3 VirusVPN.py")
    exit(0)
elif ui == 777:
    print("Пока не добавлено)")
    exit(0)

#

supported = [s for s in desired if len(s[-1]) > 0]
# Выбераем лучший сервер
winner = sorted(supported, key=lambda s: float(s[2].replace(',', '.')), reverse=True)[0]
#

##
# Вывод лучшего сервера и создание файла конфига OpenVPN

clear()

print(Fore.GREEN + f"    ╔╗  ╔╗                ╔╗  ╔╗╔═══╗╔═╗ ╔╗")
print(Fore.GREEN + f"    ║╚╗╔╝║                ║╚╗╔╝║║╔═╗║║║╚╗║║")
print(Fore.GREEN + f"    ╚╗║║╔╝╔══╗╔══╗╔╗╔╗╔══╗╚╗║║╔╝║╚═╝║║╔╗╚╝║")
print(Fore.GREEN + f"     ║╚╝║ ╚║║╝║║╔╝║║║║║══╣ ║╚╝║ ║╔══╝║║╚╗║║")
print(Fore.GREEN + f"     ╚╗╔╝ ╔║║╗║║║ ║╚╝║╠══║ ╚╗╔╝ ║║   ║║ ║║║")
print(Fore.GREEN + f"      ╚╝  ╚══╝╚═╝ ╚══╝╚══╝  ╚╝  ╚╝   ╚╝ ╚═╝{Style.RESET_ALL}")
print(Fore.BLUE+f"                               a.k.a Anti RosCom")
print(Fore.BLUE+f"╔══════════════════════════════════════════════╗")
print(Fore.BLUE+f"║{Style.RESET_ALL} Created By V1rusTeam a.k.a Koder             {Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║{Style.RESET_ALL} Telegram: https://teleg.run/V1rusCode        {Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║{Style.RESET_ALL} Ver: 0.1 alpha                               {Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"{Fore.BLUE}╠══════════════════════════════════════════════╣")
print(Fore.BLUE+f"║{Style.RESET_ALL}{Fore.GREEN}              == Best server ==               {Style.RESET_ALL}{Fore.BLUE}║"+Style.RESET_ALL)
time.sleep(0.2)
print(Fore.BLUE+f"║{Style.RESET_ALL} Username: vpn" + " "*32 + f"{Fore.BLUE}║"+Style.RESET_ALL)
time.sleep(0.2)
print(Fore.BLUE+f"║{Style.RESET_ALL} Password: vpn" + " "*32 + f"{Fore.BLUE}║"+Style.RESET_ALL)
time.sleep(0.2)

pairs = list(zip(labels, winner))

for (l, d) in pairs[:4]:
    print(Fore.BLUE+f"║{Style.RESET_ALL} " + l + ': ' + d + " "*(43-len(l)-len(d)) + f"{Fore.BLUE}║"+Style.RESET_ALL)
    time.sleep(0.2)

#
print(Fore.BLUE+f"║{Style.RESET_ALL} " + pairs[4][0] + ': ' + str(float(pairs[4][1]) / 10 ** 6) + ' MBps' + " "*(38 - len(pairs[4][0]) - len(str(float(pairs[4][1]) / 10 ** 6))) + f"{Fore.BLUE}║"+Style.RESET_ALL)
time.sleep(0.2)
print(Fore.BLUE+f"║{Style.RESET_ALL} " + "Country: " + pairs[5][1] + " "*(36 - len(pairs[5][1])) + f"{Fore.BLUE}║"+Style.RESET_ALL)

time.sleep(0.2)
print(Fore.BLUE+f"╠══════════════════════════════════════════════╣")
print(Fore.BLUE+f"║ {Style.RESET_ALL}Для обновления введите '{Fore.GREEN}7777{Style.RESET_ALL}'{Fore.BLUE}                ║")
time.sleep(0.2)
print(Fore.BLUE+f"║ {Style.RESET_ALL}Если вы хотите сообщить о баге или           {Fore.BLUE}║\n║{Style.RESET_ALL} хотите что-то предложить - введите '{Fore.GREEN}777{Style.RESET_ALL}'   {Fore.BLUE}  ║")
print(Fore.BLUE+f"╚══════════════════════════════════════════════╝")

# Конфиг файл OpenVPN
ui2 = str(input("Создать файл конфигурации OpenVPN? (y/N): "))

if ui2 == "y" or ui2 == "Y" or ui2 == "Д" or ui2 == "д":

    path = pairs[5][1] + ".ovpn"
    # Расшифровка
    ter = []
    qwer = base64.b64decode(winner[-1])

    qwer = list(qwer)
    for i in qwer:
        ter.append(chr(i))

    ter = "".join(ter)


    f = open(path, 'w')
    f.write(ter)
    # f.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
    f.close()
    print(Fore.GREEN + f"Создан файл: " + path + Style.RESET_ALL)

#

