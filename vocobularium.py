import datetime
import pickle
 
class wt:
    def __init__(self,w="",t=""):
        self.word = w
        self.translate = t
        self.list_of_success = [0 for i in range(10)]
        self.last_time_learn = datetime.datetime.now()
        
        
  
    
    def update_word_status(self,answer_correctness):
        self.list_of_success.pop(0)
        self.list_of_success.append(int(answer_correctness))
        self.last_time_learn = datetime.datetime.now()
    
    def get_time_from_last_repeat(self):
        present=datetime.datetime.now()
        past=self.last_time_learn
        result=present-past
        #print(result.seconds//60)
        return result.seconds//60
         
    def get_word_successness(self):
        #print(sum(self.list_of_success)/10)
        return sum(self.list_of_success)/10
        
    def get_word_mark(self):
        r=(1.01 - self.get_word_successness())*self.get_time_from_last_repeat()
        return r
    
    def print(self):
        print(self.word,' : ', self.translate,".time:",self.get_time_from_last_repeat(),",succ:",self.get_word_successness(),",mark:",self.get_word_mark() )
        
    def print_word(self):
        print(self.word)
    
    def print_translate(self):
        print(self.translate)
        

def create_list_of_id(num,words):
    r=[0]
    result=[]
    for i in range(len(words)):
        mark=words[i].get_word_mark()
        if  len(r)<num or mark>min(r): # it's equal to len(r)<num or (len(r)==num and mark>min(r)):
            r.append(mark)
        if len(r)>num:
            r.remove(min(r))
            
    for i in range(len(words)):
        if words[i].get_word_mark() in r:
            result.append(i)
        if len(result)==num:
            break
    
    return result
        
def dump_vocobularic(voc,path=""):
    with open(path+'vocobularic_data.pkl', 'wb') as output:
        for obj in voc:
            pickle.dump(obj,output,pickle.HIGHEST_PROTOCOL)


def pickled_items(filename):
    """ Unpickle a file of pickled data. """
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break
            
def open_vocobularic(path=""):
    words=[]
    for obj in pickled_items(path+'vocobularic_data.pkl'):
        words.append(obj)
    return words


        
        






        
