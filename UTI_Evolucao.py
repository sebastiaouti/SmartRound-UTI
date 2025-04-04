import streamlit as st

def evolucao_uti_interface():
    st.title("📋 Evolução Diária - UTI")

    with st.form("form_uti"):
        st.subheader("Identificação do Paciente")
        col1, col2, col3 = st.columns(3)
        nome = col1.text_input("Nome")
        leito = col2.text_input("Leito")
        idade = col3.number_input("Idade", min_value=0, max_value=120, step=1)

        col4, col5, col6 = st.columns(3)
        sexo = col4.selectbox("Sexo", ["Masculino", "Feminino"])
        diag = col5.text_input("Diagnóstico Principal")
        data = col6.date_input("Data da internação")

        st.subheader("Avaliação Sistêmica")
        via_aerea = st.radio("Via aérea", ["Espontânea", "O2 Suplementar", "VM", "Traqueostomizado"])
        oxigenacao = st.text_input("Oxigenação (SatO2, FiO2, VM)")
        hemo = st.text_input("Hemodinâmica (PA, FC, PAM, drogas)")
        neuro = st.text_input("Neurológico (Glasgow, sedação, pupilas)")
        renal = st.text_input("Renal (diurese, débito, SVD, diálise)")
        gastro = st.text_input("GI / Nutrição (SNE, dieta, evacuação)")
        infecto = st.text_input("Infectologia (febre, antibióticos, cultura)")
        pele = st.text_input("Pele / Dispositivos (úlceras, punções)")
        lab = st.text_area("Laboratório / Imagem")
        conduta = st.text_area("Conduta e plano")

        usar_ia = st.checkbox("Interpretar com IA (sugestões e conduta)", value=True)

        submit = st.form_submit_button("Gerar Evolução")

        if submit:
            st.subheader("Texto gerado:")
            st.markdown(f"""
**Evolução de paciente crítico - UTI**

Paciente {nome}, {idade} anos, sexo {sexo.lower()}, internado no leito {leito} com diagnóstico principal de {diag}. Internado desde {data.strftime('%d/%m/%Y')}.

- **Via aérea**: {via_aerea}
- **Oxigenação**: {oxigenacao}
- **Hemodinâmica**: {hemo}
- **Neurológico**: {neuro}
- **Renal**: {renal}
- **GI / Nutrição**: {gastro}
- **Infectologia**: {infecto}
- **Pele / Dispositivos**: {pele}
- **Exames**: {lab}
- **Conduta**: {conduta}

{"# Interpretação com IA:\n*A interpretação com IA nesse caso não está correlacionada à clínica do paciente e deve ser analisada com atenção.*" if usar_ia else ""}
            
*By Sebastião Almeida*
""")
