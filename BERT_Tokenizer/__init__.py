import BRET_Tokenizer

def sample1():
    BRT_TKN =BRET_Tokenizer.Bert_Tokenizer_basic("where is Himalayas in the world map?")
    X,Y =BRT_TKN.sample_Tokenizing()
    print(X)
    print(Y)
def sample2():
    BRT_TKN2 =BRET_Tokenizer.Bert_Tokenizer_basic("where is Himalayass in the world map?")
    X1,Y1=BRT_TKN2.sample_Tokenizing()
    print(X1)
    print(Y1)
def Question_AnswerEncoding():
    q1 = 'Who was Tony Stark?'
    c1 = 'Anthony Edward Stark known as Tony Stark is a fictional character in Avengers'
    BRT_TKN2 =BRET_Tokenizer.Bert_Tokenizer_basic("ignore")
    print(BRT_TKN2.question_Answer(q1,c1))
    print(BRT_TKN2.question_Answer_(q1,c1))
def Question_Answer_Multiple():
    q1 = 'Who was Tony Stark?'
    c1 = 'Anthony Edward Stark known as Tony Stark is a fictional character in Avengers'
    q2 = 'Who was Tony in Marvel'
    c2 = 'Tony Stark is a fictional character in Marvel Avengers'
    BRT_TKN2 =BRET_Tokenizer.Bert_Tokenizer_basic("ignore")
    print(BRT_TKN2.question_Answer_Two(q1,c1,q2,c2))
def DistilBertTokenizer_Example():

    q1 = 'Who was Tony Stark?'
    c1 = 'Anthony Edward Stark known as Tony Stark is a fictional character in Avengers'
    q2 = 'Who was Tony in Marvel'
    c2 = 'Tony Stark is a fictional character in Marvel Avengers'
    BRT_TKN2 =BRET_Tokenizer.Bert_Tokenizer_basic("ignore")
    print(BRT_TKN2.DistilBertTokenizer_Example(q1,c1,q2,c2))


#sample1()
#sample2()
#Question_AnswerEncoding()
#Question_Answer_Multiple()
DistilBertTokenizer_Example()