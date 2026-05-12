import pandas as pd
import streamlit as st
import datetime as dt
import numpy as np
import plotly.express as px
import time
from pandas.core.methods.describe import select_describe_func

st.set_page_config(layout='wide', page_title='Edge Fashion')

dfa = pd.read_csv("anarkali_Efashion.csv")
df = pd.read_csv("celeb_Efashion.csv")
dfs = pd.read_csv("saree_Efashion.csv")
dfl = pd.read_csv("lehenga_Efashion.csv")
dfj = pd.read_csv("jacket_Efashion.csv")
dfm = pd.read_csv("modern_Efashion.csv")
dfp = pd.read_csv("peplum_Efashion.csv")
dfk = pd.read_csv("kurta_Efashion.csv")
dfsh = pd.read_csv("sharara_Efashion.csv")
dfc = pd.read_csv("cord_Efashion.csv")

final = pd.read_csv("final.csv")
final = final.drop(147)
df['celebrity'] = df['celebrity'].str.replace("Ridhi mehra" , "Ridhi Mehra")
df['celebrity'] = df['celebrity'].str.replace("RIDHI MEHRA" , "Ridhi Mehra")
df['celebrity'] = df['celebrity'].str.replace("House of" , "Summiya")
df['celebrity'] = df['celebrity'].str.replace("Esha gupta" , "Esha Gupta")
df['celebrity'] = df['celebrity'].str.replace("ESHA GUPTA" , "Esha Gupta")
df['celebrity'] = df['celebrity'].str.replace("Diipa Khosla" , "Dipa Khosla")
df['celebrity'] = df['celebrity'].str.replace("GENELIA IN" , "Genelia D_Souza")
df['celebrity'] = df['celebrity'].str.replace("Hanna S" , "Hanna Khan")
df['celebrity'] = df['celebrity'].str.replace("Krithi shetty" , "Krithi Shetty")
df['celebrity'] = df['celebrity'].str.replace("Kriti Kharbanda's" , "Kriti Kharbanda")
df['celebrity'] = df['celebrity'].str.replace("MIRA KAPOOR" , "Mira Kapoor")
df['celebrity'] = df['celebrity'].str.replace("Navdeep kaur" , "Navdeep Kaur")
df['celebrity'] = df['celebrity'].str.replace("Neha nagar" , "Neha Nagar")
df['celebrity'] = df['celebrity'].str.replace("Summiya in" , "Summiya")
df['celebrity'] = df['celebrity'].str.replace("Summiyya in" , "Summiya")
df['celebrity'] = df['celebrity'].str.replace("Summiyya of" , "Summiya")
df['celebrity'] = df['celebrity'].str.replace("SUMMIYYA IN" , "Summiya")


df.loc[107, 'price'] = 153600

st.sidebar.title('🔍 Select for Manually Analyse')



def load_overall_analysis():
    st.set_page_config(
        page_title="Edge Fashion Analysis Dashboard",
        page_icon="📊",
        layout="wide"
    )

    st.title("🚀 Edge Fashion Analysis")
    st.caption("Analyzing Edge Fashion products")
    st.title(" 🎯 Overall Analysis")


    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # =========================
    # Data Preparation
    # =========================

    max_value = final.groupby('category')['price'] \
        .sum() \
        .sort_values(ascending=False)

    count_value = final.groupby('category')['title'] \
        .count() \
        .sort_values(ascending=False)

    count_values = df.groupby('celebrity')['title'] \
        .count() \
        .sort_values(ascending=False)

    # =========================
    # Create Subplots
    # =========================

    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[
            [{"colspan": 2}, None],
            [{}, {}]
        ],
        subplot_titles=(
            "Most Frequent Celebrity",
            "Category-Wise Total Value",
            "No of Items in Each Category"
        )
    )

    # =========================
    # Top Graph
    # =========================

    fig.add_trace(
        go.Bar(
            x=count_values.index,
            y=count_values.values,
            name="Celebrity Count"
        ),
        row=1,
        col=1
    )

    # =========================
    # Bottom Left Graph
    # =========================

    fig.add_trace(
        go.Bar(
            x=max_value.index,
            y=max_value.values,
            name="Total Value"
        ),
        row=2,
        col=1
    )

    # =========================
    # Bottom Right Graph
    # =========================

    fig.add_trace(
        go.Bar(
            x=count_value.index,
            y=count_value.values,
            name="Item Count"
        ),
        row=2,
        col=2
    )

    # =========================
    # Layout
    # =========================

    fig.update_layout(
        height=800,
        showlegend=False,
        title="Fashion Dashboard Analytics"
    )

    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)

    # =========================
    # Show Plot
    # =========================

    st.plotly_chart(fig, use_container_width=True)








    max_celeb = df['price'].max()
    max_anarkali = dfa['price'].max()
    max_lehenga = df['price'].max()
    max_kurta = dfk['price'].max()
    max_peplum = dfp['price'].max()
    max_saree = dfs['price'].max()
    max_sharara = dfsh['price'].max()
    max_jacket = dfj['price'].max()
    max_coord = dfc['price'].max()

    min_celeb = df['price'].min()
    min_anarkali = dfa['price'].min()
    min_lehenga = df['price'].min()
    min_kurta = dfk['price'].min()
    min_peplum = dfp['price'].min()
    min_saree = dfs['price'].min()
    min_sharara = dfsh['price'].min()
    min_jacket = dfj['price'].min()
    min_coord = dfc['price'].min()




    st.title("😎Celebrity")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('1. 🛒Toatl Items', df['title'].count())
    with col2 :
        st.metric('2. 💰Toatl Price Value', f"₹ {df['price'].sum():,.0f}")
    with col3:
        st.metric('3. 📈 Maximum', f"₹ {max_celeb:,.0f}")
    with col4:
        st.metric('4. 📉 Minimun', f"₹ {min_celeb:,.0f}")

    st.markdown("---")
    st.title("👑 Lehengas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfl['title'].count())
    with col2:
        st.metric('2. 💰 Total Price Value',f"₹ {dfl['price'].sum():,.0f}")
    with col3:
        st.metric('📈 Maximum',f"₹ {max_lehenga:,.0f}")
    with col4:
        st.metric('📉 Minimum',f"₹ {min_lehenga:,.0f}")

    st.markdown("---")
    st.title("🥻 Saree Set")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfs['title'].count())

    with col2:
        st.metric(
            '2. 💰 Total Price Value',
            f"₹ {dfs['price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            '📈 Maximum',
            f"₹ {max_saree:,.0f}"
        )

    with col4:
        st.metric(
            '📉 Minimum',
            f"₹ {min_saree:,.0f}"
        )

    st.markdown("---")
    st.title("👗 Anarkali Set")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfa['title'].count())

    with col2:
        st.metric(
            '2. 💰 Total Price Value',
            f"₹ {dfa['price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            '📈 Maximum',
            f"₹ {max_anarkali:,.0f}"
        )

    with col4:
        st.metric(
            '📉 Minimum',
            f"₹ {min_anarkali:,.0f}"
        )

    st.markdown("---")
    st.title("✨ Shararas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfsh['title'].count())

    with col2:
        st.metric(
            '2. 💰 Total Price Value',
            f"₹ {dfsh['price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            '📈 Maximum',
            f"₹ {max_sharara:,.0f}"
        )

    with col4:
        st.metric(
            '📉 Minimum',
            f"₹ {min_sharara:,.0f}"
        )

    st.markdown("---")
    st.title("🧥 Kurta Set")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfk['title'].count())

    with col2:
        st.metric('2. 💰 Total Price Value',f"₹ {dfk['price'].sum():,.0f}")

    with col3:
        st.metric('📈 Maximum',f"₹ {max_kurta:,.0f}")

    with col4:
        st.metric('📉 Minimum',f"₹ {min_kurta:,.0f}")

    st.markdown("---")
    st.title("💃 Co-ord Set")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfc['title'].count())

    with col2:
        st.metric(
            '2. 💰 Total Price Value',
            f"₹ {dfc['price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            '📈 Maximum',
            f"₹ {max_coord:,.0f}"
        )

    with col4:
        st.metric(
            '📉 Minimum',
            f"₹ {min_coord:,.0f}"
        )

    st.markdown("---")
    st.title("👚 Peplum Set")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfp['title'].count())

    with col2:
        st.metric(
            '2. 💰 Total Price Value',
            f"₹ {dfp['price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            '📈 Maximum',
            f"₹ {max_peplum:,.0f}"
        )

    with col4:
        st.metric(
            '📉 Minimum',
            f"₹ {min_peplum:,.0f}"
        )

    st.markdown("---")
    st.title("🧥 Jackets")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('1. 🛒 Total Items', dfj['title'].count())

    with col2:
        st.metric(
            '2. 💰 Total Price Value',
            f"₹ {dfj['price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            '📈 Maximum',
            f"₹ {max_jacket:,.0f}"
        )

    with col4:
        st.metric(
            '📉 Minimum',
            f"₹ {min_jacket:,.0f}"
        )


def load_category_analysis(selected_category):
    st.title(selected_category)

    filtered_cat = final[final['category'].str.contains(selected_category, case=False, na=False)]


    filtered_cat = filtered_cat.sort_values('price'  , ascending=False)

    best = filtered_cat[filtered_cat['data'] == 'Bestseller'].max()

    col1, col2, col3 , col4 , col5 = st.columns(5)
    with col1:
        st.metric("📊 Total Items in : " + selected_category, len(filtered_cat))
    with col2:
        max_price = filtered_cat['price'].max()
        st.metric("💰 Maximum Price", f"₹ {max_price:,.0f}")
    with col3:
        best_max = filtered_cat[filtered_cat['data'] == 'Bestseller']['price'].max()
        st.metric("💰 Maximum Price In Bestseller",f"₹ {best_max:,.0f}")
    with col4:
        min_price = filtered_cat['price'].min()
        st.metric("💰 Minimum Price", f"₹ {min_price:,.0f}")
    with col5:
        best_min = filtered_cat[filtered_cat['data'] == 'Bestseller']['price'].min()
        st.metric("💰 Maximum Price In Bestseller", f"₹ {best_min:,.0f}")


    st.subheader("  ")

    col1, col2, col3 , col4= st.columns(4)
    with col1:
        st.subheader(filtered_cat['title'].iloc[0])
        st.text("📈Max In " + selected_category)
        image_url = filtered_cat['image'].iloc[0]
        st.image(image_url, caption=selected_category, width=200)


    with col2:
        st.subheader(filtered_cat['title'].iloc[-1])
        st.text("📉Min In " + selected_category)
        image_url = filtered_cat['image'].iloc[-1]
        st.image(image_url, caption=selected_category, width=200)
        
    with col3:
        try:
            best = filtered_cat[filtered_cat['data'] == 'Bestseller'].iloc[0]

            st.subheader(best['title'])
            st.text("📈 Max In Bestseller")

            image_url = best['image']
            st.image(image_url, caption=selected_category, width=200)

        except IndexError:
            st.error("No item in Bestseller")

    with col4:
        try:
            best = filtered_cat[filtered_cat['data'] == 'Bestseller'].iloc[-1]

            st.subheader(best['title'])
            st.text("📉 Min In Bestseller")

            image_url = best['image']
            st.image(image_url, caption=selected_category, width=200)

        except IndexError:
            st.error("No item in Bestseller")
    st.dataframe(filtered_cat[['title', 'price', 'data' , 'image']].sort_values('price' , ascending=False))

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Category', 'Celebrity'])


def load_celebrity_analysis(selected_celebrity):
    st.title('Celebrity Analysis')
    st.subheader(selected_celebrity)
    filtered_df = df[df['celebrity'].str.contains(selected_celebrity, case=False, na=False)].sort_values(by='price', ascending=False)


    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(" ")
        st.metric("📊 Total Items by : " + selected_celebrity, len(filtered_df))
        st.metric("💰 Highest Item Price by  : " + selected_celebrity, f"₹ {filtered_df['price'].max():,.0f}")
        st.metric("💰 Lowest Item Price by : " + selected_celebrity, f"₹ {filtered_df['price'].min():,.0f}")
    with col2:
        st.subheader(filtered_df['title'].head().iloc[0])
        st.text("📈 Max Value Item")
        image_url = filtered_df['image'].iloc[0]
        st.image(image_url, caption=selected_celebrity, width=200)
    with col3:
        st.subheader(filtered_df['title'].iloc[-1])
        st.text("📉 Min Value Item ")
        image_url = filtered_df['image'].iloc[-1]
        st.image(image_url, caption=selected_celebrity, width=200)

    st.dataframe(filtered_df[['title', 'price', 'image']].head(15))

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Category':
    selected_category = st.sidebar.selectbox('Select category', sorted(set(final['category'])))
    btn1 = st.sidebar.button('Category Analysis')
    st.title('Category Wise Analysis')
    if btn1:
        load_category_analysis(selected_category)


else:
    selected_celebrity = st.sidebar.selectbox('Select Celebrity', sorted(set(df['celebrity'].str.split(',').sum())))
    btn2 = st.sidebar.button('Celebrity Analysis')
    if btn2:
        load_celebrity_analysis(selected_celebrity)
