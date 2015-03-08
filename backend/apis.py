# -*- coding: UTF-8 -*-
import conekta
import simplejson as json
from extraexceptions import NotEnoughArgsError

conekta.api_key = "key_aZh9hH9bJZ3eBS9tnAqhqw"

# charge = conekta.Charge.create({
#     "currency":"MXN",
#     "amount": 20000,
#     "description":"Stogies",
#     "reference_id":"9839-wolf_pack",
#     "card": "tok_test_visa_4242" 
# })

# charge = conekta.Charge.create({
#     "currency":"MXN",
#     "amount": 20000,
#     "description":"Stogies",
#     "reference_id":"9839-wolf_pack",
#     "card": "4242424242424242" 
# })

# print vars(charge)

def setMessage(args):
    print "holis"
    return "Exito"


def setConektaApiKey(args):
    if args:
        if args["key"]:
            conekta.api_key = args["key"]
            return "Exito"
    
    raise NotEnoughArgsError("setConektaApiKey")


def createAndCharge(args):
    chargeObject = {}
    charge = None

    try:
        if args:
            if "currency" in args:
                chargeObject["currency"] = args["currency"]
            else:
                raise NotEnoughArgsError("createAndCharge")

            if "amount" in args:
                chargeObject["amount"] = int(args["amount"])*100
            else:
                raise NotEnoughArgsError("createAndCharge")

            if "description" in args:
                chargeObject["description"] = args["description"]
            else:
                raise NotEnoughArgsError("createAndCharge")

            if "reference_id" in args:
                chargeObject["reference_id"] = args["reference_id"]
            else:
                raise NotEnoughArgsError("createAndCharge")

            if "card" in args:
                chargeObject["card"] = args["card"]
            else:
                raise NotEnoughArgsError("createAndCharge")

            charge = conekta.Charge.create(chargeObject)
        
            return json.dumps(charge.id)

    except conekta.ConektaError as ce:
        return json.dumps(ce)

    raise NotEnoughArgsError("createAndCharge")

    