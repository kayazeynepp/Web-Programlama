Okuyucu rolü için örnek kullanıcı:
email=elif@gmail.com 
password=e.123456

Yazar rolü için örnek kullanıcı:
email=orhan@gmail.com 
password=orhan.123456

NOT:
* Kayıt olurken username alanına tek bir kelime formatında giriş yapılmalıdır. 
* Nltk dosyalarının tamamı yüklenene kadar bekleyiniz. 

Proje Özeti:
Yazarların kendi kitaplarını yayınlayabileceği ve diğer kullanıcılarla etkileşim halinde
olabileceği bir platform tasarlanacaktır.
Projede kullanıcılar, yazarlar tarafından paylaşılmış kitaplar üzerinden sahip olduklar erişim
iznine bağlı olarak kitabı görüntüleyebilir ve yorum yapabilir. Bu sayede yazarların
okuyucularından geri dönüş almaları ve kullanıcıların kişisel görüşlerini yazarlara iletebilmesi
sağlanır.

Özellikler:
1. Presentation Layer: UI Framework Using : Kullancı etkileşiminin sağlandığı, kullanıcı
dostu bir arayüz sağlanacaktır. Kitap paylaşımları ve kullanıcı etkileşimleri bu arayüz
üzerinden sağlanmıştır.
2. Business Layer: OOP Components: Projede kullanılacak nesneleri (örneğin: Kitap,
Kullanıcı, Yorum) ve bunlar arasındaki ilişkileri tanımlamak için OOP prensiplerine uygun
bileşenler oluşturulmuştur.
3. Data Layer: ORM / Migrations Using: Kullanıcı, kitap ve yorum bilgilerini saklamak için
Firebase veritabanı oluşturulmuştur. Proje gereksinimine uygun teknolojiler kullanılmıştır.
4. Web Service Implementation: Kullanıcıların platforma erişimini ve veri akışını sağlamak için uygun API’ler kullanılmıştır. Bu API’ler aracılığıyla kullanıcılar çeşitli işlemler gerçekleştirebilmiştir.
5. RBAC Implementation: Kullanıcı rolüne göre etkileşim izinleri, yetkilendirme kontrolleriyle sağlanmıştır.
Platformda kayıtlı olmayan kullanıcılar kısıtlı işlem yeteneğine sahipken kayıtlı olan kullanıcılar daha geniş işlem yeteneğine sahip olmuştur.
Kayıtlı olmayan kullanıcıların kitap detaylarını görüntüleyememeleri için blurlama özelliği eklenmiştir.
6. Authorization Implementation: Kullanıcı kimlik doğrulaması ve yetkilendirme işlemleri için uygun teknolojileri kullanılmıştır.
7. Session / Cookie Management: Cookieler kullanılarak tema değişimi sağlanmıştır.
8. Extension / Third Party Library Using: AI kullanılarak elde edilen duygu analizinin mathplotlib ile görselleştirilip grafik oluşturulmuştur.
9. Web Security Implementation: Güvenliği sağlamak için Djangoya ait özellikler kullanılmıştır.
10. Cloud Service (AI) Using: Yorumlarda geçen kelimelere göre yorumların duygu analizi yapılarak yorumların renklendirilmiştir.(Türkçe yorumlar için geçerlidir.)


    
