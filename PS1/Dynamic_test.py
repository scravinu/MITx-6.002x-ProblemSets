# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:00:13 2020

@author: Sharad
"""


def countingFastMaxVal(toConsider,avail,memo):
        if (len(toConsider), avail) in memo:
            result = memo[(len(toConsider), avail)]
        elif toConsider == [] or avail == 0:
            result = (0, ())
        elif toConsider[0] > avail:
            #Explore right branch only
            result = countingFastMaxVal(toConsider[1:], avail, memo)
        else:
            nextItem = toConsider[0]
            #Explore left branch
            withVal, withToTake =\
                     countingFastMaxVal(toConsider[:],
                                avail - nextItem, memo)
            withVal += nextItem
            withToTake += (nextItem,)
             #Explore right branch
            withoutVal, withoutToTake = countingFastMaxVal(toConsider[1:],
                                                    avail, memo)
            #Choose better branch
            if withVal >= withoutVal:
                result = (withVal, withToTake)
            else:
                result = (withoutVal, withoutToTake)
        memo[(len(toConsider), avail)] = result
        return result
    
egg_weights = [20,15,10]
n = 45
memo = {}
res = countingFastMaxVal(egg_weights,n,memo)