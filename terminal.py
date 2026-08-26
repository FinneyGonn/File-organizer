import project
import sys
import time

print("""
╔══════════════════════════════════════════╗
║                                          ║
║      ██████╗ ██████╗  ██████╗            ║
║     ██╔═══██╗██╔══██╗██╔════╝            ║
║     ██║   ██║██████╔╝██║  ███╗           ║
║     ██║   ██║██╔══██╗██║   ██║           ║
║     ╚██████╔╝██║  ██║╚██████╔╝           ║
║      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝            ║
║                                          ║
║            F I L E   O R G A N I Z E R   ║
║                                          ║
╚══════════════════════════════════════════╝
""")
opc = int(input("Que quieres hacer? 1. Organizar archivos (carpeta descarga) 2. Salir"))

if opc == 1:
    project.run()
else:
    print("Saliendo...")
    time.sleep(2.0)
    print("Bye-Bye!")
    
    sys.exit()
