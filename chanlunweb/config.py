import pathlib

"""
服务总配置文件
"""

# WEB 服务器IP
WEB_HOST = '127.0.0.1'

# WEB 登录密码，为空则无需进行登录
LOGIN_PWD = ''

# 项目数据保存路径，如果以 . 开头，则保存到 home 目录，否则按照设置目录来
DATA_PATH = ".chanlun_web"

# 代理服务器配置
PROXY_HOST = ''
PROXY_PORT = 7890

# 数据库配置
DB_TYPE = "sqlite"  # 支持  mysql 与 sqlite，如果是 sqlite 则只需填写 DB_DATABASE 即可
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'chanlunweb'
DB_PWD = '123456'
DB_DATABASE = 'chanlun_web_klines'

# Redis 配置，不使用可将 REDIS_HOST 设置为空字符串
REDIS_HOST = ''  # 127.0.0.1
REDIS_PORT = 6379

# 各个市场的交易所设置（只适用于WEB页面的行情展示）
# A股市场支持：tdx / baostock
# 港股市场支持：tdx_hk / futu
# 期货市场支持：tq / tdx_futures
# 数字货币支持： binance / zb
# 美股市场支持： alpaca / polygon / ib / tdx_us
EXCHANGE_A = 'tdx'
EXCHANGE_HK = 'futu'
EXCHANGE_FUTURES = 'tq'
EXCHANGE_CURRENCY = 'binance'
EXCHANGE_US = 'ib'

# 通达信目录（例如 C:/new_tdx），用于获取行业与概念信息，留空则使用 exchange/stocks_bkgn.json 进行获取
TDX_PATH = ''

# 掘金设置 https://www.myquant.cn/docs2/faq/#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8-linux-%E7%89%88%E6%9C%AC%E7%9A%84-python-sdk
GM_SERVER_ADDR = '127.0.0.1:7001'
GM_TOKEN = '******'

# 富途API配置（不使用请将 FUTU_HOST 留空）
FUTU_HOST = ''
FUTU_PORT = 11111
FUTU_UNLOCK_PWD = ''

# 天勤账号配置
TQ_USER = '0xjun'
TQ_PWD = 'tq123456..'
TQ_SP_NAME = 'simnow'
TQ_SP_ACCOUNT = ''
TQ_SP_PWD = ''

# 币安交易所配置
BINANCE_APIKEY = ''
BINANCE_SECRET = ''

# ZB交易所配置
ZB_APIKEY = ''
ZB_SECRET = ''

# 美股 Ploygon API 配置（申请网址 https://polygon.io/）
POLYGON_APIKEY = ''

# 美股 Alpaca API 配置（申请网址 https://alpaca.markets/）
ALPACA_APIKEY = ''
ALPACA_SECRET = ''

# 盈透证券 TWS 设置
IB_HOST = '127.0.0.1'
IB_PORT = 7497
IB_CLIENT_ID = 1
IB_ACCOUNT = 'DU6941075'

# 飞书消息配置 (项目中新的消息推送使用飞书，user_id 是唯一的，不同的市场可以配置不同的机器人，没有设置则使用 default 的机器人)
# 配置获取方法，在 web 页面的系统设置中有教程
FEISHU_KEYS = {
    "default": {
        "app_id": "cli_********",
        "app_secret": "TlQXy9Y7********",
    },
    "a": {
        "app_id": "cli_********",
        "app_secret": "TlQXy9Y7********",
    },
    "us": {
        "app_id": "cli_********",
        "app_secret": "TlQXy9Y7********",
    },
    "hk": {
        "app_id": "cli_********",
        "app_secret": "TlQXy9Y7********",
    },
    "futures": {
        "app_id": "cli_********",
        "app_secret": "TlQXy9Y7********",
    },
    "currency": {
        "app_id": "cli_********",
        "app_secret": "TlQXy9Y7********",
    },
    "user_id": "86********",
    "enable_img": False,
}

def get_data_path():
    # 获取项目数据的目录
    data_path = pathlib.Path(DATA_PATH)
    if DATA_PATH.startswith("."):
        data_path = pathlib.Path().home() / DATA_PATH
    if data_path.is_dir() is False:
        data_path.mkdir(parents=True)
    print(data_path)
    return data_path
