import pickle
import torch
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
)


class TextCls:

    @staticmethod
    def htw_text_cls(data):
        """调用Bert微调模型, 进行文本分类"""
        if isinstance(data, str):
            data = [data]
        model_path = (
            "D:/code/DataWarehouse/03_代码/04_text_classifiacation/htw_bert_text_cls"
        )
        model = BertForSequenceClassification.from_pretrained(model_path)
        tokenizer = BertTokenizer.from_pretrained(model_path)
        with open(model_path + "/label_encoder.pkl", "rb") as f:
            loladed_le = pickle.load(f)
        predicitons = []
        for i in data:
            input = tokenizer(
                i, truncation=True, padding=True, max_length=50, return_tensors="pt"
            )
            output = model(**input)
            predict = [torch.argmax(output.logits).tolist()]
            predicitons.extend(loladed_le.inverse_transform(predict))

        return predicitons
