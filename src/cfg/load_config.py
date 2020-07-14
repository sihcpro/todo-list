import importlib.util


class Config:
    module_config: dict = {}

    def __init__(self, module_name="BAS"):
        self.module_name = module_name
        self.defaults = None
        self.defaults = self.loadFileConfig("./src/cfg/defaults.py")

    def loadFileConfig(self, file_config_path):
        def _loadConfig(_file):
            config = {}
            for key, value in _file.__dict__.items():
                key_upper = key.upper()
                if (
                    self.defaults is not None
                    and key_upper not in self.defaults
                ):
                    continue
                config[key_upper] = value
            return config

        spec = importlib.util.spec_from_file_location(
            self.module_name, file_config_path
        )
        file_config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(file_config)

        config = _loadConfig(file_config)
        self.module_config.update(config)
        return self.module_config

    def loadConfig(self, env):
        file_config_path = f"./env/{env}/config.py"
        self.loadFileConfig(file_config_path)
        return self.module_config

    def __getattr__(self, value):
        return self.module_config[value]
