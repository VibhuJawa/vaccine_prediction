import json
import requests
import pandas as pd
import os

us_cities_df = pd.read_csv("vaccine_data/uscitiesv1.4.csv")
county_df = us_cities_df[["state_id","county_name","zips"]]

# county_level
year = 2017
request_url = "https://fluvaccineapi.hhs.gov/api/v2/vaccination_rates/trends/{}/states/{}/counties/{}.json"
no_response_list = []
for index,row in county_df.iterrows():
    if index>10000:
        state_id = row["state_id"]
        county_name = row["county_name"]
        url = request_url.format(year,state_id,county_name)
        response = requests.get(url)
        if response.status_code!=200:
            no_response_list.append((year,state_id,county_name,response.status_code))
        else:
            curr_json = response.json()
            filename = "vaccine_data/{}_county_level/{}/{}.json".format(year,state_id,county_name)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w') as outfile:
                json.dump(curr_json, outfile)
        if index%100==0:
            print("Done till index = {}".format(index))
            thefile = open('vaccine_data/{}_county_level/no_respose_list_county_level/no_response_list_till_index_{}.txt'.format(year,index), 'w')
            for item in no_response_list:
                thefile.write("{}\n".format(item))
            thefile.close()
            


