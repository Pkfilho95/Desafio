from datetime import datetime

def extract_date(element):
    return datetime.strptime(element[0], '%Y-%m-%d')

def reconcile_accounts(transactions1, transactions2):

    for t1 in transactions1:
        matches = [t2 for t2 in transactions2 if t1[1:] == t2[1:]] 
        
        if not matches:
            t1.append('MISSING')
        
        else:
            matches = sorted(matches, key=extract_date)
            t1.append('FOUND')
            transactions2[transactions2.index(matches[0])].append('FOUND')
    
    for t2 in transactions2:
        if len(t2) != 5:
            t2.append('MISSING')

    return (transactions1, transactions2)