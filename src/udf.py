import json
from datetime import datetime
from dateutil import parser
import logging


def clean_data(message):

    logging.info(message)
    logging.info(type(message))

    message = json.loads(message)
    logging.info(message)
    logging.info(type(message))
    logging.info('-------------------------------------')

    message['manufacturing_year'] = message['year']
    message['sale_year'] = parser.parse(message['saledate']).year
    all(map(message.pop,
                ['year', 'vin', 'state', 'condition', 'odometer', 'color', 'interior', 'seller', 'mmr', 'saledate']))

    return json.dumps(message)


# message = {"data":
#                json.dumps([{"year": 1982, "make": None, "model": None, "trim": None, "body": None,
#                             "transmission": "automatic", "vin": "1g1ay0786c5123682", "state": "ca", "condition": 2.0,
#                             "odometer": 85738.0, "color": "gold", "interior": "gray",
#                             "seller": "livermore toyota and livermore scion", "mmr": 6175.0, "sellingprice": 5000.0,
#                             "saledate": "Wed Jan 28 2015 04:30:00 GMT-0800 (PST)"},
#                            {"year": 1982, "make": None, "model": None, "trim": None, "body": None,
#                             "transmission": "automatic", "vin": "wdbba45a0cb017970", "state": "pa", "condition": 4.0,
#                             "odometer": 18404.0, "color": "white", "interior": "gray", "seller": "adcock brothers inc",
#                             "mmr": 3675.0, "sellingprice": 20500.0,
#                             "saledate": "Thu Jun 11 2015 02:00:00 GMT-0700 (PDT)"}]).encode('utf-8')
#            }
# print(clean_data(message))
