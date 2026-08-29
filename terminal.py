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
║          By Miller.                      ║
╚══════════════════════════════════════════╝
""")
opc = print("Que quieres hacer? \n [1] Organizar archivos (carpeta descargas) \n [2] Salir")

opc2 = int(input("Selecciona tu respuesta:"
">>> "))

    

 

if opc2 == 1:
        project.run()
else:
    print("Saliendo...")
    time.sleep(2.0)
    print("Bye-Bye!")
    
    sys.exit()
