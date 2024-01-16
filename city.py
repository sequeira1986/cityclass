class City:
    def __init__(self, city_name, region_name, country_name, number_citizens, zip_code, area_code):
        self.name = city_name
        self.region = region_name
        self.country = country_name
        self.citizens = number_citizens
        self.zip = zip_code
        self.area = area_code
    #def __str__(self):
        #return (self.name + " patri do " + str(self.region)+ " je hlavne mestom  " + str(self.country)
         #       + " ma " + str(self.citizens) + " obivatelia a zip kod " + str(self.zip) + " a PSC: "
          #      + str(self.area))
    def get_full_address(self):
        return f"{self.name},{self.region}, {self.country}, {self.citizens}, {self.zip}, {self.area}"
managua = City("Managua", "Pacifica", "Nicaragua", "253", "124", "200 km2")
bratislava = City("Bratislava", "Bratislavskej region", "Slovensko", "500000", "811", "125")
#print(city1)
#print(city)
print(managua.get_full_address())
print(bratislava.get_full_address())