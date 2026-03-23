
def diagnostico_ping():
    import subprocess
    try:
        resultado = subprocess.run(["ping", "-c", "8", "8.8.8.8"], check = True)
        print("Conectividad OK")
    except subprocess.CalledProcessError:
        print("Error de conectividad")
    except FileNotFoundError:
        print("Comando 'ping' no disponible")
    finally:
        ("Diagnostico Finalizado")

diagnostico_ping()         