import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# Page configuration
st.set_page_config(page_title="Corporate Dashboard", layout="centered")

# Function to create the welcome page with links and mascot
def welcome_page():
    st.title("Welcome to the Corporate Dashboard")
    st.write("Navigate to different sections using the links below:")
    st.markdown("[Go to Blog Page](#blog-page)")
    st.markdown("[Go to Data Page](#data-page)")
    
    # Corporate mascot (cartoon image)
    mascot_img = Image.open("mascot_image.png")  # Replace with the path to your mascot image
    st.image(mascot_img, caption="Corporate Mascot", use_column_width=True)

# Function to create the blog page with example blog posts
def blog_page():
    st.header("Blog Page")
    st.subheader("Example Blog Post 1")
    st.write("""
        This is an example blog post. Here, you can discuss the latest corporate updates, news, 
        and insights related to your organization. Keep your audience informed and engaged.
    """)
    
    st.subheader("Example Blog Post 2")
    st.write("""
        Another example post. This post could delve into industry trends, new initiatives, or 
        achievements within the organization.
    """)

    st.subheader("Example Blog Post 3")
    st.write("""
        Use this space to share thought leadership or announce upcoming events. The blog is an 
        excellent platform to build engagement with your readers.
    """)

# Function to create the data page with example charts and graphs
def data_page():
    st.header("Data Page")

    # Line chart with dummy data
    st.subheader("Line Chart 1")
    data1 = pd.DataFrame({
        'x': np.arange(1, 11),
        'y': np.random.randint(10, 100, 10)
    })
    fig1 = px.line(data1, x='x', y='y', title="Line Chart 1")
    st.plotly_chart(fig1, use_container_width=True)

    # Line chart with different dummy data
    st.subheader("Line Chart 2")
    data2 = pd.DataFrame({
        'x': np.arange(1, 21),
        'y': np.random.randint(10, 200, 20)
    })
    fig2 = px.line(data2, x='x', y='y', title="Line Chart 2")
    st.plotly_chart(fig2, use_container_width=True)

    # Bar chart with dummy data
    st.subheader("Bar Chart 1")
    data3 = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': np.random.randint(10, 100, 4)
    })
    fig3 = px.bar(data3, x='Category', y='Values', title="Bar Chart 1")
    st.plotly_chart(fig3, use_container_width=True)

    # Scatter plot with dummy data
    st.subheader("Scatter Plot")
    data4 = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50)
    })
    fig4 = px.scatter(data4, x='x', y='y', title="Scatter Plot")
    st.plotly_chart(fig4, use_container_width=True)

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page:", ("Welcome", "Blog", "Data"))

# Display selected page
if page == "Welcome":
    welcome_page()
elif page == "Blog":
    blog_page()
elif page == "Data":
    data_page()
