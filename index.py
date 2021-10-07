from flask import Flask, jsonify, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator(service_urls = [
                        'translate.google.ac', 'translate.google.ad', 'translate.google.ae',
                        'translate.google.al', 'translate.google.am', 'translate.google.as',
                        'translate.google.at', 'translate.google.az', 'translate.google.ba',
                        'translate.google.be', 'translate.google.bf', 'translate.google.bg',
                        'translate.google.bi', 'translate.google.bj', 'translate.google.bs',
                        'translate.google.bt', 'translate.google.by', 'translate.google.ca',
                        'translate.google.cat', 'translate.google.cc', 'translate.google.cd',
                        'translate.google.cf', 'translate.google.cg', 'translate.google.ch',
                        'translate.google.ci', 'translate.google.cl', 'translate.google.cm',
                        'translate.google.cn', 'translate.google.co.ao', 'translate.google.co.bw',
                        'translate.google.co.ck', 'translate.google.co.cr', 'translate.google.co.id',
                        'translate.google.co.il', 'translate.google.co.in', 'translate.google.co.jp',
                        'translate.google.co.ke', 'translate.google.co.kr', 'translate.google.co.ls',
                        'translate.google.co.ma', 'translate.google.co.mz', 'translate.google.co.nz',
                        'translate.google.co.th', 'translate.google.co.tz', 'translate.google.co.ug',
                        'translate.google.co.uk', 'translate.google.co.uz', 'translate.google.co.ve',
                        'translate.google.co.vi', 'translate.google.co.za', 'translate.google.co.zm',
                        'translate.google.co.zw', 'translate.google.com.af', 'translate.google.com.ag',
                        'translate.google.com.ai', 'translate.google.com.ar', 'translate.google.com.au',
                        'translate.google.com.bd', 'translate.google.com.bh', 'translate.google.com.bn',
                        'translate.google.com.bo', 'translate.google.com.br', 'translate.google.com.bz',
                        'translate.google.com.co', 'translate.google.com.cu', 'translate.google.com.cy', 
                        'translate.google.com.do', 'translate.google.com.ec', 'translate.google.com.eg', 
                        'translate.google.com.et', 'translate.google.com.fj', 'translate.google.com.gh', 
                        'translate.google.com.gi', 'translate.google.com.gt', 'translate.google.com.hk', 
                        'translate.google.com.jm', 'translate.google.com.kh', 'translate.google.com.kw', 
                        'translate.google.com.lb', 'translate.google.com.ly', 'translate.google.com.mm', 
                        'translate.google.com.mt', 'translate.google.com.mx', 'translate.google.com.my', 
                        'translate.google.com.na', 'translate.google.com.ng', 'translate.google.com.ni', 
                        'translate.google.com.np', 'translate.google.com.om', 'translate.google.com.pa', 
                        'translate.google.com.pe', 'translate.google.com.pg', 'translate.google.com.ph', 
                        'translate.google.com.pk', 'translate.google.com.pr', 'translate.google.com.py', 
                        'translate.google.com.qa', 'translate.google.com.sa', 'translate.google.com.sb', 
                        'translate.google.com.sg', 'translate.google.com.sl', 'translate.google.com.sv', 
                        'translate.google.com.tj', 'translate.google.com.tr', 'translate.google.com.tw', 
                        'translate.google.com.ua', 'translate.google.com.uy', 'translate.google.com.vc', 
                        'translate.google.com.vn', 'translate.google.com', 'translate.google.cv',
                        'translate.google.cz', 'translate.google.de', 'translate.google.dj',
                        'translate.google.dk', 'translate.google.dm', 'translate.google.dz',
                        'translate.google.ee', 'translate.google.es', 'translate.google.eu',
                        'translate.google.fi', 'translate.google.fm', 'translate.google.fr',
                        'translate.google.ga', 'translate.google.ge', 'translate.google.gf',
                        'translate.google.gg', 'translate.google.gl', 'translate.google.gm',
                        'translate.google.gp', 'translate.google.gr', 'translate.google.gy',
                        'translate.google.hn', 'translate.google.hr', 'translate.google.ht',
                        'translate.google.hu', 'translate.google.ie', 'translate.google.im',
                        'translate.google.io', 'translate.google.iq', 'translate.google.is',
                        'translate.google.it', 'translate.google.je', 'translate.google.jo',
                        'translate.google.kg', 'translate.google.ki', 'translate.google.kz',
                        'translate.google.la', 'translate.google.li', 'translate.google.lk',
                        'translate.google.lt', 'translate.google.lu', 'translate.google.lv',
                        'translate.google.md', 'translate.google.me', 'translate.google.mg',
                        'translate.google.mk', 'translate.google.ml', 'translate.google.mn',
                        'translate.google.ms', 'translate.google.mu', 'translate.google.mv',
                        'translate.google.mw', 'translate.google.ne', 'translate.google.nf',
                        'translate.google.nl', 'translate.google.no', 'translate.google.nr',
                        'translate.google.nu', 'translate.google.pl', 'translate.google.pn',
                        'translate.google.ps', 'translate.google.pt', 'translate.google.ro',
                        'translate.google.rs', 'translate.google.ru', 'translate.google.rw',
                        'translate.google.sc', 'translate.google.se', 'translate.google.sh',
                        'translate.google.si', 'translate.google.sk', 'translate.google.sm',
                        'translate.google.sn', 'translate.google.so', 'translate.google.sr',
                        'translate.google.st', 'translate.google.td', 'translate.google.tg',
                        'translate.google.tk', 'translate.google.tl', 'translate.google.tm',
                        'translate.google.tn', 'translate.google.to', 'translate.google.tt',
                        'translate.google.us', 'translate.google.vg', 'translate.google.vu', 
                        'translate.google.ws'
])

@app.route('/translate', methods=["POST"])
def translate():
    request_data = request.get_json()
    q = request_data["q"]
    source = request_data["source"]
    target = request_data["target"]

    if( source == "" ):
        translatedObj = translator.translate(q, dest=target)
    else :
        translatedObj = translator.translate(q, dest=target, src=source)

    #print(translator.translate('veritas lux mea', src='la'))
    response = {"translatedText": translatedObj.text}
    return response


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port="3000")
