from __future__ import print_function

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import pydotplus
import subprocess

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
#
# os.environ['PATH'] += ":"+"/usr/local/bin"
# print (os.environ['PATH'])
#
# print (os.getcwd())

from subprocess import check_call

def get_iris_data():
    """Get the iris data, from local csv or pandas repo."""
    if os.path.exists("iris.csv"):
        print("-- iris.csv found locally")
        df = pd.read_csv("iris.csv", index_col=0)
    else:
        print('Something went wrong...')
    return df

def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    f = open("dt.dot", 'w')
    export_graphviz(tree, out_file=f,
                        feature_names=feature_names)
    f.close()
    dot_data = export_graphviz(tree, out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("iris.pdf")
    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    # subprocess.check_call(command)

def encode_target(df, target_column):
    """Add column to df with integers for the target.

    Args
    ----
    df -- pandas DataFrame.
    target_column -- column to map to int, producing
                     new Target column.

    Returns
    -------
    df_mod -- modified DataFrame.
    targets -- list of target names.
    """
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)


df = get_iris_data()

print("* df.head()", df.head(), sep="\n", end="\n\n")
print("* df.tail()", df.tail(), sep="\n", end="\n\n")
print("* iris types:", df["Name"].unique(), sep="\n")


df2, targets = encode_target(df, "Name")
print("* df2.head()", df2[["Target", "Name"]].head(), sep="\n", end="\n\n")
print("* df2.tail()", df2[["Target", "Name"]].tail(), sep="\n", end="\n\n")
print("* targets", targets, sep="\n", end="\n\n")

features = list(df2.columns[:3])
print("* features:", features, sep="\n")

y = df2['Target']
X = df2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

dt.fit(X,y)

visualize_tree(dt, features)