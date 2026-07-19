import paramiko


def configure_vm(ip, port, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, port=port, username=user, password=pwd)

        ssh.exec_command("chmod 777 .")

        sftp = ssh.open_sftp()
        sftp.put("resources.txt", "resources.txt")
        sftp.put("template.gdbinit", ".gdbinit")
        sftp.close()

        print("Uploaded resources.txt and .gdbinit!")

    finally:
        ssh.close()


if __name__ == "__main__":
    ip = input("IP [127.0.0.1]: ").strip() or "127.0.0.1"
    port = int(input("Port [8002]: ").strip() or 8002)
    user = input("User [level0]: ").strip() or "level0"
    pwd = input("Password [level0]: ").strip() or "level0"

    configure_vm(ip, port, user, pwd)
