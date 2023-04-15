import numpy as np
import pandas as pd
import pycountry_convert 


def initial_transform(df):
    df['Month'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year
    df['Day'] = df['InvoiceDate'].dt.day
    df['Hour'] = df['InvoiceDate'].dt.hour
    df['Minute'] = df['InvoiceDate'].dt.minute
    df['Second'] = df['InvoiceDate'].dt.second
    df['Price'] = df['Price'].astype(float)
    df['TotalPrice'] = df['Price'] * df['Quantity']
    df['YearMonth'] = df['InvoiceDate'].map(lambda date: str(date.year) + "-" +str(date.month).zfill(2))

    df = df[df['Quantity'] > 0]


def add_continent_and_eu_columns(df):

    # change EIRE to Ireland
    df['Country'] = df['Country'].replace('EIRE', 'Ireland')

    # change RSA to South Africa
    df['Country'] = df['Country'].replace('RSA', 'South Africa')

    # change Channel Islands to United Kingdom
    df['Country'] = df['Country'].replace('Channel Islands', 'United Kingdom')

    # change Korea to South Korea   
    df['Country'] = df['Country'].replace('Korea', 'South Korea')

    # remove West Indies and Unspecified
    df = df[df['Country'] != 'West Indies']
    df = df[df['Country'] != 'Unspecified']



    eu_countries_2011 = ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']
    countries = df.Country.unique()
    country_continent = {}
    country_eu = {}
    for country in countries:
        try:
            #country name to country code
            code = pycountry_convert.country_name_to_country_alpha2(country)
            #country code to continent
            continent  =pycountry_convert.country_alpha2_to_continent_code(code)

            country_continent[country] = continent

        except KeyError:
            continue
        country_eu[country] = 0 if country is None or country not in eu_countries_2011 else 1


    # create a new column with the continent for each row
    df['Continent'] = df['Country'].map(country_continent)
    df["is_eu"] = df["Country"].map(country_eu)
    df['is_eu'].fillna(0, inplace=True)
    df["is_eu"] = df["is_eu"].astype(int)
    return df