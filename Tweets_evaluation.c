punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(str):
    new_str = str 
    for elem in punctuation_chars:
        new_str = new_str.replace(elem,'')
    return new_str
def get_neg(string):
    string = string.lower()
    l_str = string.split()
    count = 0
    for elem in l_str:
         if strip_punctuation(elem) in negative_words:
            count += 1 
    return str(count)        
def get_pos(string):
    string = string.lower()
    l_str = string.split()
    count = 0
    for elem in l_str:
         if strip_punctuation(elem) in positive_words:
            count += 1 
    return str(count)        
wrfile = open('resulting_data.csv', 'w')
wrfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
with open ('project_twitter_data.csv') as rfile:
    for lin in rfile.readlines()[1:]:
        lst_tw_str = lin.split(',')
        tweet = lst_tw_str[0]
        retweet = lst_tw_str[1].strip()
        replies = lst_tw_str[2].strip()
        pos = get_pos(tweet)
        neg = get_neg(tweet)
        net_sc = str(int(pos) - int(neg))
        wrfile.write(retweet+', '+replies+', '+ pos +', '+ neg +', '+ net_sc +'\n')
     