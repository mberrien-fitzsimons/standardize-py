# Python Project Template

This template is based on the [DSSG machine learning pipeline](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow). 

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── conf
│   ├── base           <- Space for shared configurations like parameters
│   └── local          <- Space for local configurations, usually credentials
│
├── data
│   ├── 01_raw         <- Imutable input data
│   ├── 02_intermediate<- Cleaned version of raw
│   ├── 03_processed   <- The data used for modelling
│   ├── 04_models      <- trained models
│   ├── 05_model_output<- model output
│   └── 06_reporting   <- Reports and input to frontend
│
├── docs               <- Space for Sphinx documentation
│
├── notebooks          <- Jupyter notebooks. Naming convention is date YYYYMMDD (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `20190601-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── results            <- Intermediate analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── .gitignore         <- Avoids uploading data, credentials, outputs, system files etc
│
└── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── d00_utils      <- Functions used across the project
    │   └── remove_accents.py
    │
    ├── d01_data       <- Scripts to reading and writing data etc
    │   └── load_data.py
    │
    ├── d02_intermediate<- Scripts to transform data from raw to intermediate
    │   └── create_int_payment_data.py
    │
    ├── d03_processing <- Scripts to turn intermediate data into modelling input
    │   └── create_master_table.py
    │
    ├── d04_modelling  <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   └── train_model.py
    │
    ├── d05_model_evaluation<- Scripts that analyse model performance and model selection
    │   └── calculate_performance_metrics.py
    │    
    ├── d06_reporting  <- Scripts to produce reporting tables
    │   └── create_rpt_payment_summary.py
    │
    └── d07_visualisation<- Scripts to create frequently used plots
        └── visualise_patient_journey.py
```
