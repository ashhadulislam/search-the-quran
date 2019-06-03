import pandas as pd
from . import constants
from . import search_functions
import os
import pickle

import json



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
	data_dict=search_functions.search_word_in_quran_dict(word,get_from_pickle(pkl_location+mapping_dict),get_from_pickle(pkl_location+reject_list),df)
	data_json = json.dumps(data_dict)
	return data_json

	
	
	

