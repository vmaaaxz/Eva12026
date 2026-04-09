# Definición de variables
OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

# Solicitar protocolo al usuario
protocolo = input("Ingrese el nombre del protocolo (OSPF, RIP, EIGRP, BGP): ")

# Convertir a mayúsculas para evitar errores
protocolo = protocolo.upper()

# Evaluación con if / elif / else
if protocolo == "OSPF":
    print("El protocolo OSPF tiene una distancia administrativa de", OSPF)
elif protocolo == "RIP":
    print("El protocolo RIP tiene una distancia administrativa de", RIP)
elif protocolo == "EIGRP":
    print("El protocolo EIGRP tiene una distancia administrativa de", EIGRP)
elif protocolo == "BGP":
    print("El protocolo BGP tiene una distancia administrativa de", BGP)
else:
    print("Protocolo no reconocido")