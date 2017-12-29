'''
Created on Dec 20, 2017

@author: jjh39
'''
from org.apache.http import *


def RunClientTest():
    print("Starting httpclient test w/ proxy....")
    myClient = impl.client.HttpClients.createDefault()
    myTarget = HttpHost("google.com", 80, "http")
    myProxy = HttpHost("contractorproxyeast.northgrum.com", 80, "http")
    myConfig = client.config.RequestConfig.custom().setProxy(myProxy).build()
    myRequest = client.methods.HttpGet("/")
    myRequest.setConfig(myConfig)
    myResponse = myClient.execute(myTarget, myRequest)
    try:
        print(myResponse.getStatusLine())
    except:
        print("Operation failed...")
