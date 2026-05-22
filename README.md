# Toplumsal Fren Sistemleri (Social Braking Systems)

Kısa açıklama
----------------

Bu proje, basit bir "toplumsal fren" (social braking) modelini ve simülasyon iskeletini içerir. Amaç, bireylerin/araçların öndeki birime çok yakınlaştığında nasıl hız azalttığını gösteren deneysel bir altyapı sağlamaktır.

Neden?
------

Toplumsal fren davranışı; trafik, yaya hareketleri ve toplumsal etkileşim modellerinde kritik bir rol oynar. Bu depo minimal bir prototip sunar — araştırma veya eğitim amaçlı genişletilmeye uygundur.

Öne çıkan özellikler
--------------------

- Basit 1D ajan-temelli fren modeli (`toplumsal_fren_sistemleri.core`).
- Örnek çalıştırıcı: `run_simulation.py`
- Birim testleri: `tests/test_core.py`

Kurulum
-------

1. Python 3.8+ kurulu olduğundan emin olun.
2. (İsteğe bağlı) Sanal ortam oluşturun ve etkinleştirin.
3. Gereksinimler (şu an boş):

```
pip install -r requirements.txt
```

Çalıştırma
---------

- Örnek simülasyonu çalıştırmak için:

```
python run_simulation.py
```

- Testleri çalıştırmak için:

```
python -m unittest discover -v tests
```

Örnek çıktı
-----------

`run_simulation.py`, her adım için ajan hızlarının kısa bir özetini yazdırır. Bu, modelin takip edenlerin yakınlaştıkça yavaşladığını göstermeye yöneliktir.

Alıntılar ve ilham kaynakları
----------------------------

Aşağıdaki kısa alıntılar proje fikirlerini ve ilham kaynaklarını vurgular:

- "Bireylerin davranışları, toplumsal etkileşimler tarafından şekillenir." — Sosyal davranış paradigması
- "Güvenli mesafe, akıcı ve güvenli trafik akışı için kritiktir." — Trafik güvenliği ilkesi
- "Ajan-tabanlı modeller, mikro davranışların makro örüntülere dönüşümünü gösterir." — Modelleme yaklaşımı

Önerilen okuma / kaynaklar
-------------------------

- Treiber, M., & Kesting, A. — Trafik akışı ve araç dinamiği üzerine çalışmalar.
- Agent-based modelling literature reviews — agent tabanlı modelleme girişleri ve incelemeleri.

Katkıda bulunma
---------------

Katkılar memnuniyetle karşılanır. Yeni özellikler, görselleştirme, gerçekçi araç modelleri veya veri setleri eklemek için issue açın ve pull request gönderin.

Lisans
------

Bu proje açık kaynaklıdır; lisans olarak `MIT` veya depo sahibinin tercih ettiği başka bir lisans eklenebilir.

İletişim
--------

Proje sahibi ve uzak repo: https://github.com/arch-yunus/Toplumsal-Fren-Sistemleri
