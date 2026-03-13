
import requests

url = f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq 'COUNTRY' and TimeDimensionValue eq '2020' and Dim1 eq 'SEX_BTSX'" 

country_codes = ["USA","MEX","CAN"]

for country_code in country_codes:
    r = requests.get(f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq '{country_code}' and TimeDimensionValue eq '2020' and Dim1 eq 'SEX_BTSX'")
    result = r.json()
    life_expectancy = result["value"][0]["NumericValue"]
    print(country_code, life_expectancy)
