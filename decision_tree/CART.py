from __future__ import print_function
from IPython.display import Image

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


def get_data(name):
    if os.path.exists(name + ".csv"):
        print("-- " + name + ".csv found locally")
        df = pd.read_csv(name + ".csv", index_col=None)
    else:
        print('Something went wrong...')
    return df


def visualize_tree(tree, feature_names, target_names):
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
    dot_data = export_graphviz(tree, out_file=None,
                               feature_names=feature_names,
                               class_names=target_names,
                               filled=True, rounded=True,
                               special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("package.pdf")
    # Image(graph.create_png())
    # command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
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


df = get_data('packages')

targetName = 'STATE'

print("* df.head()", df.head(), sep="\n", end="\n\n")
print("* df.tail()", df.tail(), sep="\n", end="\n\n")
print("* states types:", df[targetName].unique(), sep="\n")

df2, targets = encode_target(df, targetName)
print("* df2.head()", df2[["Target", targetName]].head(), sep="\n", end="\n\n")
print("* df2.tail()", df2[["Target", targetName]].tail(), sep="\n", end="\n\n")
print("* targets", targets, sep="\n", end="\n\n")

features = list(df2.columns[:6])
print("* features:", features, sep="\n")

y = df2['Target']
X = df2[features]

# dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

dt = DecisionTreeClassifier()

dt.fit(X, y)

visualize_tree(dt, features, targets)

# PREDICTING FEATURES


# set = df2[features]
set = [7.2, 3.1, 6.1, 1.7, 3, 3]
set = np.array(set)
set = set.reshape(1, -1)
print(set)
predict_result = dt.predict(set)
print(predict_result)
predict_result = [targets[i] for i in predict_result]
print(predict_result)

df3 = get_data('packages_test')

predict_result = dt.predict(df3)
print(predict_result)
predict_result = [targets[i] for i in predict_result]
print(predict_result)

testList = [[1, 0, 6.082762530298219, 2.8284271247461903, 2.23606797749979, 8.602325267042627], [2, 1.4142135623730951, 0, 2.8284271247461903, 2.23606797749979, 8.602325267042627]]
testList = np.array(testList)
print(testList)
predict_result = dt.predict(testList)
print(predict_result)
predict_result = [targets[i] for i in predict_result]
print(predict_result)