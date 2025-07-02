# Gemini API ile Basit Sohbet Arayüzü

![Uygulama Arayüzü](images/demo.png)


Bu proje, **Google Gemini 1.5 Flash** modelini kullanarak Python ve Gradio ile oluşturulmuş basit bir sohbet uygulamasıdır. Amacı, Gemini API'sinin nasıl çalıştığını hızlıca görmek ve test etmektir.


## Özellikler

- Google Gemini API entegrasyonu  
- Gradio ile kullanıcı dostu web arayüzü  
- Türkçe dil desteği  
- Hızlı kurulum, kolay kullanım  

## Kurulum ve Kullanım

### 1. Depoyu klonlayın veya ZIP olarak indirin

### 2. Gerekli Python paketlerini yükleyin
```bash
pip install -r requirements.txt
```

### 3. API anahtarınızı ekleyin
Proje dizinine my_api_key.py adında bir dosya oluşturun ve aşağıdaki şekilde doldurun:

```bash
# my_api_key.py
api_key = "BURAYA_KENDİ_GEMINI_API_KEYİNİZİ_YAZIN"
```

Google Gemini API anahtarını buradan alabilirsiniz : https://www.google.com/url?q=https%3A%2F%2Fmakersuite.google.com%2Fapp%2Fapikey  

### 4. Uygulamayı başlatın

```bash
python app.py
```

### ❗ Önemli Not
my_api_key.py dosyası kişiseldir, kimseyle paylaşmayın.

 ### Kullanılan Teknolojiler
 - Google Generative AI (Gemini 1.5 Flash)
 - Gradio
 - Python 3.12


