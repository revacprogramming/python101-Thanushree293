

#def get_cs():
   # """get string input"""


#def cs_to_lot(cs):
    #"""convert connected string to list of strings"""


#def main():
   # cs = get_cs()

  #  lot = cs_to_lot(cs)
   # print(lot)


#if __name__ == '__main__':
  #  main()
def get_cs():
    st=input()
    return st
  
def cs_to_lot(cs):
    j=[]
    ll=cs.split(';')
    for i in ll:
       j.append(tuple(i.split('=')))
    return j

def main():
    cs = get_cs()
    lot=cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()