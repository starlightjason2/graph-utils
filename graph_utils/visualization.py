"""Graph visualization and plotting functionality."""

import matplotlib.pyplot as plt
from pathlib import Path

from graph_utils.data import DataSet

SAVE_DIR = './output'


class Graph:
    """Creates and displays graphs with one or more datasets."""
    
    def __init__(self, data: list[DataSet], title: str, x_label: str, y_label: str):
        """Initialize a graph.
        
        Args:
            data: List of DataSet objects to plot
            title: Graph title
            x_label: Label for x-axis
            y_label: Label for y-axis
        """
        self.data = data
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def show(self, fit: bool = False, save: bool = True):
        """Display the graph.
        
        Args:
            fit: Whether to fit curves to the datasets
            save: Whether to save the graph to a file
        """
        for data_set in self.data:
            data_set.graph()

            if fit:
                data_set.fit()

        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)

        if len(self.data) > 1:
            plt.legend()
        
        if save:
            file_name = self.title.lower().replace(' ', '_')
            plt.savefig(Path(SAVE_DIR) / file_name)

        plt.show()
