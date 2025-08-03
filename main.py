import random
import gradio as gr

nombres = ["Zarkon", "Mutog", "Xeltra", "Gribnax", "Krow'thar", "Moltrik"]
tipos = ["insectoide", "anfibio radiactivo", "humanoide fallido", "quimera", "bestia nuclear"]
descripciones = [
    "Una criatura deformada por siglos de radiación.",
    "Tiene múltiples ojos y tentáculos brillantes.",
    "Puede regenerarse rápidamente, pero pierde masa cerebral.",
    "Se comunica con chillidos que queman el aire.",
    "Tiene un instinto asesino y cero empatía.",
    "Es adorado por mutantes menores como un dios."
]

def generar_mutante():
    nombre = random.choice(nombres)
    tipo = random.choice(tipos)
    descripcion = random.choice(descripciones)
    return f"🧬 Nombre: {nombre}\n🧪 Tipo: {tipo}\n📖 Descripción: {descripcion}"

iface = gr.Interface(fn=generar_mutante, inputs=[], outputs="text", title="🧟 Mutant Generator MINI")
iface.launch()
