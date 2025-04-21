
import pandas as pd


if __name__ == "__main__":

    fligths = pd.read_csv("../data_2/T_T100D_MARKET_US_CARRIER_ONLY.csv")

    print("----- check nulls on origin and dest ------")
    print(fligths[["ORIGIN", "DEST"]].isnull().sum())

    valid_route = fligths[fligths["DEST"] != fligths["ORIGIN"]].copy()

    print("----- check route columns ------")
    print(valid_route.head(10).to_string())

    valid_route["ROUTE"] = valid_route["ORIGIN"]+"-"+valid_route["DEST"]

    print("----- check route columns ------")
    print(valid_route.head(10).to_string())

    print("---- Check unique values in month ----")
    print(fligths["MONTH"].unique())


    fligths["MONTH"] = pd.Categorical(fligths["MONTH"],categories=range(1,13),ordered=True)
    print("---- Check unique values in month after category change ----")
    print(fligths["MONTH"].unique())

    print("---- Check size month ----")
    print(fligths.groupby("MONTH", observed=True).size())

    print("------- check month category data type ----------")
    print(fligths.dtypes)




