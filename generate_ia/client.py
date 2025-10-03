import google.generativeai as genai



def generate_gift_description(gift_name):
    prompt = ("Escreva a descrição breve do produto com apenas 2 linhas para um presente de casamento chamado, '{}'.")

    genai.configure(api_key="AIzaSyAVBakZq1KjztTX71Gxwzb-UavIgUpO9q0")
    
    model = genai.GenerativeModel("models/gemini-flash-latest")

    response = model.generate_content(prompt.format(gift_name))
    
    return response.text
