# -*- coding: UTF-8 -*-

import sys
import time
import json
import requests

def GenerateOneText(sApi, iRate, iNum, sType=None):
    """生成一言文本"""
    
    """
    sApi: 调用接口
    iRate: 调用接口频率
    iNum: 生成一言总数
    sType: 一言语句类型
    ---------------------
    a：动画     b：漫画
    c：游戏     d：文学
    e：原创     f：来自网络
    g：其他     h：影视
    i：诗词     j：网易云
    k：哲学     l：抖机灵
    ---------------------
    """
    dtext = {}
    dtext['total'] = iNum
    if sType:
        sApi = "".join([sApi, '/?c=', sType])
    for i in range(iNum):
        response = requests.get(sApi)
        sText = response.text
        dData = json.loads(sText)
        dNewData = {}
        hitokoto = dData.get("hitokoto", "")
        source = dData.get("from", "")
        creator = dData.get("creator", "")
        update = dData.get("created_at", "")
        if update:
            update = time.localtime(int(update))
            update = time.strftime("%Y-%m-%d %H:%M:%S", update)
        dNewData.update({"hitokoto":hitokoto, "from":source, "creator":creator, "update":update})
        dtext[str(i+1)] = dNewData
        time.sleep(iRate)
    return dtext

if __name__ == "__main__":
    sApi = "https://v1.hitokoto.cn"
    iRate = 4
    iNum = 5
    sType = 'a'
    sPath = "yiyan.json"
    dtext = GenerateOneText(sApi, iRate, iNum)
    json_str = json.dumps(dtext, ensure_ascii=False, indent=4)
    with open(sPath, "w", encoding="utf-8") as fw:
        fw.write(json_str)
