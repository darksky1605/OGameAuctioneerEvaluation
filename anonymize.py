#!/usr/bin/python

import json
import sys

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print "Usage:", sys.argv[0], "records.txt output.json"
        sys.exit(0)
        
    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2] 
    
    with open(inputfilename, "r") as f:
        auctions = json.load(f)
        
    with open(outputfilename, "w") as f:
        for index, a in enumerate(auctions):
            a["auctionId"] = str(index)
            a["serverId"] = a["serverId"][a["serverId"].find("-")+1:]
            playerids = list(set([bid["playerId"] for bid in a["bids"]]))
            #playernames = list(set([bid["playerName"] for bid in a["bids"]]))
            #print str(playerids)
            #print str(playernames)
            for bid in a["bids"]:
            #    print bid["playerId"], bid["playerName"], playerids.index(bid["playerId"])
                val = str(playerids.index(bid["playerId"]))
                bid["playerId"] = val
                bid["playerName"] = val
            
        json.dump(auctions, f, indent=2)
