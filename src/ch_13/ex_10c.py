# merging multiple configuration files
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

# Previously read configuration
print(cfg.get('installation', 'prefix'))

if __name__ == '__main__':
    import os
    # Merge in user-specific configuration
    cfg.read(os.path.expanduser('~/.config2.ini'))
    print(cfg.get('installation', 'prefix'))
    print(cfg.get('installation', 'library'))
    print(cfg.getboolean('debug', 'log_errors'))
    cfg.set('installation', 'prefix', '/tmp/dir')
    print(cfg.get('installation', 'library'))
