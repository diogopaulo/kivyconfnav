import configparser


Config = configparser.ConfigParser()
Config.read("conf.conf")


def get_config(section, name):
    try:
        return Config[section][name]
    except:
        return None


def config_section_map(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1