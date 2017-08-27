import requests
college_list = {
    "건국대":[
        "konkuk",
        'https://ko.wikipedia.org/wiki/건국대학교#/media/File:Konkuk_University_logotype.png',
        "http://enter.konkuk.ac.kr/seoul/susi/detailGuide.jsp"
    ],
    "이화여대":[
        "ewha",
        'https://ko.wikipedia.org/wiki/이화여자대학교#/media/File:이화여자대학교_로고.png',
        "https://admission.ewha.ac.kr/enter/doc/intro.asp"
    ],
    "경희대":[
        "kyunghee",
        'https://ko.wikipedia.org/wiki/경희대학교#/media/File:Kyung_Hee_University_Logo.png',
        "http://iphak.khu.ac.kr/main.do"
    ],
    "고려대":[
        "korea",
        'https://ko.wikipedia.org/wiki/고려대학교#/media/File:고려대학교.png',
        "http://oku.korea.ac.kr/oku/index.jsp"
    ],
    "동국대":[
        "dongguk",
        'https://ko.wikipedia.org/wiki/동국대학교#/media/File:Dongguk_University.png',
        "https://ipsi.dongguk.edu/MnMain.do;jsessionid=D05CEC520A9C409E46CFA0F0D3F1C14C"
    ],
    "서울대":[
        "snu",
        'https://ko.wikipedia.org/wiki/서울대학교#/media/File:서울대학교_로고.png',
        "http://admission.snu.ac.kr/index.html"
    ],
    "서울시립대":[
        "uos",
        'https://ko.wikipedia.org/wiki/서울시립대학교#/media/File:서울시립대학교_로고.png',
        "http://admission.uos.ac.kr/admission/main.do"
    ],
    "성균관대":[
        "uos",
        'https://www.timeshighereducation.com/sites/default/files/styles/institution_logo_320x320/public/sungkyunkwan-university-skku-_logo.png',
        "https://admission.skku.edu"
    ],
    "연세대":[
        "yonsei",
        'https://ko.wikipedia.org/wiki/연세대학교#/media/File:연세대학교.png',
        "http://www.yonsei.ac.kr/sc/admission/admission.jsp"
    ],
    "중앙대":[
        "cau",
        'https://ko.wikipedia.org/wiki/중앙대학교#/media/File:Chung-Ang_University_logo.png',
        "http://admission.cau.ac.kr/intro/intro.html"
    ],
    "한국외대":[
        "hufs",
        'https://ko.wikipedia.org/wiki/한국외국어대학교#/media/File:한국외국어대학교_로고.png',
        "https://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=42977&siteId=hufs&menuType=T&uId=1&sortChar=ACAF&menuFrame=left&linkUrl=01_020111.html&mainFrame=right"
    ],
    "한양대":[
        "hanyang",
        'https://ko.wikipedia.org/wiki/한양대학교#/media/File:한양대학교.png',
        "http://iphak.hanyang.ac.kr/new/2017/intro/"
    ]}

#reply_collge_profile(fbid,collge_name,img_url,college_url,namu_url,adm_url)

def check_collge_name(college_name):
    for i in college_list:
        if(college_name == i):
            return True
    return False

def college_info_search(fbid,college_name):
    lst= college_list[college_name]
    lst.append("https://www."+lst[0]+".ac.kr/")
    lst[0] = college_name
    lst.append("https://namu.wiki/w/"+college_name+"학교"+"?from="+college_name)
    return lst

ACCESS_TOKEN = "EAAQrUsMFNsQBAO23KZCUW8jqrp6iXh5lDqf76cjISfZAwWmMWFtBNwHI0qIGIplpNkhUK3IOXDaDZB8ubvuwBVevXtBZA9zTsZBcZBn4icd6WmQwZADWABY6mQmjQTCOu0aqB6G7nTwX3aK70mXegzCcWa50hOqVoKkZBXFZAnZAO1UnTiEZBYj7a8V"

def FB_whitelisted(url1,url2,url3,url4):
    data = {
        "setting_type": "domain_whitelisting",
        "whitelisted_domains":[url1,url2,url3,url4],
        "domain_action_type": "add"
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

for j in college_list:
    lst = college_info_search('shin',j)
    FB_whitelisted(lst[1],lst[2],lst[3],lst[4])
    print(lst[0]+"successfully added\n")

rq = requests.post("https://graph.facebook.com/v2.6/me/messenger_profile?fields=whitelisted_domains&access_token="+ACCESS_TOKEN)

print("-----------------\n")
print(rq)
