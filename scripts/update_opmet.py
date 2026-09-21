import urllib.request,gzip,xml.etree.ElementTree as ET,json,datetime,pathlib
UA={"User-Agent":"HELI-FPL/0.17 educational flight-planning project"}
BASE="https://aviationweather.gov/data/cache/"
def get(name):
 r=urllib.request.Request(BASE+name,headers=UA)
 return gzip.decompress(urllib.request.urlopen(r,timeout=30).read())
def txt(e,n):
 x=e.find(n); return x.text.strip() if x is not None and x.text else None
def num(x):
 try:return float(x)
 except:return None
stations={}
root=ET.fromstring(get("metars.cache.xml.gz"))
for m in root.findall(".//METAR"):
 sid=txt(m,"station_id")
 if not sid or not sid.startswith("L"): continue
 lat,lon=num(txt(m,"latitude")),num(txt(m,"longitude"))
 if lat is None or lon is None: continue
 vis=num(txt(m,"visibility_statute_mi")); vism=None if vis is None else round(vis*1609.344)
 ceil=None
 for sk in m.findall(".//sky_condition"):
  cov=sk.attrib.get("sky_cover",""); base=num(sk.attrib.get("cloud_base_ft_agl"))
  if cov in ("BKN","OVC","VV") and base is not None: ceil=base if ceil is None else min(ceil,base)
 wx=txt(m,"wx_string")
 stations[sid]={"id":sid,"lat":lat,"lon":lon,"metar":{"raw":txt(m,"raw_text"),"obs_time":txt(m,"observation_time"),"visibility_m":vism,"ceiling_ft":ceil,"wx":wx},"taf":None}
root=ET.fromstring(get("tafs.cache.xml.gz"))
for t in root.findall(".//TAF"):
 sid=txt(t,"station_id")
 if sid in stations:
  stations[sid]["taf"]={"raw":txt(t,"raw_text"),"issue_time":txt(t,"issue_time"),"valid_from":txt(t,"valid_time_from"),"valid_to":txt(t,"valid_time_to")}
out={"generated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source":"NOAA/NWS Aviation Weather Center Data API cache","stations":list(stations.values())}
pathlib.Path("weather").mkdir(exist_ok=True)
pathlib.Path("weather/italy_opmet.json").write_text(json.dumps(out,separators=(",",":")),encoding="utf-8")
print("stations",len(stations))
