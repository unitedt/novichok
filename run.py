import json
import logging
from kutana import Kutana, load_plugins, logger
from kutana.backends import Vkontakte

# Import configuration
with open("config.json") as fh:
    config = json.load(fh)
    
# Log level
logger.set_logger_level(logging.DEBUG)

# Create application
app = Kutana()

# Add manager to application
app.add_backend(Vkontakte(token=config["vk_token"]))

# Load and register plugins
app.add_plugins(load_plugins("plugins/"))

if __name__ == "__main__":
    # Run application
    app.run()
