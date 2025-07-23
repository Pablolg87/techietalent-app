import streamlit as st
import openai

# 👉 Sustituye esto con tu clave personal de OpenAI
openai.api_key = "TU_API_KEY"

st.set_page_config(page_title="TechieTalent Performance", page_icon="🧠", layout="centered")
st.title("💼 TechieTalent Performance")
st.subheader("Asistente de IA para evaluación de talento y performance")

prompt = st.text_area("✍️ Escribe tu consulta:", placeholder="Ej. ¿Cómo mejorar el rendimiento de mi equipo de ventas?")

if st.button("🔍 Analizar con IA") and prompt.strip():
    with st.spinner("Pensando..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un experto en recursos humanos, talento y rendimiento organizacional."},
                    {"role": "user", "content": prompt}
                ]
            )
            output = response.choices[0].message.content
            st.markdown("### 🧠 Resultado:")
            st.write(output)
        except Exception as e:
            st.error(f"Error al conectar con OpenAI: {e}")