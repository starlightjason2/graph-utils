import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from pathlib import Path

SAVE_DIR = './output'


# Exponential fit
def exp_func(x, a, b):
    return a * np.log(b * x)


# Line fit
def line_func(x, m, b):
    return m * x + b


class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DataSet:
    def __init__(
        self,
        data_points: list[DataPoint],
        title="",
        # fit to line by default
        fit_func=line_func,
    ):
        self.title = title
        self.data_points = data_points
        self.fit_func = fit_func

    def get_x(self):
        return [point.x for point in self.data_points]

    def get_y(self):
        return [point.y for point in self.data_points]

    def graph(self):
        plt.scatter(self.get_x(), self.get_y(), label=self.title)

    def fit(self, label=""):
        x_values, y_values = self.get_x(), self.get_y()
        curve, curve_params = curve_fit(self.fit_func, x_values, y_values)
        x_fit = np.linspace(min(x_values), max(x_values), 100)
        y_fit = self.fit_func(x_fit, *curve)
        plt.plot(x_fit, y_fit, "--", label=f"{self.title} fit")


class Graph:
    def __init__(self, data: list[DataSet], title: str, x_label: str, y_label: str):
        self.data = data
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def show(self, fit=False, save=True):
        for data_set in self.data:
            data_set.graph()

            if fit:
                data_set.fit()

        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)

        if len(self.data) > 1:
            plt.legend()
        
        if (save):
            file_name = self.title.lower().replace(' ', '_')
            plt.savefig( Path(SAVE_DIR) / file_name)

        plt.show()

