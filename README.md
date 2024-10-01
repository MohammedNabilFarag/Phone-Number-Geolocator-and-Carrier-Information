# Phone Number Geolocator and Carrier Information

This Python script uses the `phonenumbers` and `opencage` libraries to determine the location and carrier information associated with a given phone number.  The script then generates an HTML file using `folium` displaying the location on a map.

## Contributor

* Mohammed Nabil Abdullah Faraj (202174042)

## Dependencies

Before running this script, make sure you have the following libraries installed:

* `phonenumbers`:  `pip install phonenumbers`
* `opencage`: `pip install opencage`
* `folium`: `pip install folium`

You will also need an OpenCage API key.  Replace `"c910335b70c9442380c65001f8bdeb39"` in the code with your actual API key.


## Usage

1. **Obtain an OpenCage API Key:** Sign up for a free account at [https://opencagedata.com/](https://opencagedata.com/) to get an API key.

2. **Replace the API Key:**  In the `main.py` script, replace `"c910335b70c9442380c65001f8bdeb39"` with your OpenCage API key.

3. **Run the Script:** Execute the script using `python main.py`.  The script will prompt you to enter a phone number.

4. **View the Results:** The script will print the location description and carrier name to the console.  It will also create an HTML file named `Your location.html` containing a map showing the location. Open this HTML file in a web browser to view the map.


## Functionality

The script performs the following actions:

1. **Takes Phone Number Input:** Prompts the user to enter a phone number.
2. **Parses the Number:** Uses the `phonenumbers` library to parse the phone number and ensure it's in a valid format.
3. **Geocodes the Number:** Uses the `phonenumbers` library to get a location description based on the phone number's country code.
4. **Gets Carrier Information:** Uses the `phonenumbers` library to identify the carrier associated with the phone number.
5. **Reverse Geocodes Location:** Uses the `opencage` library to perform reverse geocoding on the location description obtained earlier to get latitude and longitude coordinates.
6. **Creates a Map:** Uses the `folium` library to create an HTML map centered on the obtained coordinates, with a marker indicating the location.
7. **Saves the Map:** Saves the map as an HTML file (`Your location.html`).


## Error Handling and Potential Issues

* **Invalid Phone Number:** The script may not work correctly if the user enters an invalid phone number format.  Consider adding more robust input validation.
* **Network Connectivity:** The script requires an internet connection to access the OpenCage Geocoder API.  Error handling should be added to gracefully handle network issues.
* **API Limits:** The OpenCage API has usage limits.  If you exceed these limits, the script may fail.  Implement appropriate error handling to inform the user.
* **Geocoding Accuracy:** The accuracy of the location information depends on the accuracy of the phone number's data and the OpenCage API.


## License

[Specify your license here, e.g., MIT License]


## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.
