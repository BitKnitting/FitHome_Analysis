# FitHome Analysis
- FitHome Leaks   
    
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/BitKnitting/FitHome_Analysis/blob/master/notebooks/FitHome_Leaks.ipynb)

# Appliance Monitoring
We're exploring using Deep Learning to detect and monitor appliances.  A discussion of this is in the paper _[Neural NILM: Deep Neural Networks
Applied to Energy Disaggregation](https://arxiv.org/pdf/1507.06594.pdf)_ by Jack Kelly and William Knottenbelt.
# Exploration 1 - Microwave Detection
## Is the UK Dale Data  Right for Training?
The Question: _Given the data from house 2 of the UK Dale data, can we detect microwave activity on our home's electricity data?_
### Data from House 2
The article, _[AI in depth: monitoring home appliances from power readings with ML](https://cloud.google.com/blog/products/ai-machine-learning/monitoring-home-appliances-from-power-readings-with-ml)_, has made the data from House 2 [available for download](https://console.cloud.google.com/storage/browser/_details/gcp_blog/e2e_demo/processed_h2_appliance.csv).


- Get the data from 
