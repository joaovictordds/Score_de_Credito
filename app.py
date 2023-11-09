import streamlit as st
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline

modelo = joblib.load('modelo_boosting.pkl')

paginas = ['Home','Modelo - Score de Crédito']

pagina = st.sidebar.radio('Navegue por aqui:', paginas)

if pagina == 'Home':
    st.title('Meus modelos em produção :gem:')
    
if pagina == 'Modelo - Score de Crédito':
    
    st.title('Modelo para Score de crédito')
    st.markdown('---')
    
    st.write('Selecione a idade entre 18 e 65 anos:')
    idade = st.number_input('Age_years', 18, 65, 18)
    st.write('**Sexo:**     0 - solteiro, 1 - casado 2- feminino')
    sexo = st.selectbox('Sex_Marital_Status',[0,1,2])
    st.write('**Tempo de Serviço:** **0** - Menos de 1 ano, **1:** 1 a 4 anos **2:** 4 a 7 anos **3:** 7 ou mais')
    tempo_servico = st.selectbox('Length_of_current_employment', [0,1,2,3])
    st.write('Quantidade de parcelas:')
    parcelas = st.number_input('Duration_of_Credit_monthly', 0, 200, 3)
    st.write('Saldo atual do cliente:')
    saldo = st.number_input('Account_Balance', 0, 100000, 0)
    st.write('Possui outros financiamentos')
    st.write('**0**: Outros bancos, **1:** Em lojas de departamento, **2:** nenhum')
    outros_cred = st. selectbox('No_of_Credits_at_this_Bank', [0,1,2])
        
    input0 = {'Age_years':[idade], 'Sex_Marital_Status':[sexo], 'Duration_of_Credit_monthly':[parcelas], 'Account_Balance':[saldo],'No_of_Credits_at_this_Bank':[outros_cred],'Length_of_current_employment':[tempo_servico]}
    input = pd.DataFrame(input0)
    
    st.markdown('---')
    
    if st.button('Executar'):
        previsao_novos_dados = modelo.predict(input)
        saida = []
        #saida = previsao_novos_dados
        if previsao_novos_dados == 0:
            saida = 'Não aprovar novo crédito'
        else:
            saida= 'Aprovado'   
        st.subheader(saida)



        
            