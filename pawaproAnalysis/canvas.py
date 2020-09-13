class Canvas:
    message={'left':'','right':''}

    @classmethod
    def store(cls,message_side,new_message):
        cls.message[message_side]+=new_message+'\n'

    @classmethod
    #TODO　パネルが増えても大丈夫なようにする
    def show(cls):
        shown_message=''
        num_line={'left':0,'right':0}
        num_line['left']=cls.message['left'].count('\n')
        num_line['right']=cls.message['right'].count('\n')
        splited_message={'left':[],'right':[]}
        splited_message['left']=cls.message['left'].split('\n')
        splited_message['right']=cls.message['right'].split('\n')

        if  num_line['left']>= num_line['right']:
            longer_line_num=num_line['left']
            for i in range(num_line['left'] - num_line['right']):
                splited_message['right'].append('')

        else:
            longer_line_num=num_line['right']
            for i in range(num_line['right'] - num_line['left']):
                splited_message['left'].append('')

        for s in splited_message['left']:
            s.ljust(50,'t')
        
        for i in range(longer_line_num):
            shown_message+=splited_message['left'][i]+ '  '+ splited_message['right'][i]+'\n'
    

        cls.clear_message()
        return shown_message

    @classmethod
    def clear_message(cls):
        cls.message={'left':'','right':''}
