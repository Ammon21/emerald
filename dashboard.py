import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import plotly.graph_objects as go



st.set_page_config(
    page_title="Data Visualization Project",
    page_icon='logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <link rel="stylesheet" type="text/css" href="style.css">
    """,
    unsafe_allow_html=True
)



st.image('amon.jpg')



pf = pd.read_csv('plotlyx.csv')
gf = pd.read_csv('3d.csv')
df = pd.read_csv('hsmsx.csv')


df.gender = df.gender.replace('f', 'Female')
df.gender = df.gender.replace('m', 'Male')
df.birth_order = df.birth_order.replace('first child', 'First Child')
df.birth_order = df.birth_order.replace('middle child', 'Middle Child')
df.birth_order = df.birth_order.replace('last child', 'Last Child')
df.conduct = df.conduct.replace('a', 'A')
df.conduct = df.conduct.replace('b', 'B')
df.conduct = df.conduct.replace('c', 'C')
df.admission = df.admission.replace('paid', 'Paid')
df.admission = df.admission.replace('scholarship', 'Scholarship')
df.pob = df.pob.replace('ethiopia', 'Ethiopia')
df.pob = df.pob.replace('foriegn_soil', 'Foriegn Soil')
df.transport_type = df.transport_type.replace('private', 'Private')
df.transport_type = df.transport_type.replace('public', 'Public')
df.transport_type = df.transport_type.replace('service', 'Service')
df.transport_type = df.transport_type.replace('on foot', 'On Foot')
df.transport_type = df.transport_type.replace('foot', 'On Foot')
df.level = df.level.replace('middleschool', 'Middle School')
df.level = df.level.replace('highschool', 'High School')

df.rename(columns={"chemistry": "Chemistry"}, inplace=True)
df.rename(columns={"physics": "Physics"}, inplace=True)
df.rename(columns={"maths": "Math"}, inplace=True)
df.rename(columns={"biology": "Biology"}, inplace=True)
df.rename(columns={"geography": "Geography"}, inplace=True)
df.rename(columns={"history": "History"}, inplace=True)
df.rename(columns={"civics": "Civics"}, inplace=True)
df.rename(columns={"ict": "ICT"}, inplace=True)
df.rename(columns={"civics": "Civics"}, inplace=True)
df.rename(columns={"amharic": "Amharic"}, inplace=True)
df.rename(columns={"gpa": "GPA"}, inplace=True)
df.rename(columns={"english": "English"}, inplace=True)


st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 22px;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(13, 71, 161, 0.08);
   border: 1px solid rgba(13, 71, 161, 0.09);
   padding: 2% 2% 2% 15%;
   border-radius: 5px;
   border-left-color: #008000;
   border-left-style: solid;
   border-left-width: medium;
   color: rgb(0, 139, 0);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: black;
}
</style>
"""
, unsafe_allow_html=True)

st.markdown("---")

colz, colx, coly, cola, colb = st.columns(5)

with colz:
    st.metric(label="Total Students", value=287, delta='schoolwide', delta_color="normal")
with colx:
    st.metric(label="Male Students", value=138, delta='schoolwide', delta_color="normal")
with coly:
    st.metric("Female Students", "149", delta = "schoolwide", delta_color="normal")
with cola:
    st.metric("Scholarship Students", "92", delta = "schoolwide", delta_color="normal")
with colb:
    st.metric("Paying Students", "195", delta = "schoolwide", delta_color="normal")     

st.markdown("---")

st.markdown("#")


gf['lat']=pd.to_numeric(gf['lat']) 
gf['lon']=pd.to_numeric(gf['lon'])

col6,col7 = st.columns(2)


#st.subheader("Data")
#st.write(df.head())

df.transport_type = df.transport_type.replace('foot', 'on foot')

options = ['Admission','Gender', 'Conduct', 'Birth Order', 'Birth Place', 'Transport Type', 'Guardian']

 
with col6:
    selectedx = st.selectbox('Which feature should we plot?', options)

    if selectedx == 'Birth Order' or selectedx == 'Transport Type':
        selectedx = selectedx.lower()
        selectedx = selectedx.replace(' ', '_')
    elif selectedx == 'Birth Place':
    	selectedx = 'pob'    
    else:
        selectedx = selectedx.lower()  

    col1, col2 = st.columns(2)
    global dfg 
    

    with col1:
        typex = ['All', 'Paid', 'Scholarship']
        typey = st.radio("Filters", typex)
         

    if (typey != 'All'):
        dfg = df[df['admission'] == typey]
    else:
        dfg = df[df['grade'] > 0]
      

    with col2:
        levelx = ['All', 'Middle School', 'High School']
        levely = st.radio("Filters", levelx)
        
        
        if (levely != 'All'):
            dfg = dfg[dfg['level'] == levely]
        else:
            dfg = dfg[dfg['age'] != 0]        



    def donut(titlex, con):
    
        fig4 = px.pie(dfg[con], hole = 0.4,
                names = dfg[con], color = dfg[con],
                title = titlex.upper(),width=550, height=420,
                color_discrete_map = {'ethiopia':'#C0C0C0', 
                                        'foriegn_soil': '#FFD700',
                                        'Male' : '#189AB4', 'Female' : '#FFABAB',
                                        'c' : '#0E86D4','a' : '#003060', 'b' : '#055C9D',
                                        'Middle Child': '#189AB4', 'First Child' : '#FFD700',
                                        'Last Child': '#C0C0C0', 'service': '#189AB4', 'Private' : '#FFD700',
                                        'Public': '#055C9D', 'On Foot' : '#C0C0C0', 'mother': '#FFD700',
                                        'father': '#189AB4', 'both': '#0000FF', 'other': '#C0C0C0'
                                                
                })
        fig4.update_traces(title_font = dict(size=25,family='Verdana', 
                    color='darkred'),
                    hoverinfo="label+percent+name",
                    hoverlabel=dict(bgcolor="#444", font_size=13, font_family="Lato, sans-serif"),
                    textinfo='percent', textfont_size=20)          
     
        return fig4

    
    st.write(donut(selectedx, selectedx))
   

with col7:
    st.image('cover.png', width=400)
    st.markdown('#')
    st.markdown('#')
    st.subheader('Origin: Previous Schools')
    st.image('ps.png', caption = 'Previous Schools')

st.subheader('Analysis By Grade level')

colx, coly = st.columns(2)

with colx:
     #tobemoved #donefixed
    subjectx = st.selectbox('which type should we plot?', ['Level', 'Admission', 'Gender'])
    fig = px.histogram(df, x="grade", color=subjectx.lower(), barmode='group', height=380,width=600,
                        color_discrete_map={
                'Male' : '#189AB4', 'Female' : '#FFABAB', 'Paid' : '#c5c5c5', 'Scholarship':'deepskyblue', 'Middle School': '#5C5CFF',
                'High School': '#68BBE3'
        },)
    
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor='rgba(0, 0, 0, 0)', bargap=0.3)

    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [5,6,7,8,9,10,11,12],
            ticktext = ['Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12']
        ))

    st.write(fig)
    st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 4rem;
    }
    </style>
    """,unsafe_allow_html=True)



def ban():
    categories = ['Biology','Chemistry','Physics',
                'Geography', 'History','English','Math']


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[82.6, 83.7, 81.3, 81, 83.7,89.1,77.8],
        theta=categories,
        fill='toself',
        name='Paid'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[89, 90, 85, 89.4, 88,89.6,86],
        theta=categories,
        fill='toself',
        name='Scholarship'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[50, 100]
        )),
    showlegend=False
    )

    return fig

def van():
    categories = ['Biology','Chemistry','Physics',
                'Geography', 'History','English','Math']


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[86, 87.1, 83.1, 84, 86.4, 89.5,81.2],
        theta=categories,
        fill='none',
        name='Authoritative',
        fillcolor='red'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[82.8, 84, 82.6, 82, 82, 89.8,79.1],
        theta=categories,
        fill='toself',
        name='Authoritarian'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[50, 100]
        )),
    showlegend=False
    )

    return fig



def tan():
    categories = [ 'English', 'Amharic', 'Math', 'ICT', 'Physics']


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[89.64, 78.53, 75.2, 85.9, 76.7],
        theta=categories,
        fill='toself',
        name='Foreign lang'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[89, 90.7, 81.4, 88.5, 83.8],
        theta=categories,
        fill='toself',
        name='Ethiopian lang'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[50, 100]
        )),
    showlegend=False
    )

    return fig

pagesx = {
    "Scholarship Students vs Paid Students": ban,
    "Foriegn Language vs Ethiopian Language": tan
}

	

with coly:
    #new free spot
    selectedx = st.selectbox("Choose Pages", pagesx.keys())
    st.write(pagesx[selectedx]())
    #with st.expander("See explanation"):
        #st.markdown("#### Scholarship dominated on all major subjects, even in English by tiny margin.")
        #st.image('exp.png')
    
    
col3, col4 = st.columns(2)

with col3:
    optionsx = ['GPA', 'English', 'Amharic', 'ICT', 'Math', 'Chemistry', 'Biology', 'Physics', 'Geography', 'History','Civics']


    subjectx = st.selectbox('Which subject should we plot?', optionsx)
        
    v = df.groupby('grade')[subjectx].mean()
    xx = pd.DataFrame(v.index.to_list() , columns=['grade'])
    xx['gpa'] = v.values
    xxx = xx[xx['grade'] > 6]
    xxx['gpa'] = xxx.gpa.apply(lambda x: round(x, 1))


    figz = px.scatter(xxx, x="grade", y="gpa",
                 size="grade", width=600, height=440, color="gpa",color_continuous_scale='Bluered_r')

    figz.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0, 0, 0, 0)")

    st.write(figz)
        

with col4:
    fig4 = px.histogram(pf, y="mean", x="subject",
             color='batch', barmode='group',color_discrete_map={
             2022: '#C5C5C5',
             2023: '#145DA0'
    },
             height=350, width = 600)

    #fig.update_traces(marker_color=['red','green', 'blue'])
    fig4.update_layout(plot_bgcolor="rgba(0,0,0,0)", bargap=0.4, yaxis_range=[50,100])

    st.markdown('#### 2023 Vs 2022 Batch Academic Performance')
    st.write(fig4)
    with st.expander("See explanation"):
        st.markdown(" #### Previous batches have dominated on all matric subjects except Chemistry. This shows that current students are underperforming. Overall Gpa of students have decreased.")
        st.image('srx.png')


def wordcloud():
    st.image('b.png', caption='Location')
    
def gps():
    st.map(gf)
    
def cmap():
    st.image('map.png', caption='covered area')    
    
def tresdx():
    st.pydeck_chart(pdk.Deck(
    map_style= None,
    initial_view_state=pdk.ViewState(
        latitude=9.005401,
        longitude=38.763611,
        zoom=10.5,
        min_zoom=8,
        max_zoom=12,
        pitch=60,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=gf,
           get_position='[lon, lat]',
           auto_highlight=True,
           radius=300,
           elevation_scale=10,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
           opacity=0.2,
           coverage=1
    ),
        pdk.Layer(
            'ScatterplotLayer',
            data=gf,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=50,
    ),
    ],
    ))    
        
#Location
pages = {
    "2d Vizualization": gps,
    "3d Vizualization": tresdx,
    "Word Cloud": wordcloud,
    "Covered Area": cmap
}

col8, col9 = st.columns(2)



with col8:
    st.subheader('2022 vs 2023 Senior Batch')
    batch_option = pf['batch'].unique().tolist()

    st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

    batch = st.selectbox('which batch should we plot?', batch_option)

    pfx = pf[pf['batch'] == batch]

    fig3 = px.bar(pfx, x="mean", y="subject", orientation='h', height=350, width=350)

    fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis_range=[50,100], yaxis = {"categoryorder":"total ascending"})

    fig3.update_traces(marker_color='#2E8BC0')
    st.write(fig3)

   


#zzzz
with col9:
    st.subheader('Location')
    selected = st.selectbox("Choose Pages", pages.keys())
    pages[selected]()
    

mainx = df.groupby('birth_order')[['Math', 'Physics', 'Chemistry','Biology']].mean()
fig1 = px.imshow(mainx, text_auto=True, width= 600)
st.write(fig1)

st.markdown("<h6 style='text-align: center; color: #A9A9A9;'>Designed by Graduate Students @ Emerald | 2023 </h6>", unsafe_allow_html=True)
   

