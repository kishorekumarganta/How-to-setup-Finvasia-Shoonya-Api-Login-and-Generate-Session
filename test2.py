import config
import logging


from api_helper import ShoonyaApiPy

api = ShoonyaApiPy()  #Create an Object to use
ret = api.login(userid=config.user, password=config.pwd, twoFA=config.factor2, vendor_code=config.vc, api_secret=config.app_key, imei=config.imei)

print(api.get_limits())
#will show my all Limits

print( "  \n ** My Cash Account Limit is ==> ",api.get_limits()['cash']," \n")
#To get my Cash Limit
#for line break in print use  \n


