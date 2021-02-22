import Algorithmia

input = {
  "image": "data://gimmy/mlbook/black1.jpg"
}
try:
    client = Algorithmia.client('simNzAsHiHWn3zWnktx4UBG8mLO1')
    algo = client.algo('deeplearning/ColorfulImageColorization/1.1.13')
    print(algo.pipe(input).result)
except:
    print('資料圖片檔案讀取錯誤！')
    