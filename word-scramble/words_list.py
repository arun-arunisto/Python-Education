from english_words import get_english_words_set
import pycountry
import geonamescache

# Get the English word set
english_words = get_english_words_set(['web2'], lower=True)

# Initialize geonamescache
gc = geonamescache.GeonamesCache()

# Get country names
country_names = [country.name.lower() for country in pycountry.countries]

# Get state names (from pycountry subdivisions)
state_names = [subdiv.name.lower() for subdiv in pycountry.subdivisions]

# Get city names (from geonamescache)
city_names = [city_data['name'].lower() for city_data in gc.get_cities().values()]

# Combine all names
all_geo_names = set(country_names + state_names + city_names)

# Filter names that are English words and are longer than 5 characters
geo_words = [name for name in all_geo_names if name in english_words and len(name) > 5]

# Show top 100 results
words_list = geo_words[:100]
"""
english_words = get_english_words_set(['web2'], lower=True)

# Get the list of country names in lowercase
country_names = [country.name.lower() for country in pycountry.countries]

# Filter: keep only those countries that are also in the English words set
country_words = [country for country in country_names if country in english_words]

# Show the result (first 100 if needed)
words_list = country_words[:200]
"""