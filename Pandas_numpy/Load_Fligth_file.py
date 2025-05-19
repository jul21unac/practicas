import pandas as pd



if __name__ == "__main__":

    fligth = pd.read_csv("../data_2/T_T100D_MARKET_US_CARRIER_ONLY.csv")

    five_row = fligth.head(5)

    five_loc = fligth.loc[:5]

    print("5 rows")
    print(five_row)


    print("print columns")
    print(fligth.columns)

    print("print datatypes:")
    print(fligth.dtypes)

    print("print nulls:")
    print(fligth.isnull().sum())