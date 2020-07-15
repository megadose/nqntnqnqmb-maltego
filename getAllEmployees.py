from MaltegoTransform import *
from nqntnqnqmb import *
import random
with open('./config.json') as config_file:
    config = random.choice(json.load(config_file))

trx = MaltegoTransform()

companySearch=sys.argv[1].split("company/")[1].replace("/","")
employee = getAllEmployees(companySearch,config["JSESSIONID"],config["li_at"])

for employe in employee:
    name = employe["firstname"] + " " + employe["lastname"]
    linkedinProfileEntitie = trx.addEntity("megadose.LinkedinProfile", ''.join(random.choice(string.ascii_lowercase) for i in range(49)))
    linkedinProfileEntitie.addProperty(fieldName="Name",value=name)
    linkedinProfileEntitie.addProperty(fieldName="Occupation",value=str(employe["occupation"]).replace("&","&amp;"))
    linkedinProfileEntitie.addProperty(fieldName="Linkedin.Profile.Url",value=str(employe["profile-url"]).replace("&","&amp;"))
    linkedinProfileEntitie.addProperty(fieldName="Random",value=str(''.join(random.choice(string.ascii_lowercase) for i in range(49))).replace("&","&amp;"))
    linkedinProfileEntitie.setIconURL(employe["picture-url"].replace("&","&amp;"))

print(trx.returnOutput())
