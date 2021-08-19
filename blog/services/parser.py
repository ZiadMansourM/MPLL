import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# i="<h1>fascssadsaddasdsadsa</h1> <p>sdxasdas<br /> <span class=\"marker\">SADASDAS</span></p> <div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">class code:<br /> &nbsp; &nbsp; &nbsp;def write(self):<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;pass</div>"

# print(cleanhtml("<p>testing</p>"))