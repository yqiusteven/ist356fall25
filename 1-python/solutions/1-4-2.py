'''
Let's make the code in 1-4-1 more resusable 

re-write the date parse into a function `parsedate_mdy(text: str) -> datetime:`   
re-write the date format into a function `formatdate_ymd(date: datetime) -> str:`  
re-write the main program to use both functions. input -> parsedate -> formatdate -> output


'''

import datetime

def parsedate_mdy(text):
    return datetime.datetime.strptime(text, "%m/%d/%Y")


def formatdate_ymd(date: datetime) -> str:
    return datetime.datetime.strftime("%A, %B %d %Y")


# main Code
date = 12/30/2000
date_dt = parsedate_mdy(date)
date_str = formatdate_ymd(date_dt)
print(date_str) #2000-12-30
