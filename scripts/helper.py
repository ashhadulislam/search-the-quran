import pandas as pd
from . import constants
from . import search_functions
import os
import pickle
import time

import json

import zipfile

def read_and_reformat(csv_path):
    df = pd.read_csv(csv_path,dtype=object)
    return df


def get_from_pickle(pkl_location):
    if os.path.isfile(pkl_location):
        var=open(pkl_location,"rb")
        var = pickle.load(var)
        return var

df=None
mapping_dict=None
reject_list=None
pkl_location=None

def setup():
    data_location=constants.data_dir
    file1=constants.file1
    
    global df
    df=read_and_reformat(data_location+file1)
    print("dataframe read")

    global pkl_location
    pkl_location=constants.pkl_dir

    global reject_list
    reject_list=constants.list_reject
    print("reject list {}".format(reject_list))
    # reject_list=get_from_pickle(pkl_location+reject_list)

    global mapping_dict
    mapping_dict=constants.dict_mapping
    # mapping_dict=get_from_pickle(pkl_location+mapping_dict)
    print("mapping dict {}".format(mapping_dict))

    print("Setup done")






def search_for_word(word):
    print("searching for {}".format(word))
    data_dict=get_result(word)
    
    
    data_json = json.dumps(data_dict)
    return data_json

    
    

def get_result(word):
    '''
    check if pkl file for the word exists
    and returns necessary data_dict.
    If pickle not there, do the search,
    create pickle and return the same

    '''
    pkl_file="data/pickles/"+word+".pkl"

    if os.path.isfile(pkl_file):
        print("Relax! Pickle exists")
        isOld=is_more_than_a_week_old(pkl_file)
        print("Is old",isOld)
        if not isOld:
            data_dict=pickle.load(open(pkl_file,"rb"))
            return data_dict

    #this part to do the grunt work
    data_dict=search_functions.search_word_in_quran_dict(word,get_from_pickle(pkl_location+mapping_dict),get_from_pickle(pkl_location+reject_list),df)

    pickle.dump(data_dict,open(pkl_file,"wb"))
    return data_dict


    




def is_more_than_a_week_old(df_pkl_name):
    '''
    this is to check how old the pkl file is 
    '''
    then = os.path.getmtime(df_pkl_name)
    now=time.time()
    minutes_diff=int((now-then)/60)
    print("age of pickle in minutes is ",minutes_diff)
    #number of m inutes in a week
    minutes_in_a_week=(7*24*60)
    if minutes_diff>minutes_in_a_week:
        #too old must build a new pickle
        return True 
    else:
        return False




def zip_all_pickles():
    '''
    Zips all the pickle files 
    Returns the zip
    '''
    zipf = zipfile.ZipFile('data/zips/PklDump.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk('data/pickles/'):
        for file in files:
            zipf.write('data/pickles/'+file)
    zipf.close()
    return True

