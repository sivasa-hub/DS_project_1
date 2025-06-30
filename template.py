import os

# Define the full project structure as nested dictionary
project_structure = {
    "DS_Project_Workspace": {
        "ml_model": {
            ".vscode": ["settings.json"],
            "artifacts": ["models/", "logs/", "figures/", "results/", "checkpoints/"],
            "config": ["config.yaml", "logging.yaml"],
            "constants": ["project_constants.py"],
            "data": ["raw/", "interim/", "processed/", "external/"],
            "pipelines": [
                "data_pipeline.py", "training_pipeline.py",
                "evaluation_pipeline.py", "optimization_pipeline.py"
            ],
            "src": {
                "data": ["loader.py", "cleaner.py", "transformer.py", "splitter.py"],
                "features": ["engineering.py", "selectors.py"],
                "analysis": ["exploratory.py", "clustering.py", "statistical_tests.py"],
                "models": ["trainer.py", "evaluator.py", "optimizer.py", "checkpoint.py", "saver.py"],
                "utils": ["helpers.py", "logger.py", "validator.py"],
                "visualization": ["eda_plots.py", "result_plots.py", "dashboards.py"],
                "__init__.py": None
            },
            "tests": ["test_loader.py", "test_cleaner.py", "test_features.py", "test_models.py", "test_pipeline.py"],
            "requirements.txt": None,
            "environment.yml": None,
            "setup.py": None,
            "run.py": None
        },
        "backend_api": {
            ".vscode": ["settings.json"],
            "app": ["__init__.py", "main.py", "routes.py", "services.py", "schemas.py"],
            ".env": None,
            "requirements.txt": None,
            "README.md": None
        },
        "frontend_ui": {
            ".vscode": ["settings.json"],
            ".streamlit": ["config.toml"],
            "components": ["uploader.py", "display_result.py"],
            "assets": ["logo.png"],
            "app.py": None,
            ".env": None,
            "requirements.txt": None,
            "README.md": None
        },
        "notebooks": {
            ".vscode": ["settings.json"],
            "01_data_loading.ipynb": None,
            "02_data_exploration.ipynb": None,
            "03_data_cleaning.ipynb": None,
            "04_feature_engineering.ipynb": None,
            "05_data_clustering.ipynb": None,
            "06_data_analysis.ipynb": None,
            "07_model_training.ipynb": None,
            "08_model_evaluation.ipynb": None,
            "09_model_optimization.ipynb": None,
            "10_summary_and_conclusion.ipynb": None
        },
        "deployment": {
            "docker": ["Dockerfile", "docker-compose.yml"],
            "cloud": ["gcp_deploy.yaml", "aws_lambda_handler.py", "requirements.txt"],
            "README.md": None
        },
        "docs": [
            "system_architecture.md", "feature_plan.md", "data_dictionary.md",
            "model_experiments.md", "usage_guide.md", "changelog.md", "README_for_docs.md"
        ],
        "reports": {
            "figures": ["model_accuracy.png", "data_distribution.png"],
            "summary.md": None,
            "final_report.pdf": None
        },
        "ds_project_workspace.code-workspace": None
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        full_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(full_path, exist_ok=True)
            create_structure(full_path, content)
        elif isinstance(content, list):
            os.makedirs(full_path, exist_ok=True)
            for item in content:
                if item.endswith('/'):
                    os.makedirs(os.path.join(full_path, item.strip('/')), exist_ok=True)
                else:
                    open(os.path.join(full_path, item), 'a').close()
        else:
            if name.endswith('/'):
                os.makedirs(full_path, exist_ok=True)
            else:
                os.makedirs(base_path, exist_ok=True)
                open(full_path, 'a').close()

# Generate the structure in the temporary location
root_path = "Ds_PROJECT"
create_structure(root_path, project_structure)

root_path + "/DS_Project_Workspace"  # Return path for download or inspection