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

Bu adımların tamamında amaç, birbirinden bağımsız çalışan fakat ilişkili olan piyasalardaki farklardan faydalanabilmektir.

![Arbitraj işlemi için akış şeması](https://pbs.twimg.com/profile_images/427400464259244034/BOca13ao_400x400.jpeg)

