def convertPickle(fn):
    """ Quick module to standardize a .pickle saved gene panel and convert it to human readable JSON format. """
    import pickle
    import json
    
    baseDir = '../Results/Gene Panels/'

    # Load "bad genes" to ensure none are included
    with open("../Data/badGenes.json", "r") as f:
        badGenes = json.load(f)
    badGenes = set(badGenes)

    # Load .pickle gene panel
    with open(baseDir + fn + '.pickle', 'rb') as f:
        panel = pickle.load(f)

    # Create standardized dictionary where keys are panel length of acceptable genes
    panelDict = {}
    for key in panel.keys():
        # Remove "bad genes"
        geneList = list(set(panel[key]) - badGenes)
        panelDict[len(geneList)] = geneList

    with open(baseDir + fn + '.json', "w") as f:
        json.dump(panelDict, f, indent=4)
        
def convertCSV(fn,csvIndx = 1):
    """ Quick module to standardize a .csv saved gene panel and convert it to unscreened .pickle and screened JSON """
    import pandas as pd
    import pickle
    import json
    
    baseDir = '../Results/Gene Panels/'
    
    # Load "bad genes" to ensure none are included
    with open("../Data/badGenes.json", "r") as f:
        badGenes = json.load(f)
    badGenes = set(badGenes)    
    
    # Load csv
    panelDF = pd.read_csv('../Data/' + fn + '.csv')
    panel = {len(panelDF.iloc[:,csvIndx]) : list(panelDF.iloc[:,csvIndx])}
    
    # Resave as .pickle
    with open(baseDir + fn + '.pickle', "wb") as f:
        pickle.dump(panel, f)
    
    # Create standardized dictionary where keys are panel length of acceptable genes
    panelDict = {}
    for key in panel.keys():
        # Remove "bad genes"
        geneList = list(set(panel[key]) - badGenes)
        panelDict[len(geneList)] = geneList
    
    with open(baseDir + fn + '.json', "w") as f:
        json.dump(panelDict, f, indent=4)
