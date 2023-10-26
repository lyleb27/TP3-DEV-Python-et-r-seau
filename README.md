# TP3-DEV-Python-et-r-seau
## I. Ping
```
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python ping_simple.py

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=24 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=23 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=25 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=25 ms TTL=114

Statistiques Ping pour 8.8.8.8:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 23ms, Maximum = 25ms, Moyenne = 24ms
0
```

```
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python ping_arg.py 8.8.8.8

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=22 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=27 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=27 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=25 ms TTL=114

Statistiques Ping pour 8.8.8.8:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 22ms, Maximum = 27ms, Moyenne = 25ms
```

```
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python is_up.py 8.8.8.8
UP !
```

II. DNS

```
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python lookup.py ynov.com
L'adresse IP de ynov.com est 104.26.11.233
```
III. Get your IP

```
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python get_ip.py
10.33.48.213
```

IV. Mix

```
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python network.py lookup ynov.com
104.26.11.233
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python network.py ping 8.8.8.8

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=22 ms TTL=114

Statistiques Ping pour 8.8.8.8:
    Paquets : envoyés = 1, reçus = 1, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 22ms, Maximum = 22ms, Moyenne = 22ms
UP !
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python network.py ip
10.33.48.213
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau> python network.py ranlarjan
'ranlarjan' is not an available command. Déso.
PS C:\Users\lebou\TP3-DEV-Python-et-r-seau>
```