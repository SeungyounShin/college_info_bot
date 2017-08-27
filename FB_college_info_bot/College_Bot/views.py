import json, requests, random, re
from pprint import pprint
import apiai

from .some_methods import check_collge_name,collge_info_search
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# access token


ai = apiai.ApiAI(APIAI_ACCESS_TOKEN)

def reply_collge_profile(fbid,college_name,img_url,college_url,namu_url,adm_url):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+PAGE_ACCESS_TOKEN
    data = {
        "recipient":{"id": fbid},
        "message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[
                {
                    "title":college_name,
                    "image_url":img_url,
                    "subtitle":college_name,
                    "default_action": {
                    "type": "web_url",
                    "url": college_url,
                    "messenger_extensions": True,
                    "webview_height_ratio": "tall",
                    "fallback_url": college_url
                    },
                    "buttons":[
                    {
                        "type":"web_url",
                        "url":namu_url,
                        "title":"나무위키"
                    },{
                        "type":"web_url",
                        "url":adm_url,
                        "title":"입학처",
                    }]}]}}}
        }
    print("send data :", data)
    status = requests.post(post_message_url, json=data)
    pprint(status.json())

def reply(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

class Bot(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get('hub.verify_token') == VERIFY_TOKEN:
            print("[FB_VERIFY]successfully verified")
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            print("[FB_VERIFY]Verification Failed")
            return HttpResponse('Invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        incoming_message = json.loads(self.request.body.decode('utf-8'))
        sender = incoming_message['entry'][0]['messaging'][0]['sender']['id']
        if 'text' in incoming_message['entry'][0]['messaging'][0]['message']:
            message = incoming_message['entry'][0]['messaging'][0]['message']['text']
            print("receiving message",sender,message)

        # prepare API.ai request
            req = ai.text_request()
            req.lang = 'en'
            patt = re.compile("대학교")
            message = patt.sub("대",message)
            req.query = message

        # get response from API.ai
            api_response = req.getresponse()
            responsestr = api_response.read().decode('utf-8')
            response_obj = json.loads(responsestr)
            if 'result' in response_obj:
                response = response_obj["result"]["fulfillment"]["speech"]
                print("[API.AI received]",message,response)
                if(check_collge_name(response)):
                    lst = collge_info_search(sender,response)
                    reply_collge_profile(sender,response,lst[1],lst[3],lst[4],lst[2])
                else:
                    reply(sender, response)
        else:
            response = "no message received"
            reply(sender,response)
        return HttpResponse()

