# Programa ideal para quem esta em fase de cresimento - Recomendado para crianças e adolescentes.
# Esse programa desliga o computador as 10 horas (22:00)
# Licença: GPL
# Autor: Friboquen
# Nota: O script deve ser executado com permissões de adminstrador para funcionar no Linux/MacOS.
# Nota 2: O script deve ser deixado aberto.

import os
import time
from datetime import datetime

# Hora para desligar o computador (22:00)
shutdown_hour = 22
shutdown_minute = 0

def should_shutdown():
    if os.name == 'nt': # Windows
        os.system("shutdown -s -t 0")
    else: # Linux and MacOS
        os.system("sudo shutdown -h now")

print("Programa de desligamento automático iniciado.")
time.sleep(5)
print("O programa irá desligar o computador ás 22:00 horas.")

while True:
    now = datetime.now()
    if now.hour == shutdown_hour and now.minute == shutdown_minute:
        print("Desligando o computador agora, vejo você amanhã!")
        should_shutdown()
        break
    time.sleep(30)  # Verifica a cada 30 segundos

    # End of script
