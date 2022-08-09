import config
import logging


from api_helper import ShoonyaApiPy

# #enable dbug to see request and responses
# logging.basicConfig(level=logging.DEBUG)

#start of our program
api = ShoonyaApiPy()  #Create an Object to use

#here change prefix every thing to config.+ user like that
ret = api.login(userid=config.user, password=config.pwd, twoFA=config.factor2, vendor_code=config.vc, api_secret=config.app_key, imei=config.imei)
print(ret)

#Thats it we are Succesfully Logged in.

# Only Issue is we can only Run One Instance at a Time Here, cannot Run Multiple.

#Working on it to solve in My Next Repository.