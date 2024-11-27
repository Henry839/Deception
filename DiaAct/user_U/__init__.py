"""User Belief

This module is used to generate user belief based on the
context of the conversation.
"""

class UserU():
    """Generate Machined Estimated User Belief.

    Using prompt based or learning based method to 
    generate User belief 

    Attributes:
        model: The language model used to generate machine belief
        world: The world model
        user_belief: The user belief. 
                     `dict` if world.build_type == "KG"

    """
    def __init__(self, 
                 model,
                 world):
        """Initialization.

        Args:
            model: LLM or language model
        """
        self.model = model
        self.world = world
        self.user_belief = None

    from .generate import prompt_generate


