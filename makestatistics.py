#!/usr/bin/python

import json
import sys
from datetime import datetime, timedelta
import numpy as np 
from collections import defaultdict


def getItemName(uuid):
    itemnames = {}
    
    itemnames["de922af379061263a56d7204d1c395cefcfb7d75".upper()] = "+10% Met Booster"    
    itemnames["ba85cc2b8a5d986bbfba6954e2164ef71af95d4a".upper()] = "+20% Met Booster"
    itemnames["05294270032e5dc968672425ab5611998c409166".upper()] = "+30% Met Booster"
    itemnames["3c9f85221807b8d593fa5276cdf7af9913c4a35d".upper()] = "+10% Crys Booster"
    itemnames["422db99aac4ec594d483d8ef7faadc5d40d6f7d3".upper()] = "+20% Crys Booster"    
    itemnames["118d34e685b5d1472267696d1010a393a59aed03".upper()] = "+30% Crys Booster"
    itemnames["d9fa5f359e80ff4f4c97545d07c66dbadab1d1be".upper()] = "+10% Deut Booster"
    itemnames["e4b78acddfa6fd0234bcb814b676271898b0dbb3".upper()] = "+20% Deut Booster"
    itemnames["5560a1580a0330e8aadf05cb5bfe6bc3200406e2".upper()] = "+30% Deut Booster"
    itemnames["da4a2a1bb9afd410be07bc9736d87f1c8059e66d".upper()] =  "NEWTRON Bronze"
    itemnames["d26f4dab76fdc5296e3ebec11a1e1d2558c713ea".upper()] =  "NEWTRON Silver"
    itemnames["8a4f9e8309e1078f7f5ced47d558d30ae15b4a1b".upper()] =  "NEWTRON Gold"
    itemnames["40f6c78e11be01ad3389b7dccd6ab8efa9347f3c".upper()] =  "KRAKEN Bronze"
    itemnames["4a58d4978bbe24e3efb3b0248e21b3b4b1bfbd8a".upper()] =  "KRAKEN Silver"
    itemnames["929d5e15709cc51a4500de4499e19763c879f7f7".upper()] =  "KRAKEN Gold"
    itemnames["d3d541ecc23e4daa0c698e44c32f04afd2037d84".upper()] =  "DETROID Bronze"
    itemnames["27cbcd52f16693023cb966e5026d8a1efbbfc0f9".upper()] =  "DETROID Silver"
    itemnames["0968999df2fe956aa4a07aea74921f860af7d97f".upper()] =  "DETROID Gold"
    itemnames["16768164989dffd819a373613b5e1a52e226a5b0".upper()] =  "+4 Planet Fields"
    itemnames["0e41524dc46225dca21c9119f2fb735fd7ea5cb3".upper()] =  "+9 Planet Fields"
    itemnames["04e58444d6d0beb57b3e998edc34c60f8318825a".upper()] = "+15 Planet Fields"
    itemnames["be67e009a5894f19bbf3b0c9d9b072d49040a2cc".upper()] =  "+2 Moon Fields"
    itemnames["c21ff33ba8f0a7eadb6b7d1135763366f0c4b8bf".upper()] =  "+4 Moon Fields"
    itemnames["05ee9654bd11a261f1ff0e5d0e49121b5e7e4401".upper()] =  "+6 Moon Fields"
    itemnames["485a6d5624d9de836d3eb52b181b13423f795770".upper()] =  "42h M.O.O.N.S."
    itemnames["fd895a5c9fd978b9c5c7b65158099773ba0eccef".upper()] =  "18h M.O.O.N.S."
    itemnames["45d6660308689c65d97f3c27327b0b31f880ae75".upper()] =  "1h M.O.O.N.S."
    itemnames["cb4fd53e61feced0d52cfc4c1ce383bad9c05f67".upper()] = "50% Building Time Reduction"
    itemnames["14c17d49462963f5e5b67efa1257622ce1b866ac".upper()] = "50% Research Time Reduction"
    itemnames["75accaa0d1bc22b78d83b89cd437bdccd6a58887".upper()] = "50% Shipyard Time Reduction"
    itemnames["78badde414b2cba7c0c37e3e11a5a42e8414c8ac".upper()] = "Geologist"
    itemnames["10662141326cc46ee30bc4dd05f581424050a768".upper()] = "Commander"
    itemnames["bbc7ee322189528ad5bc3a19e048c4ff582538b5".upper()] = "Admiral"
    itemnames["ddb65e18ec97b32d7dc50249a0d9c256f57664df".upper()] = "Technocrat"
    itemnames["e8e01fb84ed1a33ed3ab34af6fc84e86e3505142".upper()] = "Engineer"
    itemnames["090a969b05d1b5dc458a6b1080da7ba08b84ec7f".upper()] = "10% Crys Booster (Buddy)"
    itemnames["b956c46faa8e4e5d8775701c69dbfbf53309b279".upper()] = "10% Met Booster (Buddy)"
    itemnames["e254352ac599de4dd1f20f0719df0a070c623ca8".upper()] = "10% Deut Booster (Buddy)"
    itemnames["67d6041bc0206d1ec7ce667e51f9d7ba73314604".upper()] = "Discoverer"
    itemnames["a521c40c620a2dd22c1bb1e9db722c4c15e42eb1".upper()] = "Collector"
    itemnames["cf37caa096aac5127ec3fe67c2606075fcc652a8".upper()] = "General"

    return itemnames.get(uuid.upper(), "Unknown item name")

def getItemNumber(uuid):
    itemnumber = {}
    
    itemnumber["de922af379061263a56d7204d1c395cefcfb7d75".upper()] = 0
    itemnumber["ba85cc2b8a5d986bbfba6954e2164ef71af95d4a".upper()] = 1    
    itemnumber["05294270032e5dc968672425ab5611998c409166".upper()] = 2
    itemnumber["3c9f85221807b8d593fa5276cdf7af9913c4a35d".upper()] = 3    
    itemnumber["422db99aac4ec594d483d8ef7faadc5d40d6f7d3".upper()] = 4
    itemnumber["118d34e685b5d1472267696d1010a393a59aed03".upper()] = 5    
    itemnumber["d9fa5f359e80ff4f4c97545d07c66dbadab1d1be".upper()] = 6
    itemnumber["e4b78acddfa6fd0234bcb814b676271898b0dbb3".upper()] = 7
    itemnumber["5560a1580a0330e8aadf05cb5bfe6bc3200406e2".upper()] = 8    
    itemnumber["da4a2a1bb9afd410be07bc9736d87f1c8059e66d".upper()] = 9
    itemnumber["d26f4dab76fdc5296e3ebec11a1e1d2558c713ea".upper()] = 10
    itemnumber["8a4f9e8309e1078f7f5ced47d558d30ae15b4a1b".upper()] = 11
    itemnumber["40f6c78e11be01ad3389b7dccd6ab8efa9347f3c".upper()] = 12
    itemnumber["4a58d4978bbe24e3efb3b0248e21b3b4b1bfbd8a".upper()] = 13
    itemnumber["929d5e15709cc51a4500de4499e19763c879f7f7".upper()] = 14
    itemnumber["d3d541ecc23e4daa0c698e44c32f04afd2037d84".upper()] = 15
    itemnumber["27cbcd52f16693023cb966e5026d8a1efbbfc0f9".upper()] = 16
    itemnumber["0968999df2fe956aa4a07aea74921f860af7d97f".upper()] = 17
    itemnumber["16768164989dffd819a373613b5e1a52e226a5b0".upper()] = 18
    itemnumber["0e41524dc46225dca21c9119f2fb735fd7ea5cb3".upper()] = 19
    itemnumber["04e58444d6d0beb57b3e998edc34c60f8318825a".upper()] = 20
    itemnumber["be67e009a5894f19bbf3b0c9d9b072d49040a2cc".upper()] = 21
    itemnumber["c21ff33ba8f0a7eadb6b7d1135763366f0c4b8bf".upper()] = 22
    itemnumber["05ee9654bd11a261f1ff0e5d0e49121b5e7e4401".upper()] = 23
    itemnumber["485a6d5624d9de836d3eb52b181b13423f795770".upper()] = 24
    itemnumber["fd895a5c9fd978b9c5c7b65158099773ba0eccef".upper()] = 25
    itemnumber["45d6660308689c65d97f3c27327b0b31f880ae75".upper()] = 26
    itemnumber["cb4fd53e61feced0d52cfc4c1ce383bad9c05f67".upper()] = 27
    itemnumber["14c17d49462963f5e5b67efa1257622ce1b866ac".upper()] = 28
    itemnumber["75accaa0d1bc22b78d83b89cd437bdccd6a58887".upper()] = 29
    itemnumber["78badde414b2cba7c0c37e3e11a5a42e8414c8ac".upper()] = 30
    itemnumber["10662141326cc46ee30bc4dd05f581424050a768".upper()] = 31
    itemnumber["bbc7ee322189528ad5bc3a19e048c4ff582538b5".upper()] = 32
    itemnumber["ddb65e18ec97b32d7dc50249a0d9c256f57664df".upper()] = 33
    itemnumber["e8e01fb84ed1a33ed3ab34af6fc84e86e3505142".upper()] = 34
    itemnumber["090a969b05d1b5dc458a6b1080da7ba08b84ec7f".upper()] = 35
    itemnumber["b956c46faa8e4e5d8775701c69dbfbf53309b279".upper()] = 36
    itemnumber["e254352ac599de4dd1f20f0719df0a070c623ca8".upper()] = 37
    itemnumber["67d6041bc0206d1ec7ce667e51f9d7ba73314604".upper()] = 38
    itemnumber["a521c40c620a2dd22c1bb1e9db722c4c15e42eb1".upper()] = 39
    itemnumber["cf37caa096aac5127ec3fe67c2606075fcc652a8".upper()] = 40   
    
    return itemnumber.get(uuid.upper(), -1)

def simplestatistics(array):
    minelem = min(array)
    maxelem = max(array)
    mean = np.mean(array)
    stddev = np.std(array)
    return [minelem, maxelem, round(mean,2), round(stddev,2)]




if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print "Usage:", sys.argv[0], "auctions.json [server]"
        sys.exit(0)
        
    inputfilename = sys.argv[1]
    
    with open(inputfilename, "r") as f:
        auctions = json.load(f)
        
    if len(sys.argv) >= 3:
        serverfilter = sys.argv[2]
        auctions = [a for a in auctions if a["serverId"] == serverfilter]
        
    print "Auctions:", len(auctions)
    print ""
    
    if len(auctions) == 0:
        sys.exit(0)
    
    itemfrequencies = {}
    itemrarityfrequencies = {}
    itemprices = defaultdict(list)
    itemdurations = defaultdict(list) #seconds
    
    itemswithoutbidsfrequencies = {}    
    relativeBidTimepointsHistogram = [0] * 100
    numBidsPerItem = defaultdict(list)
    numPlayersPerItem = defaultdict(list)
    
    for a in auctions:
        uuid = a["uuid"]
        itemfrequencies[uuid] = itemfrequencies.get(uuid, 0) + 1
        itemrarityfrequencies[a["rarity"]] = itemrarityfrequencies.get(a["rarity"], 0) + 1
        price = int(a["price"])
        if price > 0:
            itemprices[uuid].append(price)
        else:
            itemswithoutbidsfrequencies[uuid] = itemswithoutbidsfrequencies.get(uuid, 0) + 1
        
        startdate = datetime.strptime(a["startDate"], '%Y-%m-%d %H:%M:%S')
        enddate = datetime.strptime(a["endDate"], '%Y-%m-%d %H:%M:%S')
        durationInSeconds = enddate.minute * 60 + enddate.second
        itemdurations[uuid].append(durationInSeconds)
        
        playerset = set()
        
        for bid in a["bids"]:
            biddate = datetime.strptime(bid["date"], '%Y-%m-%d %H:%M:%S')
            diff = biddate - startdate
            diff = diff.seconds
            pos = int(100 * float(diff)/durationInSeconds)
            relativeBidTimepointsHistogram[pos] += 1
            playerset.add(bid["playerName"])
            
        numPlayersPerItem[uuid].append(len(playerset))
        numBidsPerItem[uuid].append(int(a["numBids"]))
        
        
    numBids = 0
        
    itempricesAgg = defaultdict(list)
    for key in itemprices:
        itempricesAgg[key] = simplestatistics(itemprices[key])
        
    itemdurationsAgg = defaultdict(list)
    for key in itemdurations:
        itemdurationsAgg[key] = simplestatistics(itemdurations[key])
        
    numPlayersPerItemAgg = defaultdict(list)
    for key in numPlayersPerItem:
        numPlayersPerItemAgg[key] = simplestatistics(numPlayersPerItem[key])
        
    numBidsPerItemAgg = defaultdict(list)
    for key in numBidsPerItem:
        numBidsPerItemAgg[key] = simplestatistics(numBidsPerItem[key])
        numBids += sum(numBidsPerItem[key])
        
    print "Bids:", numBids
    print ""
        
    print "Rarity counts:"
    for key in itemrarityfrequencies:
        print key, ":", itemrarityfrequencies[key], round(float(itemrarityfrequencies[key]) / len(auctions) * 100, 2), "%"
    print ""

    sortedlist = sorted([(k,v) for k, v in itemfrequencies.items()], key=lambda t: getItemNumber(t[0]))
    print "Item counts:"
    for k,v in sortedlist:
        print getItemName(k), ":", v, " : ", round(float(v) / len(auctions) * 100, 2), "%"
    print ""
    
    sortedlist = sorted([(k,v) for k, v in itempricesAgg.items()], key=lambda t: getItemNumber(t[0]))
    print "Item prices (only prices > 0): min, max, avg, stddev"
    for k,v in sortedlist:
        print getItemName(k), ":", str(v)
    print ""
    
    sortedlist = sorted([(k,v) for k, v in itemswithoutbidsfrequencies.items()], key=lambda t: getItemNumber(t[0]))
    print "Items without bids:"
    for k,v in sortedlist:
        print getItemName(k), ":", str(v)
    print ""
    
    sortedlist = sorted([(k,v) for k, v in itemdurationsAgg.items()], key=lambda t: getItemNumber(t[0]))
    print "Auction durations (seconds): min, max, avg, stddev"
    for k,v in sortedlist:
        print getItemName(k), ":", str(v)
    print ""
    
    print "Relative bid time"
    print str(relativeBidTimepointsHistogram)
    print ""
    
    sortedlist = sorted([(k,v) for k, v in numPlayersPerItemAgg.items()], key=lambda t: getItemNumber(t[0]))
    print "Number of players placing a bid per item: min, max, avg, stddev"
    for k,v in sortedlist:
        print getItemName(k), ":", str(v)
    print ""
    
    sortedlist = sorted([(k,v) for k, v in numBidsPerItemAgg.items()], key=lambda t: getItemNumber(t[0]))
    print "Number of bids per item: min, max, avg, stddev"
    for k,v in sortedlist:
        print getItemName(k), ":", str(v)
    print ""

