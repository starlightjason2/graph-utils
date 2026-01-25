"""Data models for representing data points and datasets."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from graph_utils.fitting import line_func


class DataPoint:
    """Represents a single (x, y) data point."""
    
    def __init__(self, x, y):
        """Initialize a data point.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        self.x = x
        self.y = y


class DataSet:
    """A collection of data points with optional curve fitting capabilities."""
    
    def __init__(
        self,
        data_points: list[DataPoint],
        title: str = "",
        fit_func=line_func,
    ):
        """Initialize a dataset.
        
        Args:
            data_points: List of DataPoint objects
            title: Optional title for the dataset
            fit_func: Function to use for curve fitting (default: line_func)
        """
        self.title = title
        self.data_points = data_points
        self.fit_func = fit_func

    def get_x(self) -> list:
        """Extract x values from data points.
        
        Returns:
            List of x coordinates
        """
        return [point.x for point in self.data_points]

    def get_y(self) -> list:
        """Extract y values from data points.
        
        Returns:
            List of y coordinates
        """
        return [point.y for point in self.data_points]

    def graph(self):
        """Plot the data points as a scatter plot."""
        plt.scatter(self.get_x(), self.get_y(), label=self.title)

    def fit(self, label: str = ""):
        """Fit a curve to the data points and plot it.
        
        Args:
            label: Optional label for the fitted curve
        """
        x_values, y_values = self.get_x(), self.get_y()
        curve, curve_params = curve_fit(self.fit_func, x_values, y_values)
        x_fit = np.linspace(min(x_values), max(x_values), 100)
        y_fit = self.fit_func(x_fit, *curve)
        plt.plot(x_fit, y_fit, "--", label=f"{self.title} fit")
