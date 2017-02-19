

from flask import Flask,render_template
import requests
#plotly is used to plot the data acquired and store it online 
import plotly.plotly as py
import plotly.graph_objs as go

import xml.dom.minidom #to parse the xml data
import plotly.plotly as py
def main():
    response = requests.get('https://data.gov.in/sites/default/files/datafile/data_aqi_cpcb.xml')

    f = open('dataxml1.xml','wb')
    f.write(requests.get('https://data.gov.in/sites/default/files/datafile/data_aqi_cpcb.xml').content)
    f.close()

    doc=xml.dom.minidom.parse("dataxml1.xml");

    state=doc.getElementsByTagName("State")


    city=doc.getElementsByTagName("City")
    for cities in city:

        if cities.getAttribute("id")=="Tirupati":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:


                pollutant=stationdata.getElementsByTagName("Pollutant")
                for pdata in pollutant:

                    if pdata.getAttribute("id")=="PM2.5":
                        pdata1=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Chennai":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="IIT":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata2=pdata.getAttribute("Avg")



        if cities.getAttribute("id")=="Hyderabad":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="Sanathnagar":
                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata3=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Delhi":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="Shadipur":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata4=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Ahmedabad":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="Maninagar":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata5=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Bengaluru":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="BTM Layout":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata6=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Mumbai":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="Bandra - MPCB":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata7=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Visakhapatnam":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="GVMC Ram Nagar-APPCB":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM2.5":
                            pdata8=pdata.getAttribute("Avg")

        if cities.getAttribute("id")=="Jaipur":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:
                print(stationdata.getAttribute("id"))
                if stationdata.getAttribute("id")=="VK Industrial Area Jaipur - RSPCB":
                    print(stationdata.getAttribute("lastupdate"))
                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:
                        print(pdata.getAttribute("id")+pdata.getAttribute("Avg"))
                        if pdata.getAttribute("id")=="PM2.5":
                            pdata9=pdata.getAttribute("Avg")
                            print(pdata9)
        if cities.getAttribute("id")=="Kolkata":
            station=cities.getElementsByTagName("Station")
            for stationdata in station:

                if stationdata.getAttribute("id")=="Victoria":

                    pollutant=stationdata.getElementsByTagName("Pollutant")
                    for pdata in pollutant:

                        if pdata.getAttribute("id")=="PM10":
                            pdata10=pdata.getAttribute("Avg")




    data = [go.Bar(
            x=['Tirupati', 'Chennai', 'Hyderabad','Delhi','Ahmedabad','Bengaluru','Mumbai','Visakhapatnam','Jaipur','Kolkata'],
            y=[pdata1, pdata2, pdata3,pdata4,pdata5,pdata6,pdata7,pdata8,pdata9,pdata10]
    )]
    layout = go.Layout(
    xaxis=dict(
        title='Major Cities',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=0,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='All'
    ),
    yaxis=dict(
        title='AQI INDEX',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=0,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='All'
    ))
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='AQI-bar',auto_open=False)



app = Flask(__name__, static_url_path = "", static_folder = "tmp")

@app.route('/')
def hello_world():
    main()
    return render_template('index.html')# On running the server calls to index.html page
  
