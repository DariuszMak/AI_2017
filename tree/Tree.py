import csv
import collections

class DecisionTree:

    def __init__(self, col=-1, value=None, trueBranch=None, falseBranch=None, results=None):
        self.col = col
        self.value = value
        self.trueBranch = trueBranch
        self.falseBranch = falseBranch
        self.results = results

def divideSet(rows, column, value):
    splittingFunction = None
    if isinstance(value, int) or isinstance(value, float):
        splittingFunction = lambda row: row[column] >= value
    else:
        splittingFunction = lambda row: row[column] == value
    list1 = [row for row in rows if splittingFunction(row)]
    list2 = [row for row in rows if not splittingFunction(row)]
    return (list1, list2)


def uniqueCounts(rows):
    results = {}
    for row in rows:
        r = row[-1]
        if r not in results: results[r] = 0
        results[r] += 1
    return results

def entropy(rows):
    from math import log
    log2 = lambda x: log(x) / log(2)
    results = uniqueCounts(rows)

    entr = 0.0
    for r in results:
        p = float(results[r]) / len(rows)
        entr -= p * log2(p)
    return entr

def gini(rows):
    total = len(rows)
    counts = uniqueCounts(rows)
    imp = 0.0

    for k1 in counts:
        p1 = float(counts[k1]) / total
        for k2 in counts:
            if k1 == k2: continue
            p2 = float(counts[k2]) / total
            imp += p1 * p2
    return imp

def variance(rows):
    if len(rows) == 0: return 0
    data = [float(row[len(row) - 1]) for row in rows]
    mean = sum(data) / len(data)

    variance = sum([(d - mean) ** 2 for d in data]) / len(data)
    return variance


def growDecisionTreeFrom(rows, evaluationFunction=entropy):

    if len(rows) == 0: return DecisionTree()
    currentScore = evaluationFunction(rows)

    bestGain = 0.0
    bestAttribute = None
    bestSets = None

    columnCount = len(rows[0]) - 1  # last column is the result/target column
    for col in range(0, columnCount):
        columnValues = [row[col] for row in rows]

        for value in columnValues:
            (set1, set2) = divideSet(rows, col, value)

            # Gain -- Entropy or Gini
            p = float(len(set1)) / len(rows)
            gain = currentScore - p * evaluationFunction(set1) - (1 - p) * evaluationFunction(set2)
            if gain > bestGain and len(set1) > 0 and len(set2) > 0:
                bestGain = gain
                bestAttribute = (col, value)
                bestSets = (set1, set2)

    if bestGain > 0:
        trueBranch = growDecisionTreeFrom(bestSets[0])
        falseBranch = growDecisionTreeFrom(bestSets[1])
        return DecisionTree(col=bestAttribute[0], value=bestAttribute[1], trueBranch=trueBranch,
                            falseBranch=falseBranch)
    else:
        return DecisionTree(results=uniqueCounts(rows))


def prune(tree, minGain, evaluationFunction=entropy, notify=False):
    # recursive call for each branch
    if tree.trueBranch.results == None: prune(tree.trueBranch, minGain, evaluationFunction, notify)
    if tree.falseBranch.results == None: prune(tree.falseBranch, minGain, evaluationFunction, notify)

    # merge leaves (potentionally)
    if tree.trueBranch.results != None and tree.falseBranch.results != None:
        tb, fb = [], []

        for v, c in tree.trueBranch.results.items(): tb += [[v]] * c
        for v, c in tree.falseBranch.results.items(): fb += [[v]] * c

        p = float(len(tb)) / len(tb + fb)
        delta = evaluationFunction(tb + fb) - p * evaluationFunction(tb) - (1 - p) * evaluationFunction(fb)
        if delta < minGain:
            if notify: print('A branch was pruned: gain = %f' % delta)
            tree.trueBranch, tree.falseBranch = None, None
            tree.results = uniqueCounts(tb + fb)


def classify(observations, tree, dataMissing=False):

    def classifyWithoutMissingData(observations, tree):
        if tree.results != None:  # leaf
            return tree.results
        else:
            v = observations[tree.col]
            branch = None
            if isinstance(v, int) or isinstance(v, float):
                if v >= tree.value:
                    branch = tree.trueBranch
                else:
                    branch = tree.falseBranch
            else:
                if v == tree.value:
                    branch = tree.trueBranch
                else:
                    branch = tree.falseBranch
        return classifyWithoutMissingData(observations, branch)

    def classifyWithMissingData(observations, tree):
        if tree.results != None:  # leaf
            return tree.results
        else:
            v = observations[tree.col]
            if v == None:
                tr = classifyWithMissingData(observations, tree.trueBranch)
                fr = classifyWithMissingData(observations, tree.falseBranch)
                tcount = sum(tr.values())
                fcount = sum(fr.values())
                tw = float(tcount) / (tcount + fcount)
                fw = float(fcount) / (tcount + fcount)
                result = collections.defaultdict(
                    int)
                for k, v in tr.items(): result[k] += v * tw
                for k, v in fr.items(): result[k] += v * fw
                return dict(result)
            else:
                branch = None
                if isinstance(v, int) or isinstance(v, float):
                    if v >= tree.value:
                        branch = tree.trueBranch
                    else:
                        branch = tree.falseBranch
                else:
                    if v == tree.value:
                        branch = tree.trueBranch
                    else:
                        branch = tree.falseBranch
            return classifyWithMissingData(observations, branch)

    # function body
    if dataMissing:
        return classifyWithMissingData(observations, tree)
    else:
        return classifyWithoutMissingData(observations, tree)


def plot(decisionTree):

    def toString(decisionTree, indent=''):
        if decisionTree.results != None:  # leaf node
            return str(decisionTree.results)
        else:
            if isinstance(decisionTree.value, int) or isinstance(decisionTree.value, float):
                decision = 'Column %s: x >= %s?' % (decisionTree.col, decisionTree.value)
            else:
                decision = 'Column %s: x == %s?' % (decisionTree.col, decisionTree.value)
            trueBranch = indent + 'yes -> ' + toString(decisionTree.trueBranch, indent + '\t\t')
            falseBranch = indent + 'no  -> ' + toString(decisionTree.falseBranch, indent + '\t\t')
            return (decision + '\n' + trueBranch + '\n' + falseBranch)

    print(toString(decisionTree))


def loadCSV(file):

    def convertTypes(s):
        s = s.strip()
        try:
            return float(s) if '.' in s else int(s)
        except ValueError:
            return s

    reader = csv.reader(open(file, 'rt'))
    return [[convertTypes(item) for item in row] for row in reader]

def calculateTest(testData, decisionTree):

    numbergood = 0
    number = 0

    for row in testData:
        result = classify([row[0], row[1], row[2], row[3]], decisionTree)
        for key in result:
            if key == row[4]:
                numbergood += 1
        number += 1

    percent = numbergood / number * 100
    return print("Skuteczność wynosi %s %%" % (percent))