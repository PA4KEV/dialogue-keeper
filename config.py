import yaml

button_mappings = {
    "nina": {"mapped_buttons": {"0"}, "value": 0,},
    "deborah": {"mapped_buttons": {"1"}, "value": 1,},
    "silvia": {"mapped_buttons": {"2"}, "value": 2,},
    "remora": {"mapped_buttons": {"3"}, "value": 3,},
}

def load_config() -> bool:
    with open("config.yaml", 'r') as config_file:
        try:
            config_data = yaml.safe_load(config_file)
            map_buttons(config_data)
            return True
        except yaml.YAMLError as exc:
            # log an error
            return False

def map_buttons(config_data: dict):
    dialogue_choices = config_data["button_maps"]["dialogue_choices"]
    for button_map in button_mappings.keys():
        button_mappings[button_map]["mapped_buttons"].add(
            dialogue_choices[button_map].upper()
            )

