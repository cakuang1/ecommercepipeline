import pandas as pd
import random
from random_username.generate import generate_username
import names



## Multiple functions that help generate random data. Our goal is to simulate data flow similar to a e-commerce site. DAG will be run every hour. Purposely making these csv tables disorganized so there is an actual transformation process

#Load in productcsv


df = pd.read_csv('product.csv')

product = df['price'].tolist()


states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']



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
    dic = {'Username':[],'First Name':[],'Last Name':[],'State':[]}


    for i in numberofnewusers:
        dic['Username'] = generate_username()
        dic['First Name'] = names.get_first_name()
        dic['Last Name'] = names.get_last_name()



        dic['State'] = random.choice(states)




        










    # load raw data into S3










## Function that generates inventory left


def invenbatch():








# load raw data into S3