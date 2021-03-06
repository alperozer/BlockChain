from block import Block
class Blockchain:
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)
    block = Block("Genesis")
    head = block
    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
   
    
#initialize blockchain
blockchain = Blockchain()
#we say how many are there blocks (range is block number)
#mine 40 blocks
for n in range(40):
    blockchain.mine(Block("Block " + str(n+1)))
    

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next