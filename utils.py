def TrimOutliers(dfIn, colName, floorThreshold, ceilingThreshold):
    '''
    INPUT - dfIn - pandas dataframe including outliers
            colName - column to clean up
            floorThreshold - lower bound for trimming
            ceilingThreshold - upper bound for trimming
    OUTPUT - 
            Dataframe with trimmed column
    '''
    floor = dfIn[colName].quantile(floorThreshold)
    ceiling = dfIn[colName].quantile(ceilingThreshold)

    index = dfIn[(dfIn[colName] >= ceiling)|(dfIn[colName] <= floor)].index
    dfIn.drop(index, inplace=True)
    return dfIn

