import pandas as pd
import random
import random-username



## Multiple functions that help generate random data. Our goal is to simulate data flow similar to a e-commerce site. DAG will be run every hour. Purposely making these csv tables disorganized so there is an actual transformation process

#Load in productcsv


df = pd.read_csv('product.csv')

product = df['price'].tolist()





# Function that generates a randomized number of orders in the last



def orderbatch():
    # Generate a random number of records
    numberoforders = random.randrange(0,10)
    dic = {'product':[],'quantity':[]}
    for i in range(numberoforders):
        #appends a random product
        dic['product'].append(random.choice(product))
        dic['quantity'].append(random.randrange(0,10))



    # load raw data into S3







#Function that generates new users joined in the last hour 
#

def newusers():
    # Generate a random number of records
    numberofnewusers = random.randrange(0,10)
    dictionary = {'Username':[],'First Name':[],'Last Name':[],'State':[],'City':[]}


    for i in numberofnewusers:







    # load raw data into S3










## Function that generates inventory left


def invenbatch():



# load raw data into S3