# burpHTTPMirror

## 说明

**顾名思义，将burp proxy过的流量 镜像一份到指定服务器；**

*由于nginx 正向代理https流量无法解包；但是又有个流量镜像的保存的需求，参考nginx_mirror_http的想法，给burp 做了一个流量转发*

## 用法


burp 的 python 插件导入，去搜索引擎搜就好；

导入后，自动镜像流量；

镜像地址可直接修改socket 地址