import html
import lxml.html
import requests
import os

os.system('clear')
QUERY_1='//div/div[@class="position-relative"]/div[@class="d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted"]/div[@class="d-table-cell col-9 v-align-top pr-3"]/a[@class="d-inline-block no-underline mb-1"]/span[@class="Link--secondary"]/text()'

QUERY_2='//div/div[@class="position-relative"]/div[@class="d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted"]/div[@class="d-table-cell col-9 v-align-top pr-3"]/a[@class="d-inline-block no-underline mb-1"]/span[@class="Link--secondary pl-1"]/text()'

GITHUB_ACC='josbyb2020'
LINK='https://github.com/'+GITHUB_ACC+'?tab=followers'
all_accounts={}
page_count=2

def result_length(result):
    return len(result)>0

def get_followers(link):
    html_content=requests.get(link).content
    doc=lxml.html.fromstring(html_content)
    result_1=doc.xpath(QUERY_1)
    result_2=doc.xpath(QUERY_2)
    return result_1, result_2, set(result_1) | set(result_2)

all_accounts=get_followers(LINK)[2]
if(len(all_accounts)>=50):
    LINK='https://github.com/'+GITHUB_ACC+'?page='+str(page_count)+'&tab=followers'
    all_accounts_temp=get_followers(LINK)[2]
    all_accounts=all_accounts | all_accounts_temp
    while(result_length(get_followers(LINK)[0]) or result_length(get_followers(LINK)[1])):
        page_count+=1
        LINK='https://github.com/'+GITHUB_ACC+'?page='+str(page_count)+'&tab=followers'
        all_accounts_temp=get_followers(LINK)[2]
        all_accounts=all_accounts | all_accounts_temp

print('\nAccount : ', GITHUB_ACC)
print('Number of followers : ', len(all_accounts))
print('Followers : ', all_accounts,'\n')