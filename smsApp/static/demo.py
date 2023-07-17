from smsApp.static.WXBizDataCrypt import WXBizDataCrypt

def main():
    appId = '************'
    sessionKey = '************'
    encryptedData = '************'
    iv = '************'

    pc = WXBizDataCrypt(appId, sessionKey)

    print( pc.decrypt(encryptedData, iv))

if __name__ == '__main__':
    main()
