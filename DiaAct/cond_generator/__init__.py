"""Utterance generator

Performing specific dialogue act based on user U and 
machine U, which is some conditional generation method
"""

class CondGenerator():
    """Conditional Generation

    Using prompt based or learning based method to 
    generate utternace 

    Attributes:
        model: The language model used to generate machine belief
    """

    def __init__(self, model):
        """Initialization.

        Args:
            model: LLM or language model
        """
        self.model = model

    def prompt_generate(self, user_U, machine_U, context):
        """Prompt-based method

        Args:
            user_U: user belief state
            machine_U: machine belief state
            context: context of the conversation

        Returns:
            response: generated utterance
        """

        prompt_template = ('1. Question background: {}\n'
                           '2. Your opponent\'s belief state: {}\n'
                           '3. Your belief state: {}\n'
                           'Please consider the Question background, '
                           'the opponent\'s belief state, and your belief state' 
                           'to provide your final choice to prevent the opponent\'s theft.').format(context, user_U, machine_U)
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt_template
            }
        ]
        response = self.model.chat(messages)
        return response

