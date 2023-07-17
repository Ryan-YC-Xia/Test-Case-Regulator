import sys
import time

from prompt import Prompt

MODEL_PATH = sys.argv[1]
RESP_PATH = sys.argv[2]
CASE_PATH = sys.argv[3]


def main():
    from transformers import AutoTokenizer, AutoModel

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).half().cuda()
    model = model.eval()

    with open(CASE_PATH, "r", encoding="utf-8") as case_file:
        cases = case_file.readlines()

    case_no = 0
    for case in cases:
        t0 = time.time()
        case_no += 1

        prompt = Prompt.regulate_case(case)
        response, history = model.chat(tokenizer, prompt, history=[])
        response_path = RESP_PATH + "response_original_case_" + str(case_no) + ".txt"
        with open(response_path, "w", encoding="utf-8") as response_file:
            response_file.write(response)
            print("Case " + str(case_no) + " original response written to file.")

        t1 = time.time()
        print("Case " + str(case_no) + " took: ", round(t1 - t0, 2), " seconds")

    print("Job Finished.")


if __name__ == "__main__":
    main()
