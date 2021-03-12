# Automated Log File Analysis Framework (ALFAF)

The ALFAF is a robust, end-to-end pipeline for performing automated log files analysis for the purposes of identifying failures from generated system log files.

Two processing stages are implemented:
1. Log parsing - transforming raw, unstructured log files into a structured dataset. Implemented by the Data Miner available at: [https://github.com/tyronevb/data_miner](https://github.com/tyronevb/data_miner)
2. Log File Analysis Anomaly Detection - using the structured dataset to train models representative of system execution and then using these models to identify failures and anomalous events from log files. Implemented by the Inference Engine available at: [https://github.com/tyronevb/inference_engine](https://github.com/tyronevb/inference_engine)
