# Reading configuration files
from configparser import ConfigParser

cfg = ConfigParser()
print(cfg.read('config.ini'))
print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.getint('server', 'port'))
print(cfg.getint('server', 'nworkers'))
print(cfg.get('server', 'signature'))

if __name__ == '__main__':
    pass
