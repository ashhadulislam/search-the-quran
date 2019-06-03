import nltk 
from nltk.corpus import wordnet 
import re
from operator import itemgetter
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 

from nltk.corpus import words

def get_sorted_list_tuple(word,list_of_tuples,df):
    '''
    basically convert
    {word:[(surah#,verse#)(surah#,verse#)(surah#,verse#)(surah#,verse#)]}
    into
    {word:[(surah#,verse#,'max_compare_val')(surah#,verse#,'max_compare_val')(surah#,verse#,'max_compare_val')(surah#,verse#,'max_compare_val')]}
    in sorted order, sorted by max_compare_val
    df is the dataframe containing quranic verses
    Surah,Ayah,Text
    '''
    
#     print("old tuple",list_of_tuples)
    new_list=[]
    for tup in list_of_tuples:
        surah=tup[0]
        ayah=tup[1]
        para=df.loc[(df['Surah'] == surah) & (df['Ayah'] == ayah)]["Text"].iloc[0]
        comp_val=find_max_compare_in_text(word,para)
        new_list.append((surah,ayah,comp_val))
    
#     print("newly generated list of tuples",new_list)
    #now sort the list of tuples
    return sort_list_of_tuples(new_list)
    
    
    

def sort_list_of_tuples(list_tuples):
    '''
    will have list of tuples like
    [
        (s1,v2,dist1),
        (s2,v2,dist2),
        .
        .
        .
        (s100,v100,dist100)
    
    ]
    Need to sort them by the last value of the tuple
    '''
    return sorted(list_tuples,key=itemgetter(2),reverse=True)
    



def find_max_compare_in_text(word, paragraph):
    '''
    word on one hand
    verse on the other
    find the maximum probable match
    '''
    val=0
    word=word.lower()
    for  w in paragraph.split():
#         print(w)
        w = re.sub(r'[^a-zA-Z]', "", w)
        w=w.lower()
        dist=compare_words(word,w)
#         print(w,dist)
        if dist>=val:
            val=dist
    
    return val
        
        




def compare_words(source,dest):
    r1=fuzz.ratio(source, dest) 
#     r2=fuzz.partial_ratio(source, dest) 
#     r3=fuzz.token_sort_ratio(source, dest) 
#     r4=fuzz.token_set_ratio(source, dest)     
    return r1
    


def search_word_in_quran_dict(word,mapper_dict,reject_list,df):
    '''
    this function will return
    {
        word_syn1:[('s#,v#,comp1'),('s#,v#,comp2'),('s#,v#,comp3')],
        word_syn2:[('s#,v#,comp1'),('s#,v#,comp2'),('s#,v#,comp3')],
        word_syn2:[('s#,v#,comp1'),('s#,v#,comp2'),('s#,v#,comp3')], 
    
    }
    comp values are in sorted order for each list
    '''
    word_list=get_synonyms(word)
#     if len(word_list)==0:
#         word_list=[word]
        
    print("Will look for the following words")
    print(word_list)
    new_dict={}
    for w in word_list:    
        print("Looking for ",w)
        if w not in reject_list and w not in mapper_dict.keys():
            print("call")
            mapper_dict_result,reject_list=get_ayahs_from_quran(w)
        if w in reject_list:
            print("Word ",w," is absent from this rendition of Quran")
            print("*********************")            
            continue
        #now find the sorted edit distance for each word and its corresponding tuple values 
        #in the dictinary
        sorted_list_tuples=get_sorted_list_tuple(w,mapper_dict[w],df)
#         print("And after sorting, list of tuple is ",sorted_list_tuples)
        new_dict[w]=[]
        print(w," has the following ocurences in Quran")
        print("*********************")
        
        for tup in sorted_list_tuples:


            verse=df.loc[(df['Surah'] == tup[0]) & (df['Ayah'] == tup[1])]["Text"].iloc[0]
            print("{}\t{}\t{}".format(tup[0],tup[1],verse))
            small_dict={}
            small_dict['Surah']=tup[0]
            small_dict['Ayah']=tup[1]
            small_dict['Text']=verse
            small_dict['Proximity']=tup[2]
            new_dict[w].append(small_dict)
        print("*********************")            
    return new_dict
        
        
        
def get_synonyms(word):
    synonyms = [] 
    antonyms = [] 

    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
  
    return set(synonyms)

