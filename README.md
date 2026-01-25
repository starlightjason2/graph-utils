# graph-utils

A simple Python wrapper for matplotlib and scipy that makes it easy to create graphs with data fitting capabilities.

## Installation

```bash
pip install graph-utils
```

## Usage

### Basic Example

```python
from graph_utils import DataPoint, DataSet, Graph

# Create data points
points = [
    DataPoint(1, 2),
    DataPoint(2, 4),
    DataPoint(3, 6),
    DataPoint(4, 8),
]

# Create a dataset
dataset = DataSet(points, title="My Data")

# Create and show the graph
graph = Graph([dataset], title="Simple Graph", x_label="X", y_label="Y")
graph.show()
```

### With Curve Fitting

```python
from graph_utils import DataPoint, DataSet, Graph, line_func, exp_func

# Create data points
points = [
    DataPoint(1, 2.1),
    DataPoint(2, 4.2),
    DataPoint(3, 6.1),
    DataPoint(4, 8.3),
]

# Create dataset with linear fit
dataset = DataSet(points, title="Linear Data", fit_func=line_func)

# Create graph with fitting enabled
graph = Graph([dataset], title="Fitted Graph", x_label="X", y_label="Y")
graph.show(fit=True)
```

### Multiple Datasets

```python
from graph_utils import DataPoint, DataSet, Graph

# Create multiple datasets
points1 = [DataPoint(i, i*2) for i in range(1, 6)]
points2 = [DataPoint(i, i*3) for i in range(1, 6)]

dataset1 = DataSet(points1, title="Dataset 1")
dataset2 = DataSet(points2, title="Dataset 2")

# Create graph with multiple datasets
graph = Graph([dataset1, dataset2], title="Comparison", x_label="X", y_label="Y")
graph.show()
```

## Classes

- **DataPoint**: Represents a single (x, y) data point
- **DataSet**: A collection of data points with optional curve fitting
- **Graph**: Creates and displays graphs with one or more datasets

## License

MIT
