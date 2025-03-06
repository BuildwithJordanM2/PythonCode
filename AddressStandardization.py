import re

# List of addresses to process
addresses = [
"1545 INTERSTATE DR.",
"2417 MYERS ROAD",
"1101 CLAY STREET",
"1195 S Guignard Dr",
"1621 1ST AVE"    
]

# Dictionary of abbreviations to their full forms
abbreviation_dict = {
    "Ave": "Avenue",
     "Ave": "Avenue",
    "St": "Street",
    "St.": "Street",
    "Blvd": "Boulevard",
    "Dr": "Drive",
    "Dr.": "Drive",
    "Pl": "Place",
    "Rd": "Road",
    "Hwy": "Highway",
    "N": "North",
    "N.": "North",
    "S": "South",
    "S.": "South",
    "E": "East",
    "E.": "East",
    "W": "West",
    "W.": "West",
    "Ste": "Suite",
    "Ct": "Court", 
    "Ln": "Lane",  
    "Pkwy": "Parkway",
    "Terr": "Terrace",
    "Cir": "Circle",
    "Sq": "Square",
    "Bldg": "Building",
    "SE": "Southeast",
    "SW": "Southwest",
    "NE": "Northeast",
    "NW": "Northwest"

}

# Function to replace abbreviations in an address
def replace_abbreviations(address, abbreviation_dict):
    for abbr, full in abbreviation_dict.items():
        # Escape the abbreviation to handle special characters like periods
        escaped_abbr = re.escape(abbr)
        
        # Use a regex pattern that matches the abbreviation followed by a non-word character or end of string
        address = re.sub(r'(?<!\w)' + escaped_abbr + r'(?!\w)', full, address, flags=re.IGNORECASE)
        
    return address

# Apply the replacement function to each address
modified_addresses = [replace_abbreviations(address, abbreviation_dict) for address in addresses]

# Print the modified addresses
for address in modified_addresses:
    print(address)
