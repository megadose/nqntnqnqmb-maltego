from MaltegoTransform import *
from nqntnqnqmb import *
import random
with open('./config.json') as config_file:
    config = random.choice(json.load(config_file))

trx = MaltegoTransform()

companyName=sys.argv[1]
companys = getCompanyFromName(companyName,config["JSESSIONID"],config["li_at"])
for company in companys:
    linkedinCompanyEntities = trx.addEntity("maltego.linkedin.company",company["urlCompany"])
    linkedinCompanyEntities.addProperty(fieldName="name",value=str(company["name"]).replace("&","&amp;"))
    linkedinCompanyEntities.setIconURL(company["logo"].replace("&","&amp;"))

print(trx.returnOutput())
