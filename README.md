# How to setup Finvasia Shoonya Api Login and Generate Session

# I am single, Unable to fetch Time Here, So Taking too Much Time for every release.


First Download Official Finvasia Shoonya API Code From Their 

github Link:
https://github.com/Shoonya-Dev/ShoonyaApi-py

****

Install Python and one Text Editor Like Sublime in Your System.

To Install any Python packages  First Press " Windows+R"  > Enter "CMD"  > "pip install pandas"

****

Now create a config.py file to store passwords.
Save Below Details in config.py file


```
#credentials
user    = <uid>
pwd     = <password>
factor2 = <2nd factor>
vc      = <vendor code>
app_key = <secret key>
imei    = <imei>

```

Will Get Above Details From Finvasia Prism Login or contact them at support

****
## Once Done

to build this package and install it on your server

go to shoonya API Extracted folder where requirements.txt is there, 

Right Click > Open Terminal and Type

``` pip install -r requirements.txt ```


****
## Copy api_helper.py file to working folder from shoonya Api. 

****
## Create test.py file to working folder. 

Install NorenRestAPI.whl from Dist Folder of Shoonya API Code

``` pip install NorenRestApiPy-0.0.20-py2.py3-none-any.whl ```

```python
import config
from api_helper import ShoonyaApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = ShoonyaApiPy()  #Create an Object to use


ret = api.login(userid=config.user, password=config.pwd, twoFA=config.factor2, vendor_code=config.vc, api_secret=config.app_key, imei=config.imei)
print(ret)
```





****















## Author

Ganta Kishore Kumar

****

## License

Copyright (C) of API belong to API Owners.

****





