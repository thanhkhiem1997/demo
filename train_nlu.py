# Imports
#-----------
# rasa nlu
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import feedparser
# Ham train NLU
#------------
def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')


# Tien hanh train modul NLU
# Input : File cauhoi.md
# Output: Model NLU trong thu mục models/nlu
train('data/nlu.md', 'config/config.yml', 'models/nlu')

# Load modul NLU
interpreter = Interpreter.load('./models/nlu/default/chat')

# Ham test NLU
def ask_question(text):
    print(interpreter.parse(text))


ask_question("mày làm được gì")
ask_question("mày tên gì")
ask_question("tạm biệt mày")
ask_question("cám ơn mày nha")
ask_question("chào mày nhé")


