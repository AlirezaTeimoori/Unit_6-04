#Created by: Alireza Teimoori
#Created on: Dec 2017
#Created for: ICS3UR-1
#Lesson: Unit 6-04
#This program shows mailing address with Enum

from enum import Enum

route_type = Enum('ABBEY','FIELD','FARM','FOREST','BEY')
province = Enum('AB','BC','MB','NB','NL','NT','NS','NU','ON','PE','QC','SK','YT')

class Mailing_address():
    def __init__(self, first_name, last_name, street_number, route_type, city_name, province, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.street_number = street_number 
        self.route_type = route_type
        self.street_number = street_number
        self.city_name = city_name
        self.province = province
        self.postal_code = postal_code

user = Mailing_address(raw_input("Enter your first name: \n"), raw_input("Enter your last name: \n"), raw_input("Enter your street_number: \n"), raw_input("Enter your route type: \n"), raw_input("Enter your city name: \n"), raw_input("Enter your province: \n"), raw_input("Enter your postal code: \n"))


if user.route_type not in route_type:
    while user.route_type not in route_type:
        
        print("Wrong route type.")
        user.route_type = raw_input("please enter a valid route type: \n")
        
        if user.province not in province:
            while user.province not in province:
                
                print("Wrong province.")
                user.province = raw_input("please enter a valid province: \n")
            
        
    print("\n\n")
    print(user.first_name+" "+user.last_name)
    print("10-123 1/2 "+" "+user.route_type+" "+user.street_number)
    print(user.city_name+" "+user.province+" "+user.postal_code)
    
    
    
elif user.province not in province:
    while user.province not in province:
        
        print("Wrong province.")
        user.province = raw_input("please enter a valid province: \n")
        
    print("\n\n")
    print(user.first_name+" "+user.last_name)
    print("10-123 1/2 "+" "+user.route_type+" "+user.street_number)
    print(user.city_name+" "+user.province+" "+user.postal_code)
    
else:
    print("\n\n")
    print(user.first_name+" "+user.last_name)
    print("10-123 1/2 "+" "+user.route_type+" "+user.street_number)
    print(user.city_name+" "+user.province+" "+user.postal_code)
