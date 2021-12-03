# prompting for a password at runtime
import getpass

user = getpass.getuser()
passwd = getpass.getpass()


def svc_login(user_, passwd_):
    if user_ and passwd_:
        return True
    return False


if __name__ == '__main__':
    svc_login(user, passwd)
