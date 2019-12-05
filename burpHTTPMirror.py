#!python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Name:   HTTPMirror
# Author: jax777

from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IResponseInfo
from burp import IRequestInfo
from burp import IHttpService
from burp import IExtensionHelpers
import socket



class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        callbacks.setExtensionName('HTTPMirror')
        callbacks.registerHttpListener(self)
        self._helpers = callbacks.getHelpers()

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            # on resp
            request = messageInfo.getRequest()
            server = messageInfo.getHttpService().toString()
            analyzedRequest = self._helpers.analyzeRequest(request)

            x_scheme_server = "X-Scheme-Server: " + server

            body = request[analyzedRequest.getBodyOffset():].tostring()
            mod_req = request[:analyzedRequest.getBodyOffset()-2].tostring() + x_scheme_server + '\r\n\r\n' + body


            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('127.0.0.1', 18080))
                s.sendall(mod_req)
                s.close()
            except:
                pass

            