# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:51:26 2022

@author: ual-laptop
"""

# Write your code here :-)
from pybliometrics.scopus import AffiliationRetrieval
from pybliometrics.scopus import AffiliationSearch
import csv

def affliations(author_list):

    '''
    This function takes a list of authors and uses the SCOPUS database to
    search for affiliated institutions and EID.
    Parameter:
        author_list: this is the list of authors we want the affiliations and
        and EIDs for.
    Returns:
       diction: This is a dictionary containing the affliations. It has 5 keys as categories.
           Each key has a list as its value. The list has the affliations stored.
    '''
    EID_list=[]
    diction={"Name":[],"Organisation":[],"Address":[],"Organisation Domain":[],"Organisation URL":[] }
    author_count=[]
    document_count=[]
    
    for name in author_list:
        query= "AFFIL(name)"
        EID= AffiliationSearch(query)
        #The class AffliationSearch mostly serves to provide a list of
        #named tuples storing information about the affiliation.
        #One of them is the affiliation ID which we use for
        #the AffiliationRetrieval class.

        for ids in EID.affiliations:
            ids= ids[0].split('-')
            #ids[0] is the affiliation ID
            #AffiliationRetrieval provides basic information
            #on registered affiliations,
            #like city, country, its members, and more
            #affiliation_list.append(institution)
            
            aff= AffiliationRetrieval(ids[-1])
            EID_list.append(ids[-1])
            author_count.append(aff.author_count)
            document_count.append(aff.document_count)
            
            diction['Name'].append(aff.affiliation_name)
            diction['Organisation'].append(aff.org_type)
            diction['Address'].append(f'{aff.city},{aff.state},{aff.country},{aff.postal_code}')
            diction['Organisation Domain'].append(aff.org_domain)
            diction['Organisation URL'].append(aff.org_URL)
            
    #with open("test.csv", "w") as outfile:
 
    # pass the csv file to csv.writer function.
        #writer = csv.writer(outfile)
 
    # pass the dictionary keys to writerow
    # function to frame the columns of the csv file
        #writer.writerow(diction.keys())
   
    # make use of writerows function to append
    # the remaining values to the corresponding
    # columns using zip function.
        #writer.writerows(zip(*diction.values()))
    print (len(author_count))
    return diction


author_list= ['Michael F. Brown']
diction= affliations(author_list)

print (diction)


