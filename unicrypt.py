import hashlib,random
badlist=[ord(i) for i in '[/\|*:?<>".']+[i for i in range(33)]
rnd=random.Random(1)

def tableforpass(password) -> list:
   seed=password
   for _i in range(50000):
      seed=hashlib.sha256(seed.encode()).hexdigest()
      rnd.seed(seed)
      rtable=rnd.sample([i for i in map(chr,range(1114112))],1114112)
      if len([i for i in badlist if ord(rtable[i]) in badlist])==0:
         for i_ in badlist:
            rtable[rtable.index(chr(i_))]=rtable[i_]
         return rtable

#####################################################################################

def enctext(password,text) -> str:
   rtable=tableforpass(password)
   pastxt=''
   for _t in text:
      pastxt+=rtable[ord(_t)]
   return pastxt
    
def dectext(password,text) -> str:
   rtable=tableforpass(password)
   plntxt=''
   for _t in text:
      plntxt+=chr(rtable.index(_t))
   return plntxt    

#############################################################################

if __name__=="__main__":
   while True:
      inp=input("""what you want to do:
         \r1. encrypt a text
         \r2. decrypt a text
         \r3. exit
         \r
         \r""")
      
      if inp=='1':
         inptxt=input("""
               \renter your text:
               \r""")
         inpass=input("""
               \renter the password:
               \r""")
         print("\nencrypted text:\n"+enctext(inpass,inptxt))
         
      if inp=='2':
         inptxt=input("""
               \renter your text:
               \r""")
         inpass=input("""
               \renter the password:
               \r""")
         print("\ndecrypted text:\n"+dectext(inpass,inptxt))
         
      if inp=='3':
         exit()
      print("\n")