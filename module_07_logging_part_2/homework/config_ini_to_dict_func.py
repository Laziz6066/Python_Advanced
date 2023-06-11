import configparser


def ini_to_dict(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    result = {'version': 1, 'disable_existing_loggers': False}

    for section in config.sections():
        section_config = {}
        for option in config.options(section):
            value = config.get(section, option)
            if value.isdigit():
                value = int(value)
            section_config[option] = value
        result[section] = section_config

    return result


# Usage example
config_dict = ini_to_dict('logging.ini')
