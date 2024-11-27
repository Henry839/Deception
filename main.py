from openai_api import openai_api
import json
from DiaAct import (MachineU, UserU, 
                    CondGenerator, WorldBuilder)


llm = openai_api("gpt-4o-mini",0)
world = WorldBuilder("KG")
user_U = UserU(llm, world)
machine_U = MachineU(llm, world)
cond_generator = CondGenerator(llm)

with open('./dataset/false_recommendation&false_label/dataset_json/base_orig.json', 'r', encoding='utf-8') as f_in:
    dataset = json.load(f_in)
f_in.close()

outputs = []
num_test = 10
i_sample = 0
for context in dataset['second_order_false_label_deception']:
    i_sample += 1
    user_belief = user_U.prompt_generate(context)
    machine_belief = machine_U.prompt_generate(context)
    machine_utterance = cond_generator.prompt_generate(context, 
                                                       user_belief, 
                                                       machine_belief)

    print(('[context: {}\n\n'
           '[burglar\'s belief]: {}\n\n'
           '[machine\'s belief]: {}\n\n'
           '[decision]: {}\n\n').format(context, user_belief, machine_belief, machine_utterance), flush=True)

    outputs.append({
        'context': context,
        'user_U': user_belief,
        'machine_U': machine_belief,
        'machine_utterance': machine_utterance
    })
    if i_sample >= num_test:
        break

with open('./Demo/outputs/output_0.json', 'w', encoding='utf-8') as f_out:
    json.dump(outputs, f_out, indent=4, ensure_ascii=False)
f_out.close()

