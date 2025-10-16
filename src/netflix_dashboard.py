import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("../data/netflix_titles.csv")
    df.drop_duplicates(inplace=True)
    return df

df = load_data()

st.sidebar.title("🎬 Netflix Content Dashboard")
st.sidebar.markdown("Explore Netflix’s catalog interactively")

type_filter = st.sidebar.multiselect("Select Type", df["type"].unique(), default=df["type"].unique())
country_filter = st.sidebar.multiselect("Select Country", df["country"].dropna().unique()[:50])
year_range = st.sidebar.slider("Select Release Year Range", int(df["release_year"].min()), int(df["release_year"].max()), (2010, 2020))

filtered_df = df[
    (df["type"].isin(type_filter)) &
    (df["release_year"].between(year_range[0], year_range[1])) &
    (df["country"].fillna("Unknown").isin(country_filter) if country_filter else True)
]

st.title("🎥 Netflix Content Strategy Dashboard")

st.markdown(f"### Showing {len(filtered_df)} titles from {year_range[0]} to {year_range[1]}")


st.subheader("Content Type Distribution")
type_counts = filtered_df["type"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]

fig1 = px.pie(
    type_counts,
    values="Count",
    names="Type",
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig1, use_container_width=True)


st.subheader("Content Growth by Year")
growth = filtered_df.groupby(["release_year", "type"]).size().reset_index(name="count")
fig2 = px.bar(growth, x="release_year", y="count", color="type", barmode="group")
st.plotly_chart(fig2, use_container_width=True)


st.subheader("Top 10 Genres")
top_genres = (
    filtered_df["listed_in"]
    .str.split(", ", expand=True)
    .stack()
    .value_counts()
    .head(10)
    .reset_index()
)
top_genres.columns = ["Genre", "Count"]

fig3 = px.bar(
    top_genres,
    x="Genre",
    y="Count",
    color="Genre",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig3, use_container_width=True)


st.subheader("Top Producing Countries")
top_countries = filtered_df["country"].value_counts().head(10).reset_index()
top_countries.columns = ["Country", "Count"]

fig4 = px.bar(
    top_countries,
    x="Country",
    y="Count",
    color="Country",
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig4.update_layout(
    xaxis_title="Country",
    yaxis_title="Number of Titles",
    showlegend=False
)
st.plotly_chart(fig4, use_container_width=True)



st.subheader("📊 Data Preview")
st.dataframe(filtered_df.head(20))
