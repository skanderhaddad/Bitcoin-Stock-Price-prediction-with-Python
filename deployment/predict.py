import matplotlib.pyplot as plt
import yfinance as yf
from fbprophet import Prophet


def Predict(a,days):
    df = yf.download(a, start="2017-01-01")
    df = df.reset_index()
    df[['ds', 'y']] = df[['Date', 'Adj Close']]
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(days)
    forecast = model.predict(future)
    print("the minimum value ", forecast.yhat_lower.iloc[-1])
    print("the maximum value ", forecast.yhat_upper.iloc[-1])
    print("the average value ", forecast.yhat.iloc[-1])
    output=forecast.yhat.iloc[-1]
    graph=model.plot(forecast)
    return(output,graph)


