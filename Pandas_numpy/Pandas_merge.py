import pandas as pd



if __name__ == "__main__":

    fligth = pd.read_csv("../data_2/T_T100D_MARKET_US_CARRIER_ONLY.csv")
    airport = pd.read_csv("../data_2/L_AIRPORT_ID.csv")

    #create a dict for map the fligths
    airport_dict = airport.set_index('Code')['Description'].to_dict()

    fligth["ORIGIN_AIRPORT_DESC"] = fligth["ORIGIN_AIRPORT_ID"].map(airport_dict)
    fligth["DEST_AIRPORT_DESC"] = fligth["DEST_AIRPORT_ID"].map(airport_dict)
    fligth.drop(columns=["ORIGIN_AIRPORT_ID","DEST_AIRPORT_ID"],axis=1 , inplace=True)

    print("----- add 2 columns nomae of airport orig and dest")
    print(fligth.head(10).to_string())

    print("----------- check nulls ------------")
    print(fligth[["ORIGIN_AIRPORT_DESC","DEST_AIRPORT_DESC"]].isnull().sum())

