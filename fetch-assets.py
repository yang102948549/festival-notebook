import urllib.request, pathlib, re
from concurrent.futures import ThreadPoolExecutor
root=pathlib.Path(__file__).parent/'dist'/'assets'
urls={
 'PretendardVariable.woff2':'https://raw.githubusercontent.com/orioncactus/pretendard/main/packages/pretendard/dist/web/variable/woff2/PretendardVariable.woff2',
 'LICENSE-Pretendard.txt':'https://raw.githubusercontent.com/orioncactus/pretendard/main/LICENSE',
 'LICENSE-Phosphor.txt':'https://raw.githubusercontent.com/phosphor-icons/core/main/LICENSE'
}
for file,url in urls.items():
 data=urllib.request.urlopen(url,timeout=30).read();(root/file).write_bytes(data);print(file,len(data))
names=['map-trifold','chat-circle-text','megaphone','note-pencil','notebook','caret-left','caret-right','question','arrow-right','hand-tap','magnifying-glass','info','users','files','map-pin','check-circle','check','lock-simple','caret-up','caret-down','arrow-up-right','x']
def get_icon(name):
 raw=urllib.request.urlopen('https://raw.githubusercontent.com/phosphor-icons/core/main/assets/regular/'+name+'.svg',timeout=30).read().decode()
 inner=re.search(r'<svg[^>]*>(.*)</svg>',raw,re.S).group(1)
 return '<symbol id="'+name+'" viewBox="0 0 256 256" fill="currentColor">'+inner+'</symbol>'
with ThreadPoolExecutor(max_workers=6) as pool:
 symbols=list(pool.map(get_icon,names))
(root/'icons.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg">'+''.join(symbols)+'</svg>',encoding='utf-8')
print('Icons',len(symbols))
