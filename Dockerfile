FROM python:3.12.4

WORKDIR /app

COPY . .

# RUN pip3 install -U numpy matplotlib pandas scikit-learn scapy pyasn1
RUN pip3 install -U numpy matplotlib pandas scikit-learn streamlit