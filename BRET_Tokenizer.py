from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
class Bert_Tokenizer_basic:
    def sample_Tokenizing(self):    
        encoding=tokenizer.encode(self.text)
        tockens = tokenizer.convert_ids_to_tokens(encoding)
        return encoding,tockens
    def question_Answer(self,question,answer):
        items=[]
        encoding=tokenizer.encode_plus(question,answer ,padding=True)
        for key ,value in encoding.items():
             items.append( (key , value))
        return items
    def question_Answer_(self,question,answer):
        items=[]
        encoding=tokenizer(question,answer ,padding=True)
        for key ,value in encoding.items():
             items.append( (key , value))
        return items

    def question_Answer_Two(self,question1,answer1,question2,answer2):
        items=[]
        encoding=tokenizer([question1,question2],[answer1,answer2] ,padding=True)
        for key ,value in encoding.items():
             items.append( (key , value))
        return items
    def DistilBertTokenizer_Example(self,question1,answer1,question2,answer2):
        from transformers import DistilBertTokenizer
        items=[]
        tokenizer= DistilBertTokenizer.from_pretrained('bert-base-uncased')
        encoding=tokenizer([question1,question2],[answer1,answer2] ,padding=True)
        for key ,value in encoding.items():
             items.append( (key , value))
        return items





    def __init__(self,text) -> None:
        self.text=text
    
    






