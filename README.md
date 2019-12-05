# burpHTTPMirror

## 说明

**顾名思义，将burp proxy过的流量 镜像一份到指定服务器；**

*由于nginx 正向代理https流量无法解包；但是又有个流量镜像的保存的需求，参考nginx_mirror_http的想法，给burp 做了一个流量转发*

## 用法


burp 的 python 插件导入，去搜索引擎搜就好；

导入后，自动镜像流量；

镜像地址可直接修改socket 地址

镜像后 增加 http 头 x-scheme-serve,记录原始请求地址 

http 包体实例
```
GET /images/spinners/octocat-spinner-128.gif HTTP/1.1
Host: github.githubassets.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: image/webp,*/*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://github.com/jax777
If-Modified-Since: Wed, 12 Dec 2018 18:17:07 GMT
Cache-Control: max-age=0
X-Scheme-Server: https://github.githubassets.com
```