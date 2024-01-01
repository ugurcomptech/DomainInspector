# DomainInspector

Bu Python betiği, bir alan adı için DNS sorgularını ve WHOIS sorgularını basitleştirir.

## Özellikler:

1. Google'ın DNS sunucularından yararlanarak doğru ve hızlı sonuçlar elde eder.
2. A, NS, MX, CNAME ve TXT gibi çeşitli kayıt türlerini alır.
3. Alan adı son kullanma tarihi gibi WHOIS bilgilerini getirir.
4. PrettyTable kullanarak sonuçları açık ve organize bir tablo formatında sunar.
5. Kolay kullanım için komut satırı arayüzü sunar.

## Kurulum:

Sisteminizde Python yüklü olduğundan emin olun.
Gerekli kitaplıkları pip kullanarak yükleyin:

```
pip install dnspython whois prettytable
```

## Kullanım:

Bu deposu klonlayın veya indirin.
Betiği komut satırından çalıştırın:

```
python app.py example.com -t A NS MX
```
1. example.com: Sorgulanacak alan adı (komut satırı argümanında belirtilmişse isteğe bağlı).
2. -t, --type: İsteğe bağlı olarak sorgulanacak bir veya daha fazla kayıt türünü belirtin (varsayılan: A, NS, MX, CNAME, TXT).

## Çıktı:
```
+------------------+--------------------+
| Kayıt Türü     | Sonuç             |
+------------------+--------------------+
| A               | 93.184.216.34      |
| MX              | mail.example.com   |
| WHOIS           | 2025-01-01         |
+------------------+--------------------+
```


## Kayıt Türleri

1. **A:** Alan adının IP adresini döndürür.
2. **NS:** Alan adının DNS sunucularını döndürür.
3. **MX:** Alan adının e-posta sunucularını döndürür.
4. **CNAME:** Alan adının takma adını döndürür.
5. **TXT:** Alan adıyla ilişkili metin verilerini döndürür.

## WHOIS Bilgileri

1. **Alan adı:** Alan adının adı.
2. **Son kullanma tarihi:** Alan adının son kullanma tarihi.
3. **Kayıt sahibi:** Alan adını kaydeden kişi veya kuruluş.
4. **Kayıt kayıtçısı:** Alan adını kaydeden kayıt şirketi.
5. **Kayıt sunucusu:** Alan adının DNS sunucuları.


## Ek Bilgiler:

Desteklenen Kayıt Türleri: A, NS, MX, CNAME, TXT
Bağımlılıklar: dnspython, whois, prettytable
Yazar: [Uğur]
Lisans: [![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

## Katkılar:

Bu projeye sorun göndererek, pull isteği yaparak veya iyileştirmeler önererek katkıda bulunabilirsiniz!




