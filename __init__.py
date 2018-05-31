# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

from os import walk
from os.path import dirname
__author__ = "Stuin"

LOGGER = getLogger(__name__)

class ReadPoemSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(ReadPoemSkill, self).__init__(name="ReadPoemSkill")

        # Initialize working variables used within the skill.
    def make_list(self):
        f = []
        self.p = []
        path = dirname(__file__)+"/Poems"
        for (dirpath, dirnames, filenames) in walk(path):
            f.extend(filenames)
            break
        for file in f:
            file = file[:-4]
            self.p.append(file.replace("-", " "))

    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        intent = IntentBuilder("PoemIntent"). \
            require("Recite").require("Poem").build()
        self.register_intent(intent, self.handle_read_poem_intent)

    #@intent_handler(IntentBuilder("PoemIntent").require("Recite").require("Poem"))#.op("Story"))
    def handle_read_poem_intent(self, message):
        self.speak_dialog("found")
        poem = message.data.get("Poem")

        if self.p.contains(poem):
            self.file = poem.replace(" ", "-") + ".txt"
            self.speak_dialog("found")
        else:
            self.speak_dialog("not.found")

    def stop(self):
        pass

def create_skill():
    return ReadPoemSkill()
