import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class Read_Config:
    @staticmethod
    def get_login_url():
        url=config.get('login information','login_url')
        return url

    @staticmethod
    def get_username():
        username=config.get('login information','username')
        return username

    @staticmethod
    def get_password():
        password=config.get('login information','password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username=config.get('login information','invalid_username')
        return invalid_username