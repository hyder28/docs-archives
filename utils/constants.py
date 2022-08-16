from pathlib import Path

# files and folders
source_dir_name = Path("src/")
temp_dir_name = Path("tmp/")
output_dir_name = Path("output/")

dir_list = [source_dir_name, temp_dir_name, output_dir_name]

# model files
wav2vec2_model_dir = "models/wav2vec2-large-960h"
spacy_model_dir = "models/en_core_web_sm-3.4.0"

# keywords
keywords_lookup = \
    {
        "PEOPLE N MANAGEMENT": ["Sergio Mattarella", "Mario Draghi", "Piyush Gupta", "John Olds"],
        "TECHNOLOGY": ["Bitcoins", "CPF Investment Account"],
        "AWARDS": ["World's Best Investment Banks", "World's Best Bank"],
        "BU/SU": ["CBG", "Consume Bank"]
    }
