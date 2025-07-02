import google.generativeai as genai
import my_api_key
import gradio as gr

# API anahtarıyla yapılandırma
genai.configure(api_key=my_api_key.api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate(prompt):
    cevap = model.generate_content(prompt)

    return cevap.text

title = "✨ Yapay Zeka ile Sohbet Et! ✨"
description = "📌 Aklına gelen her şeyi Google Gemini'ye sor. Bilgi, eğlence, yaratıcı yazım ve çok daha fazlası seni bekliyor."

# Arayüzü oluştur
gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="💬 Mesajınızı yazın", placeholder="Örn: Bugün hava nasıl?", lines=3),
    outputs=gr.Textbox(label="🤖 Cevap", lines=8),
    title=title,
    description=description,
    theme="gstaff/xkcd"
).launch(server_port=8080, share=True)
