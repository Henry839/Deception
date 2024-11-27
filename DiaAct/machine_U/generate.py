def prompt_generate(self, context):
    """Prompt-based method

    Generate the machine belief and update it

    Args:
        context: context of the conversation

    Returns:
        response: machine belief

    Raises:
        ValueError: 1) Unknown build type of world
                    2) Invalid response from LLM
    """
#    prompt_template = ('Please analyze the belief state of the specific' 
#                       'character in the following text briefly: {}\n' 
#                       'Based on the context above, what does \'you\' know beforehand?'
#                       'Please start your brief analysis with "You know ..."')

    
    W_set = self.world.W_set
    build_type = self.world.build_type

    if build_type == "KG":
        # knowledge graph based belief
        context_prompt = ('Please analyze the belief state of your specific' 
                          f'character in the following text: {context}\n')
        self.machine_belief = {}
        for triple in W_set:
            triple_prompt = (f"Given the context above, do you deem the triple {triple} true?\n"
                             "Answer with 'yes' or 'no'.\n")
            full_prompt = context_prompt + triple_prompt
    
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
            response = self.model.chat(messages)
            if "yes" in response.lower():
                self.machine_belief[triple] = True
            elif "no" in response.lower():
                self.machine_belief[triple] = False
            else:
                raise ValueError(f"Invalid response: {response}")
    else:
        raise ValueError(f"Unknown world build type: {build_type}")



