from netmiko import ConnectHandler

def configure_router(ip_address, username, password):
    # Crear una conexión al router
    device = {
        'device_type': 'arris_cer',  # Ajusta el tipo de dispositivo según la marca y modelo de tu router
        'ip': ip_address,
        'username': username,
        'password': password,
    }

    # Comandos para configurar el router (puedes personalizarlos según tus necesidades)
    commands = [
        'enable',  # Ingresa al modo privilegiado
        'configure terminal',  # Ingresa al modo de configuración global
        'interface vlan1',  # Por ejemplo, ajusta la interfaz según tu configuración
        'ip address 192.168.0.1 255.255.255.0',  # Por ejemplo, ajusta la dirección IP según tu configuración
        'no shutdown',  # Activa la interfaz
        'exit',  # Sal del modo de interfaz
        'exit',  # Sal del modo de configuración
    ]

    # Iniciar la conexión y enviar comandos
    with ConnectHandler(**device) as conn:
        output = conn.send_config_set(commands)
        print(output)

# Ejemplo de uso
configure_router('192.168.0.1', 'technician', 'Cl4r02ol8')
