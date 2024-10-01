import phonenumbers
from phonenumbers import geocoder ,carrier
import folium



number = input("Please enter the phone number and make sure that you are connected to the Network to show the GPS: ")

check_number = phonenumbers.parse(number) 

number_location = geocoder.description_for_number(check_number,'en')

print(number_location)



service_provider = phonenumbers.parse(number)  

print(carrier.name_for_number(service_provider,'en'))



from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode('c910335b70c9442380c65001f8bdeb39')

query = str(number_location) 

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat'] 

lng = results[0]['geometry']['lng']

print(lat,lng)





map_location = folium.Map(location= [lat,lng],zoom_start=9)

folium.Marker([lat,lng], popup = number_location).add_to(map_location)

map_location.save('Your location.html')