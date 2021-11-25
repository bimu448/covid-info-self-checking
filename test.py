import requests
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

class covid_data:
    def __init__(self):
        #default url
        self.location_url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-health-advice-public/contact-tracing-covid-19/covid-19-contact-tracing-locations-interest"
        self.cases_url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-current-cases"
        self.vaccine_url = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-vaccine-data"
        self.headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        self.session = requests.Session()
    def get_locations(self):
        req = self.session.get(self.location_url, headers=self.headers)
        bs_location = BeautifulSoup(req.text, features="html.parser")
        data = bs_location.findAll("td")

        count = 0
        #location_class = "views-field-title"
        #address_class = "views-field-title"

        location_interest_list = []
        row_dict = {}
        count = 1
        for info in data:
            info = info.get_text()
            info = info.strip()

            #set key
            if count % 6 == 1:
                key = "location"
            elif count % 6 == 2:
                key = "address"
            elif count % 6 == 3:
                key = "day"
            elif count % 6 == 4:
                key = "time"
            elif count % 6 == 5:
                key = "todo"
            elif count % 6 == 0:
                key = "update"

            #change row
            if key in row_dict:
                location_interest_list.append(row_dict)
                row_dict = {}

            row_dict[key] = info
            count += 1
        return location_interest_list

    def get_cases(self):
        req = self.session.get(self.cases_url, headers=self.headers)
        bs_cases = BeautifulSoup(req.text)
        data = bs_cases.findAll("table", {"class":"table-style-two"})

        cases_dict = {}
        cases_list = []
        for info in data[:2]:
            info = info.get_text()
            info = info.strip()
            info = info.split("\n")
            cases_list.append(info)
        count = 0
        for data in cases_list:
            if count == 0:
                for keys in range(len(data)):
                    if data[keys] == "New cases reported during the past 24 hours":
                        cases_dict["new_cases"] = int(data[keys+1])
                    if data[keys] == "Total":
                        cases_dict["total_caese"] = int(data[keys+1])
                    if data[keys] == "Most recent case reported":
                        cases_dict["last_case_date"] = data[keys+1]
                    count += 1
            else:
                for keys in range(len(data)):
                    if data[keys] == "Deceased":
                        cases_dict["deceased_cases"] = int(data[keys+2])
        return cases_dict

    def get_vaccine(self):
        req = self.session.get(self.vaccine_url, headers=self.headers)
        bs_vaccine = BeautifulSoup(req.text)
        data = bs_vaccine.findAll("table", {"class":"table-style-two"})
        vaccine_list = []
        for info in data[0]:
            info = info.get_text()
            info = info.strip()
            info = info.split("\n")
            vaccine_list.append(info)
        vaccine_dict = {}
        for data in vaccine_list:
            for keys in range(len(data)):
                if data[keys] == "First dose":
                    vaccine_dict[data[keys]] = [data[keys+1], data[keys+2]]
                if data[keys] == "Second dose":
                    vaccine_dict[data[keys]] = [data[keys+1], data[keys+2]]
                if data[keys] == "Total doses":
                    vaccine_dict[data[keys]] = [data[keys+1], data[keys+2]]
        return vaccine_dict
