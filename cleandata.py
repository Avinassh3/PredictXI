import pandas as pd
def clean():

    a=pd.read_csv('t20data.csv')
    a['Average']=a['Average'].str.replace('-','0')
    a['StrikeRate']=a['StrikeRate'].str.replace('-','0')
    a['Truns']=a['Truns'].str.replace('-','0')
    a['score'] = 3.5 * pd.to_numeric(a['Average']) + 6.5 * pd.to_numeric(a['StrikeRate'])
    a.to_csv('t20data.csv',index=True)

    b=pd.read_csv('odidata.csv')
    b['Average']=b['Average'].str.replace('-','0')
    b['StrikeRate']=b['StrikeRate'].str.replace('-','0')
    b['Truns']=b['Truns'].str.replace('-','0')
    b['score'] = 6.5 * pd.to_numeric(b['Average']) + 3.5 * pd.to_numeric(b['StrikeRate'])
    b.to_csv('odidata.csv',index=True)

    a2=pd.read_csv('odibowldata.csv')
    a2['Average']=a2['Average'].str.replace('-','0')
    a2['Strikerate']=a2['Strikerate'].str.replace('-','0')
    a2['Economy']=a2['Economy'].str.replace('-','0')
    a2['Wickets']=a2['Wickets'].str.replace('-','0')
    a2['score'] = pd.to_numeric(a2['Economy']) + pd.to_numeric(a2['Strikerate'])
    a2.to_csv('odibowldata.csv',index=True)

    b2=pd.read_csv('testbowling.csv')
    b2['Average']=b2['Average'].str.replace('-','0')
    b2['Strikerate']=b2['Strikerate'].str.replace('-','0')
    b2['Economy']=b2['Economy'].str.replace('-','0')
    b2['Wickets']=b2['Wickets'].str.replace('-','0')
    b2['score'] = pd.to_numeric(b2['Average'])-(pd.to_numeric(b2['Wickets'])/10)
    b2.to_csv('testbowling.csv',index=True)

    c2=pd.read_csv('t20bowling.csv')
    c2['Average']=c2['Average'].str.replace('-','0')
    c2['Strikerate']=c2['Strikerate'].str.replace('-','0')
    c2['Economy']=c2['Economy'].str.replace('-','0')
    c2['Wickets']=c2['Wickets'].str.replace('-','0')
    c2['score'] = 7 * pd.to_numeric(c2['Economy']) + 3 * pd.to_numeric(c2['Strikerate'])
    c2.to_csv('t20bowling.csv',index=True)

    c = pd.read_csv('testdata.csv')
    c['Average'] = c['Average'].str.replace('-', '0')
    c['StrikeRate'] = c['StrikeRate'].str.replace('-', '0')
    c['Truns'] = c['Truns'].str.replace('-', '0')
	
    c['score'] = pd.to_numeric(c['Average'])+(pd.to_numeric(c['Truns'])/10)
    c.to_csv('testdata.csv', index=True)

