# TRY-TRYB-Arbitrage

Türk lirasında yaşanan dalgalanmalar veya Kripto Para sektöründe yaşanan ani gelişmeler sonucunda, TL-USD fiyatı ile TL-USDT fiyatı ararsındaki farktan yararlanmak için kullanılabilecek basit bir Telegram bildirimleri uygulaması.

Takip edilecek alım satım adımları aşağıdaki gibidir:

1) Herhangi bir Türk bankasındaki hesaptan BtcTürk'e TL aktarımı
2) BtcTürk üzerinde USDT alımı
3) USDT'lerin Huobi borsasına gönderilmesi
4) Huobi borsasında USDT'lerin USDC'ye çevirilmesi
5) USDC'lerin Ethereum cüzdanına aktarılması
6) BiLira platformu üzerinde USDC'den TRYB'ye swap işleminin gerçekleştirilmesi
7) TRYB'lerin banka hesabına geri çekilmesi


Adımlar arasında BtcTürk'ten doğrudan USDC almak yerine, Huobi'ye USDT'lerin gönderilip sonrasında USDC'ye çevrildiğini görebilirsiniz. Bunun sebebi, Huobi borsasında USDC çekim işlemlerinin batchlenerek gerçekleştirilmesi sebebiyle 2 USDC gibi düşük bir komisyon ücretiyle gerçekleştirilmesidir. BtcTürk'te USDC çekim işlemlerinde 15 USDC komisyon ücreti uygulanmaktadır. 

Bu adımların tamamında amaç, birbirinden bağımsız çalışan fakat ilişkili olan piyasalardaki farklardan faydalanabilmektir. Gerçekleştirilen adımlar için akış şeması şekildeki gibidir:

![Arbitraj işlemi için akış şeması](https://github.com/iakarsu/TRY-TRYB-Arbitrage/blob/main/schema1.png?raw=true)

config.py dosyası üzerinde, borsaların komisyon oranlarını, programın kontrol sıklığını ve başlangıç bakiyenizi değiştirebilirsiniz. Ayrıca, config.py dosyasındaki TELEGRAM bağlantı bilgilerini de doldurmanız halinde, %3'ten yüksek arbitraj olanakları yakalanırsa TELEGRAM kanalınıza bildirim gelecek şekilde ayarlama yapabilirsiniz.


## Projeyi Çalıştırma Adımları

- pip install -r requirements.txt
- python arb.py

