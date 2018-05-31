# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

from os import walk

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class ReadPoemSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(ReadPoemSkill, self).__init__(name="ReadPoemSkill")
        
        # Initialize working variables used within the skill.
        f = []
        self.p = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            f.extend(filenames)
            break
        for file in f:
            self.p.add(file.remove(".txt").replace("-", " "));


    @intent_handler(IntentBuilder("").require("Recite").op("Story").require("Poem"))
    def handle_read_poem_intent(self, message):
        poem = message.data.get("Poem")
        if p.contains(poem):
            self.file = poem.replace(" ", "-") + ".txt"
            self.speak_dialog("found.here")
        else:
            self.speak_dialog("not.found")

    def stop(self):
        return True

def create_skill():
    return TemplateSkill()
