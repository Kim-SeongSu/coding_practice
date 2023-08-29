def solution(new_id):
    import re
    
    ID = new_id.lower()
    ID = re.sub('[^a-z0-9\-_.]', '', ID)
    ID = re.sub('\.+', '.', ID)							
    ID = re.sub('^[.]|[.]$', '', ID)						
    ID = 'a' if ID == '' else ID[:15]					
    ID = re.sub('^[.]|[.]$', '', ID)		
    ID = ID if len(ID) > 2 else ID+ID[-1]*(3-len(ID))
    return ID