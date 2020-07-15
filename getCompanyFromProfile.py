from MaltegoTransform import *
from nqntnqnqmb import *
import random
with open('./config.json') as config_file:
    config = random.choice(json.load(config_file))

trx = MaltegoTransform()

companySearch=str(sys.argv).split('Linkedin.Profile.Url=')[1].replace("'","").replace("]","").split('#Random=')[0]
companys = getCompanyFromProfile(companySearch,config["JSESSIONID"],config["li_at"])

for company in companys:
    linkedinCompanyEntities = trx.addEntity("maltego.linkedin.company",company["linkedin_url"].replace("&","&amp;"))
    linkedinCompanyEntities.addProperty(fieldName="name",value=str(company["name"]).replace("&","&amp;"))
    linkedinCompanyEntities.setIconURL(company["logo"].replace("&","&amp;"))
print(trx.returnOutput())
