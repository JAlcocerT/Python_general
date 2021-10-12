# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:12:06 2021

@author: jesus.tagua
"""
"""


[01/10/2021 15:02] Mateusz Juszczuk
https://www.linkedin.com/developers/login


[01/10/2021 15:03] Mateusz Juszczuk
https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS
LinkedIn 3-Legged OAuth Flow - LinkedIn
Step-by-step guide for LinkedIn's 3-legged OAuth flow.

[01/10/2021 15:03] Mateusz Juszczuk
https://www.youtube.com/watch?v=jYflkIo1R4A&ab_channel=API-University

POSTMAN
https://www.youtube.com/watch?v=dfof_ha0WGM&ab_channel=amityazdan

[01/10/2021 15:04] Mateusz Juszczuk
we need to get the get access token
"""



#Step1: https://linkedin.com/developers/apps

#The clientID identifies our app on linkedin

#OAuth acces token to call the Linkedin API


redirectURI = "https://www.google.com/"
#https://api-university.com
URLENCODE_redirectURI = "https%3A%2F%2Fwww.google.com%2F" #use https://www.urlencoder.org/
#https%3A%2F%2Fapi-university.com
clientID = "787k4ec3o5svb9"
clientSecret = "GlYjLOK8AMMLqyfs"


#The first request is going to the authorization end point, in the browser:
    
scope = "r_liteprofile"

https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&scope&client_id=clientId&redirect_uri=URLENCODE_redirectURI



https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&scope&client_id=clientId&redirect_uri=URLENCODE_redirectURI

linkedin_url="https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&" & scope
print("https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&"+scope+"&client_id="+clientID+"&redirect_uri="+URLENCODE_redirectURI)

https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&r_liteprofile&client_id=787k4ec3o5svb9&redirect_uri=https%3A%2F%2Fapi-university.com

joke="aaaa"
base_url = 'https://api.telegram.org/bot1664755389:AAEd1vvaLyjAkVxfh8s3vDwPWcJf2di5eDE/sendMessage?chat_id=-548977370&text="{}"'.format(joke) 
requests.get(base_url) #it calls the url
time.sleep(15) #seconds





#Linkedin official APi returns data in xml format
#The uri to hit is: https://api.linkedin.com/v1/people/~
#to have the reply in json: https://api.linkedin.com/v1/people/~?format=json





#pip install linkedin_api
from linkedin_api import Linkedin

api = Linkedin('juszczukmateusz@gmail.com','batfor11')
api = Linkedin('jesalctag@gmail.com','Abcdef13$$lin')

# GET a profiles contact info
print(api.get_profile('jalcocer')) #it returns a json file with the information of the profile
#to have a better view of the json's structure: https://jsonformatter.curiousconcept.com/#

contact_info = api.get_profile_contact_info('jalcocer')
print(contact_info)


# GET 1st degree connections of a given profile
connections = api.get_profile_connections('jalcocer')
print(connections)


# Get company data
api.get_company('cloudbest')

#Company's updates
api.get_company_updates('cloudbest')


#Last 90 days visits
view_data=api.get_current_profile_views()


api.get_invitations()


api.get_profile_skills('jalcocer')
api.get_profile_updates('jalcocer')


api.search_jobs(keywords=None, companies=None, experience=None, job_type=None, job_title=None, industries=None, location_name=None, remote=True, listed_at=86400, distance=None, limit=-1, offset=0, **kwargs)


api.view_profile('jalcocer')
api.get_invitations()
