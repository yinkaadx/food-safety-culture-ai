import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Food Safety Culture AI", layout="wide")

st.title("Serverless Food Safety Culture Pipeline")
st.caption("Real-Time Organizational Behavior Analytics & AI Intervention Engine")

st.sidebar.header("Multi-Plant Configuration")
selected_plant = st.sidebar.selectbox("Target Manufacturing Plant", ["Auckland Meat Processing Plant", "Christchurch Dairy Facility", "Wellington Agro-Logistics Hub"])
culture_shock = st.sidebar.slider("Simulate Cultural Degradation Event", 1.0, 5.0, 3.0)
run_simulation = st.sidebar.button("Initialize Culture AI Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Behavioral API Ingestion -> XGBoost Inference -> Intervention Deployment")

if run_simulation:
    st.subheader(f"Active Cultural Maturity Monitoring: {selected_plant}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_compliance = col1.empty()
    metric_nearmiss = col2.empty()
    metric_maturity = col3.empty()
    metric_action = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(2020)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    compliance_rates = []
    maturity_scores = []
    
    base_compliance = 98.0 
    base_maturity = 85.0
    
    for i in range(100):
        if i < 35:
            current_comp = base_compliance + np.random.uniform(-1.0, 1.0)
            current_mat = base_maturity + np.random.uniform(-2.0, 2.0)
            near_misses = int(np.random.uniform(0, 2))
        elif i >= 35 and i < 65:
            current_comp = base_compliance - (i - 35) * (0.3 * culture_shock) + np.random.uniform(-2.0, 2.0)
            current_mat = base_maturity - (i - 35) * (0.8 * culture_shock) + np.random.uniform(-3.0, 3.0)
            near_misses = int(np.random.uniform(2, 8 * culture_shock))
        else:
            current_comp = current_comp + np.random.uniform(0.5, 1.5)
            current_mat = min(90.0, current_mat + 2.0 + np.random.uniform(-1.0, 1.0))
            near_misses = int(np.random.uniform(0, 3))
            
        compliance_rates.append(current_comp)
        maturity_scores.append(current_mat)
        
        metric_compliance.metric("Floor Compliance Rate", f"{current_comp:.1f}%", f"{(current_comp - base_compliance):.1f}%")
        metric_nearmiss.metric("Near-Miss Reports / Hr", f"{near_misses}", "Behavioral Friction")
        metric_maturity.metric("Culture Maturity Index", f"{current_mat:.1f} pts")
        
        if current_mat <= 60.0:
            metric_action.metric("AI Recommendation", "DEPLOYING INTERVENTION", "Targeted Retraining")
        elif i >= 65:
            metric_action.metric("AI Recommendation", "CULTURE RECOVERING", "Intervention Successful")
        else:
            metric_action.metric("AI Recommendation", "MAINTAINING PROTOCOLS", "Stable Culture")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=compliance_rates, mode='lines', name='Compliance Rate (%)', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=maturity_scores, mode='lines', name='Culture Maturity Index', yaxis='y2', line=dict(color='orange', dash='dot')))
        
        fig.update_layout(
            title="Food Safety Culture: Behavioral Compliance vs AI-Measured Maturity Index",
            xaxis=dict(title="High-Frequency Operational Timestamp"),
            yaxis=dict(title="Compliance (%)", range=[60, 100]),
            yaxis2=dict(title="Maturity Index (Pts)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if current_mat <= 60.0 and i == 64:
            log_placeholder.error(f"CULTURE ALERT: Severe behavioral degradation detected at {time_steps[i].strftime('%H:%M:%S')}. Machine learning inference engine identified process gaps. Autonomous retraining intervention deployed to factory floor.")
        elif i >= 65 and i % 5 == 0:
            log_placeholder.success(f"INTERVENTION SUCCESS: Post-intervention data streams confirm behavioral alignment. Culture Maturity Index recovering to baseline metrics.")
        elif i < 35 and i % 5 == 0:
            log_placeholder.info(f"Log: Organizational telemetry tick {i} ingested via serverless middleware. Food safety culture operating within optimal parameters.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The cloud-native machine learning pipeline successfully identified hidden cultural gaps and dynamically optimized the organizational food safety culture.")
else:
    st.info("Click 'Initialize Culture AI Engine' in the sidebar to simulate high-frequency behavioral data ingestion.")