import numpy as np
import pandas as pd
import pycountry_convert 


def add_continent_column(df):
    countries = df.Country.unique()
    country_continent = {}
    for country in countries:
        try:
            #country name to country code
            code = pycountry_convert.country_name_to_country_alpha2(country)
            #country code to continent
            continent  =pycountry_convert.country_alpha2_to_continent_code(code)

            country_continent[country] = continent
        except KeyError:
            continue

    # create a new column with the continent for each row
    df['Continent'] = df['Country'].map(country_continent)