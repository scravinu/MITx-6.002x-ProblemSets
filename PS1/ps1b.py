###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Sharad Chand Ravinuthala
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    toConsider = sorted(egg_weights,reverse=True)
    avail = target_weight
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
    return countingFastMaxVal(toConsider,avail,memo)
# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()