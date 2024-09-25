import streamlit as st
import pandas as pd
import plotly.express as px
data=pd.read_csv('/workspaces/tb_details/mentornow/TB_Burden_Country.csv')
with st.expander('show more'):
    st.write(data)

df=data['Year'].unique()
s=st.sidebar.selectbox('Select Year',df)
df1=data[data['Year']==s]
with st.expander('Show More'):
    st.write(df1)
st.metric('Estimated prevalence of TB',df1['Estimated prevalence of TB (all forms) per 100 000 population'].sum())
st.metric('Estimated number of death',round(df1['Estimated number of deaths from TB (all forms, excluding HIV), high bound'].sum(),2))

st.header('Bar chart')

fig=px.bar(df1,x='Estimated prevalence of TB (all forms) per 100 000 population',y='Country or territory name')
st.write(fig)

df2=df1.sort_values(by=['Estimated prevalence of TB (all forms) per 100 000 population'], ascending=False)

st.write(df2)
top=df2.head(10)
fig2=px.bar(top,x='Estimated prevalence of TB (all forms) per 100 000 population',y='Country or territory name',text='Estimated prevalence of TB (all forms) per 100 000 population')
fig2.update_yaxes(autorange='reversed')
st.write(fig2)
