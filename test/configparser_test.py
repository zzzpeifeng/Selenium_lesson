import configparser
from selenium import webdriver
import getcwd

config = configparser.ConfigParser()

path = getcwd.getcwd()

file = path+ '/Config/config.ini'

config.read(file)
print(config.get('prod', 'url'))


# config.add_section('login')
# config.set('login', 'username', '1111')
# config.set('login', 'password', '2222')
# with open(file, 'w') as configfile:
#     config.write(configfile)

# config.read(file)
# print(config.get('login', 'username'))
# # import getcwd
# #
# # path = getcwd.getcwd()
# # print(path)


