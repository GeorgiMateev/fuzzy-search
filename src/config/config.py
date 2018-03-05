import yaml


class Config:
    secrets = None

    @staticmethod
    def get_secrets():
        if Config.secrets:
            return Config.secrets

        with open("../secrets.yml", 'r') as yml_file:
            cfg = yaml.load(yml_file)
            Config.secrets = cfg
            return cfg
