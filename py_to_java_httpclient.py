'''
Created on Dec 20, 2017

@author: jjh39
'''
import sys
from org.apache import http
from java.io import InputStream, InputStreamReader
#from java.io import InputStreamReader
from java.nio import charset



from org.apache.http.impl.client import BasicCredentialsProvider, CloseableHttpClient, HttpClients, HttpClientBuilder
from org.apache.http.auth import AuthScope, UsernamePasswordCredentials



def RunClientTest():
    print("Starting httpclient test w/ proxy....")
    myClient = http.impl.client.HttpClients.createDefault()
    myTarget = http.HttpHost("google.com", 80, "http")
    myProxy = http.HttpHost("localhost", 8080, "http")
    #myProxy = http.HttpHost("contractorproxyeast.northgrum.com", 80, "http")
    #http.client.config.RequestConfig.proxy()
    myConfig = http.client.config.RequestConfig.custom().setProxy(myProxy).build()
    myRequest = http.client.methods.HttpGet("/")
    myRequest.setConfig(myConfig)
    try:
        #myCharSet = charset.StandardCharsets.UTF_8
        myResponse = myClient.execute(myTarget, myRequest)
        print("........Response data........")
        responseContent = myResponse.getEntity().getContent()
        inputStreamReader = InputStreamReader(responseContent, charset.StandardCharsets.UTF_8)
        responseText = ""
        responseChar = inputStreamReader.read()
        while(responseChar != -1):
            responseText = responseText + str(responseChar)
            responseChar = inputStreamReader.read()
        print(responseText)
        #myReader = InputStream(myResponse.getEntity().getContent())
        #myEntity = myResponse.getEntity().getContent()
        #responseText = http.util.EntityUtils.toString(myEntity)
        #print(myReader)
        print("........End Response data........")
        #print(myResponse.getStatusLine())
    except Exception as ex:
        print("Operation failed...")
        print(ex)
    finally:
        try:
            myResponse.close()
            myClient.close()
        except:
            print("Error closing resources.")
            
def RunClientProxyTest():
    myHttpClient = None
    myResponse = None
    try:
        
        print("Trying Request w/ Proxy Authentication")
        tempHttpClient = HttpClientBuilder.useSystemProperties().build()
        tempHttpClient.execute()
        #tempHttpClientBuilder = tempHttpClientBuilder.useSystemProperties()
        #tempHttpClient = tempHttpClientBuilder.build()
        #
        
        
        myHttpClient = http.impl.client.HttpClientBuilder.create().build()
        myTarget = http.HttpHost("localhost", 8080, "http")
        
        credsProvider = http.auth.NTCredentials()
        credsProvider.setCredentials(AuthScope(myTarget.getHostName(), myTarget.getPort()), UsernamePasswordCredentials("J83509", "Alpha795"))
        #myHttpClient = HttpClients.custom().setDefaultCredentialsProvider(credsProvider).build()
        myProxy = http.HttpHost("localhost", 8080, "http")
        #myProxy = http.HttpHost("contractorproxyeast.northgrum.com", 80, "http")
        #http.client.config.RequestConfig.proxy()
        myConfig = http.client.config.RequestConfig.custom().setProxy(myProxy).build()
        myHttpGet = http.client.methods.HttpGet("www.google.com")
        myHttpGet.setConfig(myConfig)
        #Run and get response
        #httpclient.
        myResponse = myHttpClient.execute(myTarget, myHttpGet)
        print(myResponse.getStatusLine())
        print("Test succeeded...")
    except Exception as ex:
        print("Operation failed...")
        print(ex)
    finally:
        if myHttpClient is not None: myHttpClient.close()
        if myResponse is not None: myResponse.close()
    
    