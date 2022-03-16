# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:17:43 2022

@author: DEKELCO
"""

E1_S = '[E1]' 
E1_E = '[/E1]'
E2_S = '[E2]' 
E2_E = '[/E2]'

def remove_substr(strng,substr):
    s_idx = strng.find(substr)
    new_strng = strng[0:s_idx] + strng[s_idx+ len(substr):]
    return s_idx, new_strng
    
def convert_markers_to_positions(sent):
    """
    Convert RE formats from text-embedded markers [E1] --> head, tail positions as dicts
    'The CEO of [E1]IBM[\E1] , [E2]Steve Cohen[\E2]'  --> {'text': 'The CEO of IBM , Steve Cohen', 'h': {'pos': (11, 14)},'t': {'pos': (17, 28)}}
    """
    sent_new = sent.replace('[\\','[/') # in case [\\E1] --> normalize to [/E1]
    s_e1,sent_new = remove_substr(sent_new,E1_S)
    e_e1,sent_new = remove_substr(sent_new,E1_E)
    s_e2,sent_new = remove_substr(sent_new,E2_S)
    e_e2,sent_new = remove_substr(sent_new,E2_E)
    return { 'text' : sent_new, 'h' : { 'pos' : (s_e1,e_e1)}, 't' : { 'pos' : (s_e2,e_e2)}}
    
    
    
    
def test():
    samp = convert_markers_to_positions(sent = 'The CEO of [E1]IBM[\E1] , [E2]Steve Cohen[\E2]')
    print(samp['text'].find('Cohen'))

if __name__=="__main__":
    test() 

