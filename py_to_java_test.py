'''
Created on Dec 20, 2017

@author: jjh39
'''
from org.apache.http import HttpHeaders
from org.apache.http.util import EntityUtils
from org.apache.http.impl.client import HttpClients, BasicCredentialsProvider, HttpClientBuilder
from org.apache.http.auth import AuthScope, UsernamePasswordCredentials
from org.apache.http.client.methods import HttpGet, HttpUriRequest, RequestBuilder
from org.apache.http import HttpHost
from org.apache.http.client.config import RequestConfig
from org.apache.http.client.protocol import HttpClientContext
import sys
import os

def VarTest():
    print(os.environ["http_proxy"])

def RunClientTest_Auth():
    print("Running Test w/ Auth")
    try:
        credentialsProvider = BasicCredentialsProvider()
        credentialsProvider = credentialsProvider.setCredentials(AuthScope.ANY, UsernamePasswordCredentials("NORTHGRUM\J83509", "Alpha795"))
        httpClientBuilderObj = HttpClientBuilder.create()
        httpClientBuilderObj = httpClientBuilderObj.setDefaultCredentialsProvider(credentialsProvider)
        httpClient = httpClientBuilderObj.build()
        #httpClientBuilderObj.setProxy(HttpHost("contractorproxyeast.northgrum.com", 80, "http"))
        proxyHost = HttpHost("localhost", 8080)
        #httpClientBuilderObj.setProxy(HttpHost("localhost", 8080))
        myConfig = RequestConfig.custom().setProxy(proxyHost).build()
        #
        myRequest = HttpGet("http://www.cnn.com")
        myRequest.setConfig(myConfig)
        #requestBuilder.setHeader(HttpHeaders.ACCEPT_ENCODING, "RAW")
        #myRequest = requestBuilder.build()
        
        #
        myResponse = httpClient.execute(myRequest)
        print(myResponse.getStatusLine())
        print(EntityUtils.toString(myResponse.getEntity(), "UTF-8"))
        
    except Exception as ex:
        print("Oops....")
        print(ex)
    finally:
        print("Execution completed.....")



def RunClientTest():
    print("Starting httpclient test without proxy....")
    #myClient = HttpClients.createSystem()
    myClient = HttpClientBuilder.create().useSystemProperties().build()
    myProxy = HttpHost("contractorproxyeast.northgrum.com", 80)
    myConfig = RequestConfig.custom().setProxy(myProxy).build()
    requestBuilder = RequestBuilder.get("http://api.coindesk.com/v1/bpi/currentprice.json")
    requestBuilder.setHeader(HttpHeaders.ACCEPT, "application/json")
    requestBuilder.setHeader(HttpHeaders.ACCEPT_ENCODING, "raw")
    #
    myRequest = requestBuilder.build()
    myRequest.setConfig(myConfig)
    #
    myResponse = myClient.execute(myRequest)
    try:
        print(myResponse.getStatusLine())
        sys.stdout.write(EntityUtils.toString(myResponse.getEntity(), "UTF-8"))
        #print(EntityUtils.toString(myResponse.getEntity()))
        myResponse.close()
        myClient.close()
    except:
        print("Operation failed...")
