

import pandas as pd 
import streamlit as st 
import numpy as np

# Title of the app
st.title("NALEDI KHATI")

# Collect basic information
name = "**Naledi Khati**"
field = "**Computational Chemistry**"
Institution = "**University of the Witwatersrand**"


# Page configuration

st.set_page_config(
    page_title="Researcher Profile",
    page_icon="🧪",
    layout="wide"
)

# Sidebar

st.sidebar.title("Profile Navigation")
section = st.sidebar.radio(
    "Jump to:",
    ["About", "Research Interests", "Skills", "Contact"]
)

st.sidebar.markdown("---")

# Header

st.subheader("Electrochemistry | Energy Materials | Machine Learning")
st.write(
    "Translating fundamental science into scalable energy solutions. "
    
)
st.write(f"Name: {name}")
st.write(f"Field: {field}")
st.write(f"Institution: {Institution}")

st.markdown("---")


# About

if section == "About":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://d2cbg94ubxgsnp.cloudfront.net/Pictures/2000xAny/2/2/8/132228_Computational-chemistry-concept_GettyImages-503260821_credit-DigitalVision-Vectors_Getty-Images.jpg",
            width=10000
        )
        

    with col2:
        st.markdown("### About Me")
        st.write(
            """
            I am a researcher specializing in electrocatalysis and energy storage materials.
            My work sits at the intersection of lectrochemistry, computational modeling,
            and machine learning, with a focus on sustainable battery technologies.
            """
        )

# Research Interests

elif section == "Research Interests":
    st.markdown("### Research Interests")
    st.markdown(
        """
        - Oxygen Evolution & Oxygen Reduction Reactions (OER/ORR)  
        - Rechargeable Zinc–Air Batteries (RZABs)  
        - Spinel Oxide Electrocatalysts  
        - Density Functional Theory (DFT)  
        - Machine Learning for Materials Discovery  
        - Sustainable Energy Systems  
        """
    )

# Skills

elif section == "Skills":
    st.markdown("### Technical Skill Set")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Experimental**")
        st.write(
            """
            - Electrochemical Testing
            - Electrochemical Impedance Spectroscopy (EIS)   
            - Battery Testing & Analysis  
            """
        )

    with col2:
        st.markdown("**Computational & Data**")
        st.write(
            """
            - DFT (CASTEP, Materials Studio)  
            - Python (NumPy, Pandas, Scikit-learn)  
            - Machine Learning for Materials  
            """
        )

# Contact

elif section == "Contact":
    st.markdown("### Contact")

    st.write("📧 naledikhati1@student.wiuts.ac.za")
    st.write("🔗 www.linkedin.com/in/naledi-khati-b97a18230")

    st.markdown("---")
    st.caption("Open to collaboration")

#

