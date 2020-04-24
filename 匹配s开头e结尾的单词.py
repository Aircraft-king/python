import re
text ='site sea sue sweet see case sse ssee loses'
result = re.findall(r'\bs\S*?e\b',text)
print(result)
