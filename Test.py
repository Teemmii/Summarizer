
import os
from dotenv import find_dotenv, load_dotenv
import openai
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

#==== Using OpenAI Chat API =======
llm_model = "gpt-3.5-turbo"
open_ai = OpenAI(temperature=0.7)

def generate_readout(specialty, name):
    template = """ 
        As a read out manager, please come up with a simple read out (1200 words) of key clinical trails stages by pharmaceutical companys in the last one year based on specialties
        {specialties}
        and the main companies {name}
        
        STORY:
    """

    prompt = PromptTemplate(input_variables=["specialties", "name"],
                            template=template)

    chain_story = LLMChain(llm=open_ai, prompt=prompt, verbose=True)
    response = chain_story({"specialties": specialty, "name": name})

    #print(story['text'])
    
    return response

def main():
    st.set_page_config(page_title="Generate ReadOut",
                       layout="centered")
    st.title("Let AI generate Clinical readout for you 📖")
    st.header("Get Started...")
    
    Specialty_input = st.text_input(label="What TA are you intrested?")
    Company_input = st.text_input(label="What Pharma company are you intrested?")
    #language_input = st.text_input(label="Translate the story into...")
    
    submit_button = st.button("Submit")
    if Specialty_input and Company_input:
        if submit_button:
            with st.spinner("Generating Read Out..."):
                response = generate_readout(specialty=Specialty_input,
                                            name=Company_input
                                            )
                
                with st.expander("English Version"):
                    #st.write(response)
                    st.write(response)
                #with st.expander(f"{language_input} Version"):
                    #st.write(response['translated'])
                
            st.success("Read Out Successfully Generated!")









#invoking the main function
if __name__ == '__main__':
    main()
