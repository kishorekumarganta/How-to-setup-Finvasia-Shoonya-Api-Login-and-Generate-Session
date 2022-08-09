import config
import logging


from api_helper import ShoonyaApiPy

api = ShoonyaApiPy()  #Create an Object to use
ret = api.login(userid=config.user, password=config.pwd, twoFA=config.factor2, vendor_code=config.vc, api_secret=config.app_key, imei=config.imei)

while True:
	print(api.get_quotes('NSE','ITC-EQ')['lp']) #to Get LTP

#Current Code will not Accept more than two Scripts Running at Same Time, Gonna upload Tweaked Script to Run Multiple Scripts Here Soon.

