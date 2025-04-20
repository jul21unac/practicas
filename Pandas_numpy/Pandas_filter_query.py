import pandas as pd



if __name__ == "__main__":

    fligths = pd.read_csv("../data_2/T_T100D_MARKET_US_CARRIER_ONLY.csv")

    delta_1 = fligths[(fligths['UNIQUE_CARRIER_NAME'] =='Delta Air Lines Inc.') & (fligths['ORIGIN'] == 'ATL' )]

    lax_dec = fligths.query('DEST == "LAX" & MONTH == 12 ')

    print("---------fligth from ATL of delta air lines inc---------")
    print(delta_1.to_string())

    print("---------fligths to LAX on December")
    print(lax_dec.to_string())