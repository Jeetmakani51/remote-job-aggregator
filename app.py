import streamlit as st
import pandas as pd

df = pd.read_csv(r"jobs.csv")

st.header("Remote job Dashboard")
st.write("Explore remote jobs scraped from WeWorkRemotely")
st.divider()
total_jobs, ai_jobs = st.columns(2)
python_jobs, salary_given = st.columns(2)

total_jobs.metric("Total Jobs", 238, border = True)
ai_jobs.metric("AI Jobs", 23, border = True)
python_jobs.metric("Python Jobs", 5, border = True)
salary_given.metric("Salaries given", 35, border = True)
st.divider()
search_bar = st.text_input("Search Jobs")
st.write("you can search about - python, AI, devops, Senior Product Manager")

search_jobs = df[df['job-title'].str.contains(search_bar,case = False, na = False)]   

location_filter = st.sidebar.selectbox(
    "Location",
    ["All"] + sorted(df["company-location"].unique().tolist())
)

company_filter = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["company-name"].unique().tolist())
)

salary_filter = st.sidebar.checkbox(
    "Show only jobs with salary"
)

filtered_df = df.copy()

if location_filter != "All":
    filtered_df = filtered_df[
        filtered_df["company-location"] == location_filter
    ]

if company_filter != "All":
    filtered_df = filtered_df[
        filtered_df["company-name"] == company_filter
    ]

if salary_filter:
    filtered_df = filtered_df[
        filtered_df["salary"] != "not provided"
    ]

if search_bar:
    filtered_df = filtered_df[
        filtered_df["job-title"].str.contains(
            search_bar,
            case=False,
            na=False
        )
    ]

st.dataframe(filtered_df)

common_job_locations = df['company-location'].value_counts().head(10).sort_values(ascending = False)
st.subheader("Most Common Job Locations")
st.bar_chart(common_job_locations)

common_job_titles = df['job-title'].value_counts().head(10).sort_values(ascending = False)
st.subheader("Most Common Job Titles")
st.bar_chart(common_job_titles)

top_companies = df['company-name'].value_counts().head(10).sort_values(ascending = False)
st.subheader("Top Hiring Companies")
st.bar_chart(top_companies)