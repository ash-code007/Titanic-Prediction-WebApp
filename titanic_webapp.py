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
    font-family: Goudy Old Style;
    border-radius:20px;
    border-style: solid;
    padding:10px;
    }
    #textspace img {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 5px;
    width: 100%;
    }
    
    </style>
    
    <div id='textspace'>
        <h1 style="font-family: Copperplate Gothic Light; font-variant: small-caps;text-align:center;">Titanic Survival Prediction</h1>
            <div>
               <img src="https://cdn.wallpapersafari.com/9/99/g7mtvV.jpg" align="middle" alt="Titanic Image"/>
            </div><div>
               <p> 
                  The sinking of the Titanic is one of the most infamous shipwrecks in history.
                  <br/><br/>
                  On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. 
                  Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.
                  While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.
                  <br/><br/>
                  In this web-app, you can enter the details of an imaginary traveller (ie name, age, gender, socio-economic class, etc). 
                  and the app will use the help of an ML algorithm to tell you whether your traveller would have survived the catastrophe or not.
               </p>
            </div>
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
