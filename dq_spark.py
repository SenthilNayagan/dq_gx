from ruamel import yaml
import great_expectations as gx

data_context: gx.DataContext = gx.get_context()

datasource_config: dict = {
    "name": "my_datasource_name",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",

    # Uses Spark execution engine
    "execution_engine": {
        "class_name": "SparkDFExecutionEngine",
        "module_name": "great_expectations.execution_engine",
    },

    # We can add more Data Connectors to our configuration
    # For each Data Connector configuration, we will need to specify which type of Data Connector we will be using. 
    "data_connectors": {
        "name_of_my_inferred_data_connector": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "./data",
            "glob_directive": "*/*",
            "default_regex": {},
            # A dictionary of values that are passed to the Execution Engine's backend
            "batch_spec_passthrough": {
                "reader_method": "csv",
                "reader_options": {
                    "header": True,
                    "inferSchema": True,  # inferSchema will read datetime columns in as text columns
                },
            },
        }
    },
}

# Testing our configuration
data_context.test_yaml_config(yaml.dump(datasource_config))

# Adding our Datasource to our Data Context
#data_context.add_datasource(**datasource_config)

context = gx.get_context()
datasource = context.get_datasource("datasource_config")