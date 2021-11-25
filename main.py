from test import*

class statementData:
    def __init__(self):
        c = covid_data()
        #location return dict
        self.locations = c.get_locations()
        #cases return dict
        self.cases = c.get_cases()
        #vaccine return dict
        self.vaccine = c.get_vaccine()

    def get_locations(self):
        location_list = []
        month_dict = {"January":"01",
                      "February":"02",
                      "March":"03",
                      "Apirl":"04",
                      "May":"05",
                      "June":"06",
                      "July":"07",
                      "August":"08",
                      "Septermber":"09",
                      "October":"10",
                      "November":"11",
                      "December":"12"}
        for location in self.locations:
            address_code = len(location["address"])
            day_list = location["day"].split()
            day_code = "0" + day_list[1]
            day_code = day_code[-2:] + month_dict[day_list[-1]]
            time_code = ""
            for num in location["time"]:
                if num.isdigit():
                    time_code += num
            time_code = time_code + "00"
            time_code = time_code[:8]
            update_code = ""
            for num in location["update"]:
                if num.isdigit():
                    update_code += num
            update_code = update_code + "00"
            update_code = update_code[:6]        
            location_code = address_code + int(day_code) + int(time_code) + int(update_code)

            location_list.append((location_code,
                                     location["location"],
                                     location["address"],
                                     location["day"],
                                     location["time"],
                                     location["update"]))

        return location_list

    def get_cases(self):
        return self.cases


        
            
