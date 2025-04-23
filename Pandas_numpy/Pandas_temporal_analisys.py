import pandas as pd


if __name__ == "__main__":
    fligth = pd.read_csv("../data_2/T_T100D_MARKET_US_CARRIER_ONLY.csv")
    fligth_c = fligth.copy()

    fligth_c["COUNT"] =  fligth.groupby(["MONTH","UNIQUE_CARRIER_NAME"])["UNIQUE_CARRIER_NAME"].transform("count")
    fligth_UC = fligth_c[['MONTH','UNIQUE_CARRIER_NAME', "COUNT" ]]
    fligth_UC = fligth_UC.sort_values(by=['MONTH','UNIQUE_CARRIER_NAME' ], ascending=[True, True])
    fligth_UC = fligth_UC.drop_duplicates()

    print(fligth.sort_values(by=['MONTH','UNIQUE_CARRIER_NAME' ], ascending=[True, True]).head(18).to_string())

    print(fligth_UC.head(10).to_string())

    fligth_c_airport = fligth.copy()

    fligth_c_airport_or = fligth.copy()

    airport = pd.read_csv("../data_2/L_AIRPORT_ID.csv")

    #create a dict for map the fligths
    airport_dict = airport.set_index('Code')['Description'].to_dict()

    fligth_c_airport["DEST_AIRPORT_DESC"] = fligth_c_airport["DEST_AIRPORT_ID"].map(airport_dict)

    fligth_c_airport["COUNT"] = fligth_c_airport.groupby(["DEST_AIRPORT_DESC","MONTH"])["DEST_AIRPORT_DESC"].transform("count")

    fligth_dest_mont = fligth_c_airport[["DEST_AIRPORT_DESC","MONTH","COUNT"]]

    fligth_dest_mont = fligth_dest_mont.sort_values(by=["DEST_AIRPORT_DESC","COUNT", "MONTH"],ascending=[True, False, True])

    fligth_dest_mont = fligth_dest_mont.drop_duplicates()

    print(fligth_dest_mont.head(100).to_string())

    fligth_c_airport_or["ORIGIN_AIRPORT_DESC"] = fligth_c_airport_or["ORIGIN_AIRPORT_ID"].map(airport_dict)

    fligth_c_airport_or["COUNT"] = fligth_c_airport_or.groupby(["ORIGIN_AIRPORT_DESC","UNIQUE_CARRIER_NAME","MONTH"])["ORIGIN_AIRPORT_DESC"].transform("count")

    fligth_or_mont = fligth_c_airport_or[["UNIQUE_CARRIER_NAME","ORIGIN_AIRPORT_DESC","MONTH","COUNT"]]

    fligth_or_mont = fligth_or_mont.sort_values(by=["UNIQUE_CARRIER_NAME","ORIGIN_AIRPORT_DESC","COUNT"],ascending=[True,True, False])

    fligth_or_mont = fligth_or_mont.drop_duplicates()

    print(fligth_or_mont.head(100).to_string())