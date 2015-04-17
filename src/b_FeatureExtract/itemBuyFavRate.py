# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午3:09:18
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString 
def itemBuyFavRate(dateScope,outputPath):
    featureSid="101"
#     outputPath=Conf.featureExtractPath+"/"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"""
        select 
        item_id,ceil(100*((sum(if(behavior_type=4,1,0))+1)/(sum(if(behavior_type=2,1,0))+1))) as BuyFavRate 
        from useritem 
        where date_format(usertime,'%%Y%%m%%d') in (%s) 
        group by item_id 
        order by BuyFavRate desc;
        """%(dateString)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo(Result, outputPath,featureSid)
#以下为测试代码
# itemBuyFavRate("20141122-20141127",r"\1122_1127\itemBuyFavRate.csv")