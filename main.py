from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TextClassificationPipeline
from transliterate import translit

model_path = './mymodel'

tokenizer = AutoTokenizer.from_pretrained(f'{model_path}', local_files_only=True)

model = AutoModelForSequenceClassification.from_pretrained(model_path, num_labels=2)

nlp = TextClassificationPipeline(model=model, tokenizer=tokenizer)


while True:
    name = input('Enter name: ')

    tran = translit(name, language_code='ru', reversed=True)

    result = nlp(tran)

    print(result)
