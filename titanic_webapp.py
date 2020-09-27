import streamlit as st
import pickle
import time

model=pickle.load(open('model.pkl','rb'))

   
def main():
    # st.title("Titanic Survival Prediction")
    html_temp = """
    <style>
    
    #textspace {
    color: white;
    background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);
    text-align:left;
    font-family: Copperplate;
    border-radius:10px;
    border-style: solid;
    padding:10px;
    }
    
    </style>
    
    <div id='textplace'>
        <h1>Titanic Survival Prediction</h1>
    </div>
    
    <h4 style="color:black;text-align:left;">Enter the details of the traveller:</h2>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    # activities=['Logistic Regression','Decision Tree','Random Forrest','Support Vector','K-Neighbours']
    # option=st.sidebar.selectbox('Which model would you like to use?',activities)
    # st.subheader(option)

    pclass=st.radio("Ticket Class:",(1,2,3))
    
    g=st.radio("Gender:",('Male', 'Female'))
    if g=="Male":
        gender=1
    else:
        gender=0
          
    
    age=st.slider('Age:',max_value=100) 
    
    sibsp =st.slider('# of siblings / spouses aboard:',max_value=10)
    
    parch =st.slider('# of parents / children aboard:',max_value=10)
    
    fare=st.number_input('Ticket Fare ($):', min_value=0.0, max_value=100.0,step=0.1)
    
    emb=st.radio("Port of Embarkation:",('Cherbourg', 'Queenstown','Southampton'))[0]
    if emb=="C":
        embarked=1
    elif emb=="S":
        embarked=0
    else:
        embarked=2
    
    inputs=[[pclass, gender, age, sibsp, parch, fare, embarked]]
    
    
    prediction = model.predict(inputs)
    pred = prediction[0]

    if st.button('Predict!'):
        if pred ==1:
            with st.spinner('Loading...'):
                time.sleep(2)
            with st.spinner('Hmm...looks like your traveller..'):
                time.sleep(3)
            st.success("SURVIVED")
            st.balloons()
            time.sleep(0.3)
            st.balloons()
            time.sleep(0.3)
            st.balloons()
        else: 
            with st.spinner('Loading...'):
                time.sleep(2)
            with st.spinner('Hmm...looks like your traveller..'):
                time.sleep(3)
            st.error("Didn't Survive...RIP")
        

if __name__=='__main__':
    main()
