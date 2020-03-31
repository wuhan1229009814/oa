import time

def getTimeStamp():
    """

    :return:返回当前年月日和时间戳后4位生成id
    """
    #生成时间戳
    time_stamp = str(time.time())
    #生成当前年月日时间
    time_date = time.strftime("%Y%m%d", time.localtime())
    #返回当前年月日和时间戳后4位
    return time_date[2:] + time_stamp[-4:]