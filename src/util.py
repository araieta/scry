import configparser

def load_config(filepath):
    # Usa ExtendedInterpolation per supportare i riferimenti come ${Defaults:base_dir}
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read(filepath)
    return config