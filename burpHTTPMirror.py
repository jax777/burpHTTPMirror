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
            resquest = messageInfo.getRequest()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 18080))
            s.sendall(resquest.tostring())
            s.close()

            