# code_credits: https://medium.com/ai-quest/pre-trained-language-model-in-any-language-7531ea7217d4


from fastai import *
from fastai.text import *
from nlputils import split_wiki, get_wiki

bs = 128
data_path = Config.data_path()

lang = 'es'
name = f'{lang}wiki'
path = data_path/name
#path.mkdir(exist_ok=True, parents=True)
lm_fns = [f'{lang}_wt', f'{lang}_wt_vocab']

get_wiki(path, lang)
dest = split_wiki(path, lang)
