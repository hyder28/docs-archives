from pathlib import Path

# files and folders
source_dir_name = Path("src/")
temp_dir_name = Path("tmp/")
output_dir_name = Path("output/")

dir_list = [source_dir_name, temp_dir_name, output_dir_name]

# model files
wav2vec2_model_dir = "models/wav2vec2-base-960h"
spacy_model_dir = "models/en_core_web_sm-3.4.0"

# keywords
keywords_dict = \
    {
        "PERSON": ["hyder", "ali"],
        "LOCATION": ["singapore", "eunos"]
    }
