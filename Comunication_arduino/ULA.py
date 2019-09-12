import serial as arduino
import time

print("Iniciando..")

# TODO: fazer um metodo para pegar o systema operacional atual

# serial = input("Entrar com a porta: ")  # metodo para pegar a porta atual

# port = arduino.Serial('/dev/ttyUSB0')
port = arduino.Serial('COM22')
port.flush()


def send(x):
    port.write(x)
    # port.timeout(10)
    # port.write(data)


if port.is_open:

    print("porta Valida")

    while True:

        bit_a = input("Digite o A: ")
        bit_b = input("Digite o B: ")
        operation = input("Digite a operacao: ")
        print()

        # TODO: pensar em um metodo para ler o retorno do arduino
        data = f'{bit_a} {bit_b} {operation}\n'.encode()
        print(data)

        print("vlavla1")

        send(data)
        # print()

        print("vlavla2")

        outro = input("...")
        if outro != '':
            break

    print("Fechando porta")
    port.close()

else:
    port.close()
    print("Porta ja em uso")



