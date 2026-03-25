---
name: cve_navi
description: 具体版本的 geoserver 可能的漏洞
---
## geoserver : < 2.22.6, < 2.23.6, < 2.24.4, < 2.25.2
  - CVE-2024-36401：GeoServer 在 2.22.6、2.23.6、2.24.4 和 2.25.2 之前的版本存在远程代码执行漏洞。未经身份验证的攻击者可通过多个 OGC 请求参数（WFS GetFeature、WFS GetPropertyValue、WMS GetMap、WMS GetFeatureInfo、WMS GetLegendGraphic 和 WPS Execute）利用此漏洞执行任意代码。详见 data/skills/ours/pocs/geoserver/cve_2024_36401.md