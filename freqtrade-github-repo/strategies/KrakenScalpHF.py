# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
from functools import reduce

from freqtrade.strategy import IStrategy, IntParameter, DecimalParameter
from pandas import DataFrame
import talib.abstract as ta


class KrakenScalpHF(IStrategy):
    INTERFACE_VERSION = 3

    timeframe = "5m"
    process_only_new_candles = True
    startup_candle_count = 50

    minimal_roi = {
        "0": 0.015
    }

    stoploss = -0.0012
    trailing_stop = False

    use_exit_signal = False
    exit_profit_only = True
    ignore_roi_if_entry_signal = True

    buy_rsi = IntParameter(25, 45, default=40, space="buy")
    ema_fast_len = IntParameter(8, 20, default=12, space="buy")
    ema_slow_len = IntParameter(21, 80, default=34, space="buy")
    vol_mult = DecimalParameter(0.5, 1.5, default=0.6, decimals=2, space="buy")
    bounce_mult = DecimalParameter(1.000, 1.004, default=1.000, decimals=3, space="buy")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod=int(self.ema_fast_len.value))
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod=int(self.ema_slow_len.value))
        dataframe["ema_200"] = ta.EMA(dataframe, timeperiod=200)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)

        bb = ta.BBANDS(dataframe, timeperiod=20, nbdevup=2.0, nbdevdn=2.0)
        dataframe["bb_upper"] = bb["upperband"]
        dataframe["bb_mid"] = bb["middleband"]
        dataframe["bb_lower"] = bb["lowerband"]

        dataframe["vol_mean"] = dataframe["volume"].rolling(20).mean()
        dataframe["prev_close"] = dataframe["close"].shift(1)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions = []

        conditions.append(dataframe["volume"] > 0)

        # looser oversold threshold
        conditions.append(dataframe["rsi"] < int(self.buy_rsi.value))

        # buy dips below fast EMA
        conditions.append(dataframe["close"] < dataframe["ema_fast"])

        # allow near lower BB instead of deep below it
        conditions.append(dataframe["close"] < dataframe["bb_mid"])

        # simple bounce confirmation
        conditions.append(dataframe["close"] >= (dataframe["prev_close"] * float(self.bounce_mult.value)))

        # looser volume filter
        conditions.append(dataframe["volume"] > (dataframe["vol_mean"] * float(self.vol_mult.value)))

        dataframe.loc[
            reduce(lambda x, y: x & y, conditions),
            "enter_long"
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["exit_long"] = 0
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return self.populate_entry_trend(dataframe, metadata)

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return self.populate_exit_trend(dataframe, metadata)
