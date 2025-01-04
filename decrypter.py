import os
import pyaes

file_name = 'teste.txt.ransomwaretroll'
if os.path.exists(file_name):
    try:
        # Abrir arquivo
        file = open(file_name, 'rb')
        file_data = file.read()
        file.close()

        # Chave para descriptografar
        key = b'testeransomware1'
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover arquivo
        os.remove(file_name)

        # Gerar novo arquivo
        new_file = 'teste.txt'
        with open(new_file, 'wb') as new_file:
            new_file.write(decrypt_data)

        print("arquivo descriptografado")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
else:
    print(f"Arquivo {file_name} não encontrado.")
