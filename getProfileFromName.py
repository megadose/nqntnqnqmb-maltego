from MaltegoTransform import *
from nqntnqnqmb import *
import random
with open('./config.json') as config_file:
    config = random.choice(json.load(config_file))

trx = MaltegoTransform()

nameSearch=sys.argv[1]
names = getProfileFromName(nameSearch,config["JSESSIONID"],config["li_at"])

for name in names:
    linkedinProfileEntitie = trx.addEntity("megadose.LinkedinProfile", ''.join(random.choice(string.ascii_lowercase) for i in range(49)))
    linkedinProfileEntitie.addProperty(fieldName="Name",value=name["firstname"] + " " + name["lastname"])
    linkedinProfileEntitie.addProperty(fieldName="Occupation",value=str(name["occupation"]).replace("&","&amp;"))
    linkedinProfileEntitie.addProperty(fieldName="Linkedin.Profile.Url",value=str(name["profile-url"]).replace("&","&amp;"))
    linkedinProfileEntitie.addProperty(fieldName="Location",value=str(name["location"]).replace("&","&amp;"))
    linkedinProfileEntitie.addProperty(fieldName="Industry",value=str(name["industry"]).replace("&","&amp;"))
    linkedinProfileEntitie.setIconURL(name["picture-url"].replace("&","&amp;"))
print(trx.returnOutput())
