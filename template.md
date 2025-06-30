DS_Project_1/
├── .gitignore
├── README.md
├── ds_project_workspace.code-workspace

├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── ISSUE_TEMPLATE/
│       └── bug_report.md

├── ml_model/                     ← Conda env: ds_env_ml
│   ├── .vscode/
│   │   └── settings.json
│   ├── artifacts/
│   │   ├── models/
│   │   ├── logs/
│   │   ├── figures/
│   │   ├── results/
│   │   └── checkpoints/
│   ├── config/
│   │   ├── config.yaml
│   │   └── logging.yaml
│   ├── constants/
│   │   └── project_constants.py
│   ├── data/
│   │   ├── raw/
│   │   ├── interim/
│   │   ├── processed/
│   │   └── external/
│   ├── pipelines/
│   │   ├── data_pipeline.py
│   │   ├── training_pipeline.py
│   │   ├── evaluation_pipeline.py
│   │   └── optimization_pipeline.py
│   ├── src/
│   │   ├── __init__.py
│   │   ├── data/
│   │   │   ├── loader.py
│   │   │   ├── cleaner.py
│   │   │   ├── transformer.py
│   │   │   └── splitter.py
│   │   ├── features/
│   │   │   ├── engineering.py
│   │   │   └── selectors.py
│   │   ├── analysis/
│   │   │   ├── exploratory.py
│   │   │   ├── clustering.py
│   │   │   └── statistical_tests.py
│   │   ├── models/
│   │   │   ├── trainer.py
│   │   │   ├── evaluator.py
│   │   │   ├── optimizer.py
│   │   │   ├── checkpoint.py
│   │   │   └── saver.py
│   │   ├── utils/
│   │   │   ├── helpers.py
│   │   │   ├── logger.py
│   │   │   └── validator.py
│   │   └── visualization/
│   │       ├── eda_plots.py
│   │       ├── result_plots.py
│   │       └── dashboards.py
│   ├── tests/
│   │   ├── test_loader.py
│   │   ├── test_cleaner.py
│   │   ├── test_features.py
│   │   ├── test_models.py
│   │   └── test_pipeline.py
│   ├── requirements.txt
│   ├── environment.yml
│   ├── setup.py
│   └── run.py

├── backend_api/                  ← venv: venv_api
│   ├── venv_api/
│   ├── .vscode/
│   │   └── settings.json
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── services.py
│   │   └── schemas.py
│   ├── .env
│   ├── requirements.txt
│   └── README.md

├── frontend_ui/                  ← venv: venv_ui
│   ├── venv_ui/
│   ├── .vscode/
│   │   └── settings.json
│   ├── app.py
│   ├── components/
│   │   ├── uploader.py
│   │   └── display_result.py
│   ├── assets/
│   │   └── logo.png
│   ├── .env
│   ├── .streamlit/
│   │   └── config.toml
│   ├── requirements.txt
│   └── README.md

├── notebooks/                   ← Uses Conda: ds_env_ml
│   ├── .vscode/
│   │   └── settings.json
│   ├── 01_data_loading.ipynb
│   ├── 02_data_exploration.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_data_clustering.ipynb
│   ├── 06_data_analysis.ipynb
│   ├── 07_model_training.ipynb
│   ├── 08_model_evaluation.ipynb
│   ├── 09_model_optimization.ipynb
│   └── 10_summary_and_conclusion.ipynb

├── deployment/
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   ├── cloud/
│   │   ├── gcp_deploy.yaml
│   │   ├── aws_lambda_handler.py
│   │   └── requirements.txt
│   └── README.md

├── docs/
│   ├── system_architecture.md
│   ├── feature_plan.md
│   ├── data_dictionary.md
│   ├── model_experiments.md
│   ├── usage_guide.md
│   ├── changelog.md
│   └── README_for_docs.md

├── reports/
│   ├── summary.md
│   ├── final_report.pdf
│   └── figures/
│       ├── model_accuracy.png
│       └── data_distribution.png