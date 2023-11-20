from setuptools import setup, find_packages

setup(
    name="dynaflow-plugin",
    version="0.0.1",
    description="DynamoDB plugin for MLflow",
    packages=find_packages(),
    # Require MLflow as a dependency of the plugin, so that plugin users can simply install
    # the plugin & then immediately use it with MLflow
    install_requires=["pynamodb", "mlflow"],
    entry_points={
        # Define a Tracking Store plugin for tracking URIs with scheme 'file-plugin'
        "mlflow.tracking_store": "dynamodb=dynaflow.tracking_store:DynamodbTrackingStore",
    },
)