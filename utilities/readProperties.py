import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\User\\PycharmProjects\\nopcommerceApp\\Configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')    # obtain baseURL from config.in
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')  # obtain username from config.in
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')  # obtain password from config.in
        return password

    @staticmethod
    def getExcelPath():
        excelPath = config.get('common info', 'excelPath')  # obtain excel path from config.in
        return excelPath
