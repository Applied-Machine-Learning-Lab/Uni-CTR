from transformers import AutoModel


# 计算整个模型参数大小
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


nlp_model = AutoModel.from_pretrained("huawei-noah/TinyBERT_General_4L_312D", output_hidden_states=True)
print(nlp_model)
# print(count_parameters(nlp_model))

# nlp_model = AutoModel.from_pretrained("bert-base-uncased", output_hidden_states=True)
# # print(nlp_model)
# print(count_parameters(nlp_model))
#
# nlp_model = AutoModel.from_pretrained("microsoft/deberta-v3-large", output_hidden_states=True)
# # print(nlp_model)
# print(count_parameters(nlp_model))
#
# nlp_model = AutoModel.from_pretrained("princeton-nlp/Sheared-LLaMA-1.3B", output_hidden_states=True)
# # print(nlp_model)
# print(count_parameters(nlp_model))
