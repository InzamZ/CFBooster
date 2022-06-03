# coding=utf8
from __future__ import print_function
from cgitb import text
import json
from time import sleep
from unicodedata import name

from numpy import integer

# CFBooster by TLE
# Ver 0.12 (2020-01-09)
# too lazy to make gui, maybe someone can do that

# 0% deep learning
# 100% rule-based

# put your own template here!
padding = "\t"
code_template = r"""#define main fakemain
#include <bits/stdc++.h>
using namespace std;
[VARS]
#define ll long long
#define pii pair<int,int>
#define f(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define F(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
const int maxn = 5e5 + 10;
const int maxb = 110;
int T = 1, n, m, x, ans = 0, a[maxn], b[maxn];
vector<int>v;
string s;

int solve() {
    ans = 0;
    cin >> n;
    cout << n << '\n';
    return 0;
}
void main()
{
#ifdef ONLINE_JUDGE //don't mix cin/scanf, cout/printf!
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
#endif
[CODES]	
    cin >> T;
    while (T--) {
    // cout << "Case #" << T + 1 << ":" << endl;
        solve();
    }
}


#undef main
#ifndef ONLINE_JUDGE
// *INDENT-OFF*
void rmv_() {remove("in_temp");remove("out_temp");} /*edit if you want to don't want your temps removed*/ string to_str__booster__(int x) {char buf[100];sprintf(buf,"%d",x);return buf;} vector<string> clean__booster___(string u){u.push_back('\n');vector<string> w;string c;for(auto t:u){if(t=='\n'||t=='\r'){while(c.size()&&c.back()==' ') c.pop_back();if(c.size()) w.push_back(c);c.clear();}else c.push_back(t);}return w;}int to_num__booster__(string s){int w=atoi(s.c_str());char buf[10];sprintf(buf,"%d",w);if(buf==s) return w;return -1;}signed main(int argc,char**argv){if(argc==2&&(string)argv[1]=="r") {fakemain();return 0;}vector<string> code;{std::ifstream t(__FILE__);std::stringstream buffer;buffer << t.rdbuf();t.close(); code=clean__booster___(buffer.str());}int num_samples=0;map<pair<int,int>,string> samples;{string cs="";pair<int,int> id(-1,-1);for(auto s:code){if(s.substr(0,4)=="*o* "){if(id.second!=-1)samples[id]=cs;id=make_pair(-1,-1),cs="";string g=s.substr(4);string si="Sample Input ";string so="Sample Output ";if(g.back()==':'&&g.substr(0,si.size())==si){int w=to_num__booster__(g.substr(si.size(),g.size()-si.size()-1));if(w>=1) id=make_pair(w,0);}if(g.back()==':'&&g.substr(0,so.size())==so){int w=to_num__booster__(g.substr(so.size(),g.size()-so.size()-1));if(w>=1) id=make_pair(w,1);}}else cs=cs+s+"\n";}while(samples.count(make_pair(num_samples+1,0))&&samples.count(make_pair(num_samples+1,1)))++num_samples;}if(!num_samples){fakemain();return 0;}int w; int cap=1,sil=0; if(argc==2) {w=to_num__booster__(argv[1]); cerr<<w<<"... "; cap=2;} else {cerr<<num_samples<<" samples. autofeed: ";cerr.flush();string u;getline(cin,u);if(u=="a"){cerr<<"testing all samples..."<<endl;for(int i=1;i<=num_samples;++i) {cerr<<"testing sample ";int rt=system(((string)"\""+argv[0]+"\" "+to_str__booster__(i)).c_str()); if(rt) cerr<<endl<<"WA/RE (return value "<<rt<<")\n",exit(-1);}cerr<<"all samples passed!"<<endl;exit(0);}while(1){if(u.size()&&u.back()=='r')u.pop_back(),cap=0;else if(u.size()&&u.back()=='s')u.pop_back(),sil=1,cap=0;else break;}w=to_num__booster__(u);}string in,out;rmv_();if(w>=1&&w<=num_samples){in=samples[make_pair(w,0)];out=samples[make_pair(w,1)];ofstream o("in_temp");o<<in; o.close();freopen("in_temp","r",stdin);if(cap){if(cap!=2) cerr<<"============= testcase "<<w<<" (captured) ============="<<endl;freopen("out_temp","w",stdout);}else{cerr<<"================== testcase "<<w<<" ==================="<<endl;}}else{cap=0; cerr<<"=============== normal run ================"<<endl;}time_t start_time=clock(); fakemain(); time_t end_time=clock(); bool force_stop=false;if(w>=1&&w<=num_samples){string out_str;if(cap){fclose(stdout);std::ifstream t("out_temp");std::stringstream buffer;buffer << t.rdbuf();t.close();out_str=buffer.str();if(cap!=2) cerr<<out_str;}if(sil);else{if(cap!=2) cerr<<endl<<"================================================="<<endl<<"sample output:"<<endl<<out<<endl;if(cap){if(clean__booster___(out)==clean__booster___(out_str))cerr<<"compare passed ("<<int((end_time - start_time)*1000.0/CLOCKS_PER_SEC+0.5)<<"ms)!"<<endl;else {cerr<<"compare failed ("<<int((end_time - start_time)*1000.0/CLOCKS_PER_SEC+0.5)<<"ms)!"<<endl; force_stop=true; if(cap==2) {cerr<<"=============== your output ==============="<<endl<<out_str<<endl<<"============== sample output =============="<<endl<<out<<endl;}}}}}fclose(stdin);rmv_(); if(force_stop) exit(-1);}
// *INDENT-ON*
#else
signed main(){fakemain();}
#endif
"""
# If you use a proxy...


http_proxy = "http://127.0.0.1:7890"
https_proxy = "http://127.0.0.1:7890"

proxyDict = {"http": http_proxy, "https": https_proxy}

AtcoderRound = False

from bs4 import BeautifulSoup
import requests
import random
import string
import sys
import os

round = "1284"

try:
    reload(sys)
    sys.setdefaultencoding("UTF8")
except:
    pass
if len(sys.argv) >= 2:
    round = str(int(sys.argv[1]))
else:
    print("input round number: ", end="")
    try:
        input = raw_input
    except NameError:
        pass
    # round = input()

def write_file(fn, code):
    if os.path.exists(fn):
        if not query_yes_no(" " + fn + " already exists. Overwrite?", default="no"):
            print("skipped writing " + fn + ".")
            return
    print("writing to " + fn + " ... ", end="")
    f = open(fn, "w")
    f.write(code)
    f.close()
    print("succeed.")

# from https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

proCnt = 0

async def post_handler(request):
    global proCnt
    reqText = await request.text()
    reqJson = json.loads(reqText)
    p = reqJson["name"]
    p = p[:2]
    p = p.strip('.- ')
    if reqJson["group"][:8] == "CodeChef":
        p = string.ascii_uppercase[proCnt]
        proCnt += 1
    if reqJson["group"] == "NowCoder":
        p = reqJson["url"][-1:]
    if reqJson["group"] == "Luogu":
        p = reqJson["name"].split(" ")[0]
    rng_str = (
        p
        + "_"
        + "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(7)
        )
    )
    sampleList = reqJson["tests"]
    inputs = []
    outputs = []
    for test in sampleList:
        strr = test["input"]
        strr = strr.replace("\r\n", "\n")
        strr = strr.replace("\r", "\n")
        while strr[0] == "\n":
            strr = strr[1:]
        if strr[-1] != "\n":
            strr = strr + "\n"
        inputs.append(strr)
        strr = test["output"]
        strr = strr.replace("\r\n", "\n")
        strr = strr.replace("\r", "\n")
        while len(strr) > 0 and strr[0] == "\n":
            strr = strr[1:]
        if len(strr) > 0 and strr[-1] != "\n":
            strr = strr + "\n"
        outputs.append(strr)
    tail = "/*\n"
    for w in range(len(inputs)):
        tail += "*o* Sample Input " + str(w + 1) + ":\n"
        tail += inputs[w]
        tail += "*o* Sample Output " + str(w + 1) + ":\n"
        tail += outputs[w]
    tail += (
        "*o* This chunk of comment is used for auto-testing. Please don't modify.\n*/"
    )
    code1 = code_template.replace("[CODES]", "").replace("[VARS]", "") + tail
    code1 = code1.replace("in_temp", "IN_TEMP_" + rng_str).replace(
        "out_temp", "OUT_TEMP_" + rng_str
    )
    write_file(p + ".cpp", code1)
    # web.stop()


from aiohttp import JsonPayload, web

app = web.Application()
app.add_routes([web.post("/", post_handler)])


if round.find("abc") != -1 or round.find("arc") != -1 or round.find("agc") != -1:
    web.run_app(app, host="0.0.0.0", port=10043)
    exit()

web.run_app(app, host="localhost", port=10043)
print("all done.")
