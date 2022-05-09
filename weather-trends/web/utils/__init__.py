import pandas as pd
import matplotlib.pyplot as plt

from os import path

from flask import Flask

app = Flask()

def get_path(file_name: str):
    return path.abspath(f'data/{file_name}.csv')


class WeatherTrends:
    def __init__(self) -> None:
        self.city_data, self.global_data = self.init()

    @staticmethod
    def init() -> tuple:
        return pd.read_csv(get_path('city_data')), \
               pd.read_csv(get_path('global_data'))

    def get_data_by_city(self, city: str) -> list:
        """
        Returns all local and global data
        related to the city name
        """
        lc_data = self.city_data.loc[
            self.city_data['city'] == city
            ]

        years = lc_data.year
        beginning, ending = min(years), max(years)

        gl_data = self.global_data[
            (beginning <= self.global_data.year) &
            (self.global_data.year <= ending)
        ]

        return [lc_data, gl_data]

    def make_plot(self, city_name: str):
        data = self.get_data_by_city(city_name)
        local_data, global_data = data[0], data[1]

        """
        rolling() method of pandas
        provides us the feature of 
        rolling window calculations.

        For calculating moving averages,
        we should use mean() method and we can
        achieve to calculate the rolling mean.
        """
        # setting the first line-chart params
        x_global = global_data['year']
        y_global = global_data['avg_tmp'].rolling(10).mean()

        # setting the first line-chart params
        x_local = local_data['year']
        y_local = local_data['avg_tmp'].rolling(10).mean()

        # for creating new figure
        plt.figure(figsize=(30, 10), dpi=55)

        plt.plot(
            x_global, y_global,
            label='Global temperature'
        )

        plt.plot(
            x_local, y_local,
            label='{} temperature'.format(
                city_name.title()
            )
        )

        plt.title('Global and ' + city_name + ' average temperature over time')

        plt.xlabel('Years', fontsize=20)
        plt.ylabel('Temperature in Celsius', fontsize=20)
        plt.grid(True)
        plt.legend(loc='upper right')

        return plt

    def save(self, city_name: str):
        plot = self.make_plot(city_name)

        plot.savefig(f'charts/{city_name.title()}.png')


__all__ = ["WeatherTrends"]
