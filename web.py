import streamlit as st
import pickle
import pandas as pd 

def recommend(book):
    book_id=books[books['Title']==book]['ids'].values[0]
    score=list(enumerate(sim[book_id]))
    sorted_score=sorted(score,key=lambda x:x[1],reverse=True)
    sorted_score=sorted_score[1:]
    bookt=[books[bookt[0]==books["ids"]]["Title"].values[0] for bookt in sorted_score]
    bookg=[books[bookg[0]==books["ids"]]["Genre"].values[0] for bookg in sorted_score]
    bookreco=[bookt[x]+"--" + bookg[x] for x in range(len(bookt))]
    return bookreco
def rec_five(books_list):
    first_five=[]
    c=0
    for b in books_list:
        if c>4:
            break
        c+=1
        first_five.append(b)
    return first_five

booksd = pickle.load(open('books_dict.pkl','rb'))
books = pd.DataFrame(booksd)


sim = pickle.load(open('sim.pkl','rb'))

st.title('Book recommender')    

selected_book=st.selectbox('pls select books',books['Title'].values)
if st.button('Recommend'):
    l=recommend(selected_book)
    reco=rec_five(l)
    for i in reco:
        st.write(i)
       
        