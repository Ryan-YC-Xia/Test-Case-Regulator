import json


class Prompt:
    def regulate_case(case):
        content = []
        content.append("请以专业测试工程师的角度,把不规范的测试用例转化为规范的形式,并以json的文件格式返回。以下是几个例子: \n")
        with open("example_regulations_b.json", encoding="utf-8") as f:
            content.extend(f.readlines())
        content.append("\n现在把这个不规范的测试用例转化为规范的形式:")
        content.append('"' + case + '"\n')
        content.append("注意要把它分成前置条件，操作步骤，预期结果三个部分。")
        content.append("使用标准化的语言。不要输出除了json格式文件以外的任何内容。")
        return "".join(content)
