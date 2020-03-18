# IMPORT TWO LIBRARIES 
# datatime include same time fuction like currenttime
# hashlib include algorithm of Sha256 
import datetime
i
mport hashlib
# we need only two classes.these are block and blockchain.
#defining the block 
class Block:
    #each block has got has 7 attributes 
    #these are blockNo,data,nest,nonce,previous_hash,timestamp
  
    blockNo = 0
    data = None
    next = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    #this function is construction
    def __init__(self, data):
        self.data = data

    #hash funchion convert to 256-bit
    def hash(self):
        
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()
      

    def __str__(self):
        #print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"