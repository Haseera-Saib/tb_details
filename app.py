import streamlit as st
import pandas as pd
import plotly.express as px
data=pd.read_csv('/workspaces/tb_details/mentornow/TB_Burden_Country.csv')
#with st.expander('show more'):
#    st.write(data)

st.header('TB BURDEN COUNTRY DETAILS')
df=data['Year'].unique()
s=st.sidebar.selectbox('Select Year',df)
df1=data[data['Year']==s]
#with st.expander('Show More'):
#    st.write(df1)
cl1,cl2=st.sidebar.columns(2)

cl1.metric('Estimated prevalence of TB',df1['Estimated prevalence of TB (all forms) per 100 000 population'].sum())
cl2.metric('Estimated number of death',round(df1['Estimated number of deaths from TB (all forms, excluding HIV), high bound'].sum(),2))

#st.header('Bar chart')

#fig=px.bar(df1,x='Estimated prevalence of TB (all forms) per 100 000 population',y='Country or territory name')
#st.write(fig)

df2=df1.sort_values(by=['Estimated prevalence of TB (all forms) per 100 000 population'], ascending=False)
#with st.expander('Show more'):
#    st.write(df2)
st.subheader('Estimated prevalence of TB by Country')
top=df2.head(10)
fig2=px.bar(top,x='Estimated prevalence of TB (all forms) per 100 000 population',y='Country or territory name',text='Estimated prevalence of TB (all forms) per 100 000 population')
fig2.update_yaxes(autorange='reversed')
st.write(fig2)

st.subheader('World Map Of Estimated prevalance of TB')
fig3 = px.choropleth(df2,color="Estimated prevalence of TB (all forms) per 100 000 population",
                    locations="ISO 3-character country/territory code", 
                    projection="mercator"
                   )

st.write(fig3)
df3=df2['Country or territory name'].unique()
ss=st.sidebar.selectbox('Select Country',df3)
df3=data[data['Country or territory name']==ss]
#with st.expander('show more'):
#    st.write(df3)
c1,c2=st.sidebar.columns(2)

c1.metric('Total Number of Positive Case',df3['Estimated prevalence of TB (all forms) per 100 000 population'].sum())
c2.metric('Total Number of deaths',round(df3['Estimated number of deaths from TB (all forms, excluding HIV), high bound'].sum(),2))


st.subheader('Changes of Estimated prevalence of Tb in countries')
nd=data[data['Country or territory name']==ss]
#st.write(nd)
fig4=px.bar(nd,y='Estimated prevalence of TB (all forms) per 100 000 population',x='Year')
st.write(fig4)
