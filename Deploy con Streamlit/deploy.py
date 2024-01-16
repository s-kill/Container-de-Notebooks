import streamlit as st
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import norm

st.title("Tendencia y Predicción")

class Predictor:
   def Prepare_data(self):

      #MA
      Muestras_MA=np.empty([10])        
      for i in range(10):
         Muestras_MA[i]=np.mean(self.data[i:i+3])
      
      self.Muestras_MA = Muestras_MA 
   
      #CMA (Tendencia)
      Muestras_CMA=np.empty([9])
        
      for i in range(9):
         Muestras_CMA[i]=np.mean(self.Muestras_MA[i:i+2])
      
      self.Muestras_CMA = Muestras_CMA 
   
      #Si_Ii
      Si_Ii=np.empty([9])

      for i in range(9):
         Si_Ii[i] = self.data[i+2]/Muestras_CMA[i]
      
      self.Si_Ii = Si_Ii

      #S_I
      S_i = np.empty([3])
      
      for i in range(3):
         tercio = 3
         sum_aux = 0
         count = 0
         for val in self.Si_Ii:
            if(i+1==tercio): #si el trimestre buscado es igual al tercio
               sum_aux += val
               count += 1
            if(tercio==3):
               tercio=1
            else:
               tercio+=1

         S_i[i]=sum_aux/count
      self.S_i = S_i

      #Deseasonanlize
      deseas = np.empty([12])
      tercio = 1
      for i in range(12):
         deseas[i] =  self.data[i] / self.S_i[tercio-1]
         if(tercio == 3):
            tercio = 1
         else:
            tercio += 1
      self.deseas = deseas


      #T_t y P_t
      T_t = np.empty([15])
      P_t = np.empty([15])
      X = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
      X = X.reshape(-1,1)
      reg = LinearRegression().fit(X, self.data)      
      inter = reg.intercept_
      coef = reg.coef_[0]

      tercio = 1
      
      for i in range(15):
         T_t[i] = coef*(i+1)+inter
         P_t[i] = T_t[i] * self.S_i[tercio-1]
         if(tercio == 3):
            tercio = 1            
         else:
            tercio += 1
      
      self.P_t = P_t





      #plot_results
      Meses = ["Ene","Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "En","Fe", "Ma"]
      #valores = self.Data
      #Tendencia = self.Muestras_CMA
      #Predict = self.T_t

      fig, ax = plt.subplots()
      ax.plot(Meses[0:12], self.data, label='Reales', color='blue')
      ax.plot(Meses[0:9], self.Muestras_CMA, label='Tendencia', color = 'red')
      ax.plot(Meses[0:15], self.P_t, label='Prediccion', color = 'green')
      legend = ax.legend()
      plt.xlabel('Meses')
      plt.ylabel('N° Ventas')
      plt.title('Ventas de bicicletas')
      st.pyplot(fig)
      #st.line_chart(chart_data)


      #Data Control inventario
      Dem_pro = np.mean(self.data)
      Dev_est = np.std(self.data,ddof=1)
      Dev_TL = np.sqrt((self.t_ent + self.t_rev) * Dev_est ** 2)
      Z = norm.ppf(0.98)
      Cant_P = Dem_pro * (self.t_ent + self.t_rev) + Z * Dev_TL - self.exist
      
      #Print Data Inv
      st.title("Control de inventario")
      st.write(pd.DataFrame({
         'Existencias dis': [self.exist],
         'Tiempo de entrega': [self.t_ent],
         'Tiempo de revision': [self.t_rev],
         'Prob de Agotamiento': [0.98],   
         }))
      st.write(pd.DataFrame({
         'Demanda Promedio': [Dem_pro],
         'Desviación Estandar': [Dev_est],
         'Desviación T+L': [Dev_TL], 
         'Nivel de Servicio (Z)': [Z]      
         }))
      st.write(pd.DataFrame({
         'Cantidad a pedir': [Cant_P]         
         }))

      




if __name__ == '__main__':
   controller = Predictor()
   st.sidebar.title("Ventas")
   meses = np.empty([12])
   meses[0] = st.sidebar.number_input('Enero',min_value=0, value=56)
   meses[1] = st.sidebar.number_input('Febrero',min_value=0, value=24)
   meses[2] = st.sidebar.number_input('Marzo',min_value=0, value=10)
   meses[3] = st.sidebar.number_input('Abril',min_value=0, value=4)
   meses[4] = st.sidebar.number_input('Mayo',min_value=0, value=19)
   meses[5] = st.sidebar.number_input('Junio',min_value=0, value=24)
   meses[6] = st.sidebar.number_input('Julio',min_value=0, value=21)
   meses[7] = st.sidebar.number_input('Agosto',min_value=0, value=158)
   meses[8] = st.sidebar.number_input('Septiembre',min_value=0, value=41)
   meses[9] = st.sidebar.number_input('Octubre',min_value=0, value=59)
   meses[10] = st.sidebar.number_input('Noviembre',min_value=0, value=204)
   meses[11] = st.sidebar.number_input('Diciembre',min_value=0, value=257)
   controller.exist = st.sidebar.number_input('Existencias disponibles',min_value=0, value=185)
   controller.t_ent = st.sidebar.number_input('Tiempo de entrega',min_value=0, value=3)
   controller.t_rev = st.sidebar.number_input('Tiempo de revision', value=0.3)

   controller.data = meses
   controller.Prepare_data()
   
   


   
