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
    """
    def __init__(self, model):
        """Initialization.

        Args:
            model: LLM or language model
        """
        self.model = model

    def prompt_generate(self, context):
        """Prompt-based method

        Args:
            context: context of the conversation

        Returns:
            response: machine generated user belief
        """
        prompt_template = ('Please analyze the belief state of the' 
                           'specific character in the following text briefly: {}\n' 
                           'Based on the context above, what does the burglar' 
                           'know beforehand? Please start your brief analysis' 
                           'with "The burglar knows ..."')
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt_template.format(context)
            }
        ]
        response = self.model.chat(messages)
        return response

