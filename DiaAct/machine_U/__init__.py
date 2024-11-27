"""Machine Belief

This module is used to generate machine belief based on the context of the conversation.
"""

class MachineU():
    """Generate Machine Belief.

    Using prompt based or learning based method to 
    generate machine belief

    Attributes:
        model: The language model used to generate machine belief
        world: The world model
        machine_belief: The machine belief. 
                        `dict` if world.build_type == "KG"

    """
    def __init__(self, 
                 model,
                 world):
        """Initialization

        Args:
            model: LLM or language model
            world: the world model, containing the full set W

        """
        self.model = model 
        self.world = world
        self.machine_belief = None


    from .generate import prompt_generate

