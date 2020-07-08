def yrs_in_min(no):
    return no*365
def yrs_in_hrs(no):
    return no/60

def min_to_hrs(no):
    return no/60
def hrs_to_days(no):
    return no/24
def days_to_yrs(no):
    return no/365



if __name__=="__main__":
    
    minutes=int(input("How many minutes you will take to finish a food: "))#no of minutes for single food
    times=int(input("How many times you take daily food: ")) #no of meals daily
    total_per_day=minutes*times  #single day time to take food in minutes
    years_in_min=yrs_in_min(total_per_day)
    years_in_hours=yrs_in_hrs(years_in_min)
    
    
    lifespan=int(input("Enter total lifespan in years: "))
    
    lifespan_in_hrs=lifespan*years_in_hours
    
    lifespan_in_days=hrs_to_days(lifespan_in_hrs)
    lifespan_in_year=days_to_yrs(lifespan_in_days)
    
    print('\nAccording to your inputs:')
    print('An Human will take food throuh out the lifetime is %s Hours'%(lifespan_in_hrs))
    print('An Human will take food throuh out the lifetime is %s Days'%(lifespan_in_days))
    print('An Human will take food throuh out the lifetime is %s Years'%(lifespan_in_year))
    
    per=((lifespan_in_year)/(lifespan))*100
    print('In total of 100 % life of Human about {} % of life they spend in taking food'.format(per))