# Generate a Phoeneme distribution for the text. 
import nltk
import epitran
from nltk.corpus import brown
ep_eng= epitran.Epitran('eng-Latn')
import time
phoeneme_sents=[]
L=len(brown.sents())
print(L)
cnt=0
st=time.time()
for sent in brown.sents():
    cnt+=1
    if cnt%500==0:
        print(cnt*100/L)
        print(time.time()-st)
        st=time.time()
    doc= " ".join(sent)
    phoeneme_sents.append(ep_eng.transliterate(doc))

import pickle
with open('phoneme_sents.p','wb')as handle:
	pickle.dump(phoeneme_sents,handle)

