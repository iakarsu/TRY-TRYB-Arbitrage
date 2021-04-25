import requests
import time
from config import BTCTURK_COMISSION_RATE, HUOBI_COMMISSION_RATE, HUOBI_USDC_WITHDRAW_FEE, BILIRA_COMMISSION_FEE, \
                    TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, INITIAL_BALANCE, FREQUENCY

btctr_commission = BTCTURK_COMISSION_RATE
huobi_commission = HUOBI_COMMISSION_RATE
huobi_wtrdw = HUOBI_USDC_WITHDRAW_FEE
bilira_commission = BILIRA_COMMISSION_FEE

# Get TL-USDT last price from BTCTURK
def getTLUSDT():
    url = 'https://api.btcturk.com/api/v2/ticker'
    payload = {'pairSymbol': 'USDT_TRY'}

    response = requests.get(url, params=payload).json()
    return response['data'][0]['last']

# Get USDT-USDC last price from HUOBI
def getUSDTUSDC():
    url = 'https://api.huobi.pro/market/history/trade'
    payload = {'symbol': 'usdcusdt', 'size': 1}

    response = requests.get(url, params=payload).json()
    return response['data'][0]['data'][0]['price']

# Get ETH-USDT last price from HUOBI
def getUSDTETH():
    url = 'https://api.huobi.pro/market/history/trade'
    payload = {'symbol': 'ethusdt', 'size': 1}

    response = requests.get(url, params=payload).json()
    return response['data'][0]['data'][0]['price']

# Get USDC-TRYB swap price from 0X
def getUSDCTRYB(amount=1000):
    url = 'https://api.0x.org/swap/v1/quote'

    payload = {
        'buyToken': '0x2c537e5624e4af88a7ae4060c022609376c8d0eb',
        'sellToken': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
        'sellAmount': amount * 1000000
    }

    response = requests.get(url, params=payload).json()
    return response['guaranteedPrice']

def sendTGMessage(rate):
    message = """ Su anda, arbitraj yontemi icerisinde belirtilen adımları uygulamanız halinde
                {} oranında kar elde edebilirsiniz.  """.format(rate)

    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
    payload = {'chat_id': TELEGRAM_CHAT_ID,'text': message}
    response = requests.post(url, params=payload).json()

    return response

# Calculate Arbitrage outputs     
def arb(initial_balance = INITIAL_BALANCE):
    print('INITIAL BALANCE', initial_balance)

    # TL to USDT on BTCTURK
    tl_usdt = getTLUSDT()
    print('BTCTURK USDT PRICE', tl_usdt)
    usdt_amount = (initial_balance - (initial_balance * btctr_commission)) / tl_usdt
    print('BTCTURK USDT AMOUNT:', usdt_amount)
    usdt_amount -= 1 #withdraw fee

    # USDT to USDC on HUOBI
    usdt_usdc = getUSDTUSDC()
    usdc_amount = (usdt_amount - (usdt_amount * huobi_commission)) / usdt_usdc
    print('HUOBI USDC AMOUNT:', usdc_amount)
    usdc_amount -= 2 #withdraw fee

    # USDC to TRYB on BiLira
    usdc_eth = getUSDTETH() # eth price

    eth_commission = usdc_eth * 0.007 # eth commission
    print('SWAP_COMMISSION', eth_commission)

    usdc_amount -= eth_commission # total balance after commission
    print('USDC AMOUNT AFTER ETH COMMISSION', usdc_amount)

    usdc_tryb = getUSDCTRYB(round(usdc_amount)) # swap price
    print('USDC - TRYB PRICE', usdc_tryb)

    tryb_amount = usdc_amount * float(usdc_tryb)
    print('TOTAL TRYB AMOUNT', tryb_amount)

    # TRYB to TL on BiLira
    bank_amount = tryb_amount - (tryb_amount * bilira_commission)
    print('TOTAL AMOUNT GOING TO BANK', bank_amount)
    return bank_amount


while(True):
    time.sleep(FREQUENCY)
    last_balance = arb()
    if(last_balance >= INITIAL_BALANCE * 1.03):
        try:
            sendTGMessage((last_balance - INITIAL_BALANCE) / INITIAL_BALANCE * 100)
        except:
            print("There might be a arb. chance, please check your TG setup.")