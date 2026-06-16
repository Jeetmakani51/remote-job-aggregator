from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "https://weworkremotely.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tag = doc.find_all("li",class_="new-listing-container")
all_job_titles = []
all_company_names = []
all_company_location = []
all_salary = []

print(len(tag))

for jobs in tag:
    salary_found = False

    job_title = jobs.find("span",class_="new-listing__header__title__text")
    company_name = jobs.find("p",class_="new-listing__company-name")
    locations = jobs.find("p",class_="new-listing__company-headquarters")
    salary = jobs.find_all("p",class_="new-listing__categories__category")

    if(not job_title or not company_name):
        continue

    for category in salary:
        if "$" in category.text:
            all_salary.append(category.text)
            salary_found = True
            break
    if not salary_found:
        all_salary.append("not provided")
    
    if locations:
        location_title_text = locations.text.encode('ascii',errors='ignore').decode()
        all_company_location.append(location_title_text)
    else:
        all_company_location.append("not provided")
            

    job_title_text = job_title.text.encode('ascii',errors='ignore').decode()
    company_title_text = company_name.text.encode('ascii',errors='ignore').decode()
    

    all_job_titles.append(job_title_text)
    all_company_names.append(company_title_text)
    
    
print(all_job_titles)
print(len(all_job_titles))
#print(all_company_names)
print(len(all_company_names))
#print(all_company_location)
print(len(all_company_location))
#print(all_salary)
print(len(all_salary))

# first_10 = tag[:10]
# for i in first_10:
#     categories= i.find_all("p",class_="new-listing__categories__category")
#     for category in categories:
#         if "$" in category.text:
#             print(category.text)
        
df = pd.DataFrame({
    'job-title' : all_job_titles,
    'company-name' : all_company_names,
    'company-location' : all_company_location,
    'salary' : all_salary
})

print(df.head())
df.to_csv('jobs.csv',index=False)
print("csv created")