import configparser

key_file = "aes_key.ini"

config = configparser.ConfigParser()
config['Keys'] = {
    'AESKey': ''
}

with open(key_file, 'w') as configfile:
    config.write(configfile)
