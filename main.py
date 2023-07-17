import os
import shutil

from prompt import Prompt

MODEL_PATH = "../../../../hy-tmp/chatglm-6b"
Responses_PATH = "./Test/Responses/"

from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).half().cuda()
model = model.eval()

with open("./Test/cases.txt", "r", encoding="utf-8") as case_file:
    cases = case_file.readlines()

shutil.rmtree(Responses_PATH)
os.makedirs(Responses_PATH)

case_no = 0
for case in cases:
    case_no += 1
    prompt = Prompt.regulate_case(case)
    response, history = model.chat(tokenizer, prompt, history=[])
    response_path = Responses_PATH + "response_" + str(case_no) + ".txt"
    with open(response_path, "w", encoding="utf-8") as response_file:
        response_file.write(response)
    print("Case " + str(case_no) + " response written to file.")

print("Job Finished.")
