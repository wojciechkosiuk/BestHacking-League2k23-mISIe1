import numpy as np
import pandas as pd
import pycountry_convert 


def initial_transform(df):
    df['Month'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year
    df['Day'] = df['InvoiceDate'].dt.day
    # df['Hour'] = df['InvoiceDate'].dt.hour
    # df['Minute'] = df['InvoiceDate'].dt.minute
    # df['Second'] = df['InvoiceDate'].dt.second
    df['Price'] = df['Price'].astype(float)
    df['TotalPrice'] = df['Price'] * df['Quantity']
    df['YearMonth'] = df['InvoiceDate'].map(lambda date: str(date.year) + "-" +str(date.month).zfill(2))

    df = df[df['Quantity'] > 0]
    df = df[df['Price'] > 0]
    df["is_logged"] = df['Customer ID'].isnull().astype(int)
    df["is_logged"] = (df["is_logged"] == 0).astype(int)

    return df


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
            if country == "United Kingdom":
                continent = "EU_UK"

            else:
                #country name to country code
                code = pycountry_convert.country_name_to_country_alpha2(country)
                #country code to continent
                continent  =pycountry_convert.country_alpha2_to_continent_code(code)
                


            country_continent[country] = continent

        except KeyError:
            continue
        is_eu = 0 if country is None or country not in eu_countries_2011 else 1

        if continent == "EU" and not is_eu:
            continent = "EU_nonEU"
            country_continent[country] = continent
            


    # create a new column with the continent for each row
    df['Continent'] = df['Country'].map(country_continent)

    return df


def add_moving_mean_columns(df):

    df_grouped = df.groupby(['Year', 'Month', 'StockCode', 'Continent']).agg({'Quantity': 'sum'})
    df_grouped = df_grouped.reset_index()
    
    # mr. worldwide
    quantities_total = df_grouped.groupby(['Year', 'Month', 'StockCode']).agg({'Quantity': 'sum'}).reset_index().rename(columns={'Quantity': 'quantity_month_worldwide'})
    quantities_total["mean_worldwide"] = quantities_total.groupby("StockCode")["quantity_month_worldwide"].rolling(window=3).mean().reset_index(level=0, drop=True)
    quantities_total["weighted_mean_worldwide"] = quantities_total.groupby("StockCode")["quantity_month_worldwide"].ewm(span=3, adjust=False).mean().reset_index(level=0, drop=True)
    quantities_total["mean_worldwide"].fillna(quantities_total["quantity_month_worldwide"],inplace=True)

    

    
    df_grouped = df_grouped.merge(quantities_total, on=['Year', 'Month', 'StockCode'], how='left').rename(columns={'Quantity': 'quantity_month_continent'})
    df_grouped["mean_continent"] = df_grouped.groupby("StockCode")["quantity_month_continent"].rolling(window=3).mean().reset_index(level=0, drop=True)
    df_grouped["weighted_mean_continent"] = df_grouped.groupby("StockCode")["quantity_month_continent"].ewm(span=3, adjust=False).mean().reset_index(level=0, drop=True)
    df_grouped["mean_continent"].fillna(df_grouped["quantity_month_continent"],inplace=True)
    return df_grouped