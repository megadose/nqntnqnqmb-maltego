from MaltegoTransform import *
from nqntnqnqmb import *
import random
with open('./config.json') as config_file:
    config = random.choice(json.load(config_file))

trx = MaltegoTransform()

profileToSearch=str(sys.argv).split('Linkedin.Profile.Url=')[1].replace("'","").replace("]","").split('#Random=')[0]
profileSearch=profileToSearch
data = GetContactInformations(profileSearch,config["JSESSIONID"],config["li_at"])

if data["birthDate"] !=None:
    trx.addEntity("megadose.Birthday", data["birthDate"])
if len(data["twittersAccount"])!=0:
    for twitter in data["twittersAccount"]:
        trx.addEntity("megadose.twitter", twitter)
if len(data["phoneNumbers"])!=0:
    for phone in data["phoneNumbers"]:
        trx.addEntity("maltego.PhoneNumber", phone)
if len(data["websites"])!=0:
    for website in data["websites"]:
        trx.addEntity("maltego.Website", website)
if data["address"] !=None:
    trx.addEntity("maltego.Location", data["address"])
if data["emailAddress"] !=None:
    trx.addEntity("maltego.EmailAddress", data["emailAddress"])
print(trx.returnOutput())
