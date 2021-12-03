# writing to existing configuration file
import sys
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config2.ini')
cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')
cfg.write(sys.stdout)

if __name__ == '__main__':
    pass
