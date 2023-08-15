# Overview

TL;DR
A simple Python GCP Cloud Function that pulls stock data from https://alpaca.markets and publishes results to Google Cloud PubSub.

This project was built to demonstrate a straight forward and low cost option for ingesting application data for analytics.

An example Alpaca API response is shown below. The cloud function selects all attributes and writes to a predefined PubSub topic.

```json
{
  "symbol": "GOOG",
  "trade": {
    "t": "2022-11-22T19:52:11.744989347Z",
    "x": "V",
    "p": 97.18,
    "s": 300,
    "c": ["@"],
    "i": 3171,
    "z": "C"
  }
}
```

# API Ingestion

Application data is frequently exposed via APIs for integration. Frameworks like REST make _app-to-app_ integration and microservice architectures extremely simple; however, they pose a challenge for analytics teams relying on low code integration tools such as Alteryx, Azure Data Factory, Informatica, and Google Data Fusion.

A serverless function can often bridge this gap and provide teams of analysts and data scientst a simple approach to ingesting application data for analytics.

This repo contains Python code used to ingest data from an open REST API and publish results to Google PubSub for downstream consumption. For this project the a BigQuery subscription type was used to stream the results into BigQuery.A BigQuery subscription in PubSub autmatically and effeciently streams data into BigQuery via the Storage API as messages are published.

# Setup

This project includes a yaml file for deployment to Google Cloud using Github Actions maintained here: https://github.com/google-github-actions/deploy-cloud-functions. The Github Action Workflow requires several _"Action Secrets"_ used to set environment variables during deployment. Set the following secrets in the repository before deployment.

| Action Secret  | Value                                                          |
| -------------- | -------------------------------------------------------------- |
| KEY_ID         | Alpaca API Key ID Issued _(authenticate to data source)_       |
| SECRET_KEY     | Alpaca API Secret Key ID                                       |
| PROJECT_ID     | GCP Project ID where Topic is deployed                         |
| TOPIC_ID       | GCP PubSub Topic                                               |
| GCP_PROJECT_ID | GCP Project ID where Function will be deployed                 |
| GCP_SA_KEY     | Service Account Key used to authenticate GitHub to GCP Project |
