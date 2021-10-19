#Code to calculate how long it would take to afford a new car, taking in a new car price, the price of the old car, the amount saved each month, and the amount of value both cars lose per month
#the amount lost per month goes up by .5 every 2 months

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    amountAvailable = startPriceOld - startPriceNew
    months = 0
    if amountAvailable > 0:
        return [months, amountAvailable]
    while amountAvailable < 0:
        months = months + 1
        if months % 2 == 0:
            percentLossByMonth = percentLossByMonth + .5
        differenceOld = startPriceOld * (percentLossByMonth/100)
        differenceNew = startPriceNew * (percentLossByMonth/100)
        startPriceOld = startPriceOld - differenceOld
        startPriceNew = startPriceNew - differenceNew
        if months == 1:
            amountAvailable = startPriceOld - startPriceNew + savingperMonth
        if months > 1:
            amountAvailable = amountAvailable - (differenceOld - differenceNew) + savingperMonth
    amountAvailable = round(amountAvailable, 0)
    return [months, int(amountAvailable)]
    
    
    
    
    ##############
    ##Better Way##
    ##############
    
def nbMonths(priceold, pricenew, savingperMonth, percentloss):
# define a month and saving variable
    month = 0
    saving = 0
    
# use a while loop to repeat every month until the savings are more than the price of the new car.             
    while pricenew > saving + priceold:
    # check if price of old car is larger than new, and break if needed.
        if priceold >= pricenew:
            break
    # start the month with counting the months, and if it is an even month, increase percent loss.        
        month += 1     
        if month%2==0 and month != 0:
            percentloss+=0.5
    # adjust the values of the cars by percent loss and increase savings.        
        pricenew -= (pricenew*percentloss)/100
        priceold -= (priceold*percentloss)/100
        saving += savingperMonth

    # once the while loop has ended, we can return the necessary information to the customer (must assign leftover again as it was within the while loop earlier). 
    leftover = priceold - pricenew + saving
    return [month,round(leftover,0)]
