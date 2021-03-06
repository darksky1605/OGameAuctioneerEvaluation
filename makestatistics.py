#!/usr/bin/python

import json
import sys
from datetime import datetime, timedelta
import numpy as np 
from collections import defaultdict


def getItemName(uuid):
    itemnames = {}
    
    itemnames["de922af379061263a56d7204d1c395cefcfb7d75".upper()] = "+10% Met Booster 7 days"    
    itemnames["ba85cc2b8a5d986bbfba6954e2164ef71af95d4a".upper()] = "+20% Met Booster 7 days"
    itemnames["05294270032e5dc968672425ab5611998c409166".upper()] = "+30% Met Booster 7 days"
    itemnames["a83cfdc15b8dba27c82962d57e50d8101d263cfb".upper()] = "+40% Met Booster 7 days"
    itemnames["3c9f85221807b8d593fa5276cdf7af9913c4a35d".upper()] = "+10% Crys Booster 7 days"
    itemnames["422db99aac4ec594d483d8ef7faadc5d40d6f7d3".upper()] = "+20% Crys Booster 7 days"    
    itemnames["118d34e685b5d1472267696d1010a393a59aed03".upper()] = "+30% Crys Booster 7 days"
    itemnames["35d96e441c21ef112a84c618934d9d0f026998fd".upper()] = "+40% Crys Booster 7 days"
    itemnames["d9fa5f359e80ff4f4c97545d07c66dbadab1d1be".upper()] = "+10% Deut Booster 7 days"
    itemnames["e4b78acddfa6fd0234bcb814b676271898b0dbb3".upper()] = "+20% Deut Booster 7 days"
    itemnames["5560a1580a0330e8aadf05cb5bfe6bc3200406e2".upper()] = "+30% Deut Booster 7 days"
    itemnames["4b51d903560edd102467b110586000bd64fdb954".upper()] = "+40% Deut Booster 7 days"
    itemnames["742743b3b0ae1f0b8a1e01921042810b58f12f39".upper()] = "+20% Met Booster 30 days"
    itemnames["6fecb993169fe918d9c63cd37a2e541cc067664e".upper()] = "+30% Met Booster 30 days"
    itemnames["c690f492cffe5f9f2952337e8eed307a8a62d6cf".upper()] = "+40% Met Booster 30 days"    
    itemnames["5b69663e3ba09a1fe77cf72c5094e246cfe954d6".upper()] = "+20% Crys Booster 30 days"    
    itemnames["36fb611e71d42014f5ebd0aa5a52bc0c81a0c1cb".upper()] = "+30% Crys Booster 30 days"
    itemnames["6bf45fcba8a6a68158273d04a924452eca75cf39".upper()] = "+40% Crys Booster 30 days"    
    itemnames["26416a3cdb94613844b1d3ca78b9057fd6ae9b15".upper()] = "+20% Deut Booster 30 days"
    itemnames["300493ddc756869578cb2888a3a1bc0c3c66765f".upper()] = "+30% Deut Booster 30 days"
    itemnames["620f779dbffa1011aded69b091239727910a3d03".upper()] = "+40% Deut Booster 30 days"    
    itemnames["6f44dcd2bd84875527abba69158b4e976c308bbc".upper()] = "+20% Met Booster 90 days"
    itemnames["21c1a65ca6aecf54ffafb94c01d0c60d821b325d".upper()] = "+30% Met Booster 90 days"
    itemnames["ca7f903a65467b70411e513b0920d66c417aa3a2".upper()] = "+40% Met Booster 90 days"    
    itemnames["04d8afd5936976e32ce894b765ea8bd168aa07ef".upper()] = "+20% Crys Booster 90 days"    
    itemnames["d45f00e8b909f5293a83df4f369737ea7d69c684".upper()] = "+30% Crys Booster 90 days"
    itemnames["7c2edf40c5cd54ad11c6439398b83020c0a7a6be".upper()] = "+40% Crys Booster 90 days"    
    itemnames["6f0952a919fd2ab9c009e9ccd83c1745f98f758f".upper()] = "+20% Deut Booster 90 days"
    itemnames["dc5896bed3311434224d511fa7ced6fdbe41b4e8".upper()] = "+30% Deut Booster 90 days"
    itemnames["831c3ea8d868eb3601536f4d5e768842988a1ba9".upper()] = "+40% Deut Booster 90 days"
    itemnames["3f6f381dc9b92822406731a942c028adf8dc978f".upper()] = "+20% Energy Booster 7 days"
    itemnames["7eeeb36a455c428eb6923a50d2f03544b6dd05d6".upper()] = "+20% Energy Booster 30 days"
    itemnames["6837c08228d2b023fb955ca2dc589a0a4bed3ba8".upper()] = "+20% Energy Booster 90 days"
    itemnames["c2bad58fcec374d709099d11d0549e59ea7e233e".upper()] = "+40% Energy Booster 7 days"
    itemnames["bedd248aaf288c27e9351cfacfa6be03f1dbb898".upper()] = "+40% Energy Booster 30 days"
    itemnames["e05aa5b9e3df5be3857b43da8403eafbf5ad3b96".upper()] = "+40% Energy Booster 90 days"
    itemnames["55b52cbfb148ec80cd4e5b0580f7bed01149d643".upper()] = "+60% Energy Booster 7 days"
    itemnames["4fa9a2273ee446284d5177fd9d60a22de01e932b".upper()] = "+60% Energy Booster 30 days"
    itemnames["5ad783dcfce3655ef97b36197425718a0dad6b66".upper()] = "+60% Energy Booster 90 days"
    itemnames["77c36199102e074dca46f5f26ef57ce824d044dd".upper()] = "+80% Energy Booster 7 days"
    itemnames["dfe86378f8c3d7f3ee0790ea64603bc44e83ca47".upper()] = "+80% Energy Booster 30 days"
    itemnames["c39aa972a971e94b1d9b4d7a8f734b3d8be12534".upper()] = "+80% Energy Booster 90 days"
    itemnames["da4a2a1bb9afd410be07bc9736d87f1c8059e66d".upper()] =  "NEWTRON Bronze"
    itemnames["d26f4dab76fdc5296e3ebec11a1e1d2558c713ea".upper()] =  "NEWTRON Silver"
    itemnames["8a4f9e8309e1078f7f5ced47d558d30ae15b4a1b".upper()] =  "NEWTRON Gold"
    itemnames["a1ba242ede5286b530cdf991796b3d1cae9e4f23".upper()] =  "NEWTRON Platinum"
    itemnames["40f6c78e11be01ad3389b7dccd6ab8efa9347f3c".upper()] =  "KRAKEN Bronze"
    itemnames["4a58d4978bbe24e3efb3b0248e21b3b4b1bfbd8a".upper()] =  "KRAKEN Silver"
    itemnames["929d5e15709cc51a4500de4499e19763c879f7f7".upper()] =  "KRAKEN Gold"
    itemnames["f36042d76e6b8b33d931e1d4ae99f35265cd82d1".upper()] =  "KRAKEN Platinum"    
    itemnames["d3d541ecc23e4daa0c698e44c32f04afd2037d84".upper()] =  "DETROID Bronze"
    itemnames["27cbcd52f16693023cb966e5026d8a1efbbfc0f9".upper()] =  "DETROID Silver"
    itemnames["0968999df2fe956aa4a07aea74921f860af7d97f".upper()] =  "DETROID Gold"
    itemnames["3347bcd4ee59f1d3fa03c4d18a25bca2da81de82".upper()] =  "DETROID Platinum"
    itemnames["16768164989dffd819a373613b5e1a52e226a5b0".upper()] =  "+4 Planet Fields"
    itemnames["0e41524dc46225dca21c9119f2fb735fd7ea5cb3".upper()] =  "+9 Planet Fields"
    itemnames["04e58444d6d0beb57b3e998edc34c60f8318825a".upper()] = "+15 Planet Fields"
    itemnames["f3d9b82e10f2e969209c1a5ad7d22181c703bb36".upper()] = "+20 Planet Fields"
    itemnames["be67e009a5894f19bbf3b0c9d9b072d49040a2cc".upper()] =  "+2 Moon Fields"
    itemnames["c21ff33ba8f0a7eadb6b7d1135763366f0c4b8bf".upper()] =  "+4 Moon Fields"
    itemnames["05ee9654bd11a261f1ff0e5d0e49121b5e7e4401".upper()] =  "+6 Moon Fields"
    itemnames["8a426241572b2fea57844acd99bc326fe40e35cf".upper()] =  "+8 Moon Fields"
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
    itemnames["2dd05cc4c0e185fce2e712112dc44932027aee98".upper()] = "Discoverer"
    itemnames["9374c79a24b84c4331f0d26526ef6c2d33319a6e".upper()] = "Collector"
    itemnames["77eff880829027daf23b755e14820a60c4c6fd93".upper()] = "General"

    return itemnames.get(uuid.upper(), "Unknown item name, id " + uuid.upper())

def getItemNumber(uuid):
    itemnumber = {}
    
    itemnumber["de922af379061263a56d7204d1c395cefcfb7d75".upper()] = 0
    itemnumber["ba85cc2b8a5d986bbfba6954e2164ef71af95d4a".upper()] = 1
    itemnumber["05294270032e5dc968672425ab5611998c409166".upper()] = 2
    itemnumber["a83cfdc15b8dba27c82962d57e50d8101d263cfb".upper()] = 3
    itemnumber["3c9f85221807b8d593fa5276cdf7af9913c4a35d".upper()] = 4
    itemnumber["422db99aac4ec594d483d8ef7faadc5d40d6f7d3".upper()] = 5
    itemnumber["118d34e685b5d1472267696d1010a393a59aed03".upper()] = 6
    itemnumber["35d96e441c21ef112a84c618934d9d0f026998fd".upper()] = 7
    itemnumber["d9fa5f359e80ff4f4c97545d07c66dbadab1d1be".upper()] = 8
    itemnumber["e4b78acddfa6fd0234bcb814b676271898b0dbb3".upper()] = 9
    itemnumber["5560a1580a0330e8aadf05cb5bfe6bc3200406e2".upper()] = 10
    itemnumber["4b51d903560edd102467b110586000bd64fdb954".upper()] = 11
    itemnumber["742743b3b0ae1f0b8a1e01921042810b58f12f39".upper()] = 12
    itemnumber["6fecb993169fe918d9c63cd37a2e541cc067664e".upper()] = 13
    itemnumber["c690f492cffe5f9f2952337e8eed307a8a62d6cf".upper()] = 14
    itemnumber["5b69663e3ba09a1fe77cf72c5094e246cfe954d6".upper()] = 15
    itemnumber["36fb611e71d42014f5ebd0aa5a52bc0c81a0c1cb".upper()] = 16
    itemnumber["6bf45fcba8a6a68158273d04a924452eca75cf39".upper()] = 17
    itemnumber["26416a3cdb94613844b1d3ca78b9057fd6ae9b15".upper()] = 18
    itemnumber["300493ddc756869578cb2888a3a1bc0c3c66765f".upper()] = 19
    itemnumber["620f779dbffa1011aded69b091239727910a3d03".upper()] = 20
    itemnumber["6f44dcd2bd84875527abba69158b4e976c308bbc".upper()] = 21
    itemnumber["21c1a65ca6aecf54ffafb94c01d0c60d821b325d".upper()] = 22
    itemnumber["ca7f903a65467b70411e513b0920d66c417aa3a2".upper()] = 23
    itemnumber["04d8afd5936976e32ce894b765ea8bd168aa07ef".upper()] = 24
    itemnumber["d45f00e8b909f5293a83df4f369737ea7d69c684".upper()] = 25
    itemnumber["7c2edf40c5cd54ad11c6439398b83020c0a7a6be".upper()] = 26
    itemnumber["6f0952a919fd2ab9c009e9ccd83c1745f98f758f".upper()] = 27
    itemnumber["dc5896bed3311434224d511fa7ced6fdbe41b4e8".upper()] = 28
    itemnumber["831c3ea8d868eb3601536f4d5e768842988a1ba9".upper()] = 29
    itemnames["3f6f381dc9b92822406731a942c028adf8dc978f".upper()] = 30
    itemnames["7eeeb36a455c428eb6923a50d2f03544b6dd05d6".upper()] = 31
    itemnames["6837c08228d2b023fb955ca2dc589a0a4bed3ba8".upper()] = 32
    itemnames["c2bad58fcec374d709099d11d0549e59ea7e233e".upper()] = 33
    itemnames["bedd248aaf288c27e9351cfacfa6be03f1dbb898".upper()] = 34
    itemnames["e05aa5b9e3df5be3857b43da8403eafbf5ad3b96".upper()] = 35
    itemnames["55b52cbfb148ec80cd4e5b0580f7bed01149d643".upper()] = 36
    itemnames["4fa9a2273ee446284d5177fd9d60a22de01e932b".upper()] = 37
    itemnames["5ad783dcfce3655ef97b36197425718a0dad6b66".upper()] = 38
    itemnames["77c36199102e074dca46f5f26ef57ce824d044dd".upper()] = 39
    itemnames["dfe86378f8c3d7f3ee0790ea64603bc44e83ca47".upper()] = 40
    itemnames["c39aa972a971e94b1d9b4d7a8f734b3d8be12534".upper()] = 41
    itemnumber["da4a2a1bb9afd410be07bc9736d87f1c8059e66d".upper()] = 42
    itemnumber["d26f4dab76fdc5296e3ebec11a1e1d2558c713ea".upper()] = 43
    itemnumber["8a4f9e8309e1078f7f5ced47d558d30ae15b4a1b".upper()] = 44
    itemnumber["a1ba242ede5286b530cdf991796b3d1cae9e4f23".upper()] = 45    
    itemnumber["40f6c78e11be01ad3389b7dccd6ab8efa9347f3c".upper()] = 46
    itemnumber["4a58d4978bbe24e3efb3b0248e21b3b4b1bfbd8a".upper()] = 47
    itemnumber["929d5e15709cc51a4500de4499e19763c879f7f7".upper()] = 48
    itemnumber["f36042d76e6b8b33d931e1d4ae99f35265cd82d1".upper()] = 49
    itemnumber["d3d541ecc23e4daa0c698e44c32f04afd2037d84".upper()] = 50
    itemnumber["27cbcd52f16693023cb966e5026d8a1efbbfc0f9".upper()] = 51
    itemnumber["0968999df2fe956aa4a07aea74921f860af7d97f".upper()] = 52
    itemnumber["3347bcd4ee59f1d3fa03c4d18a25bca2da81de82".upper()] = 53
    itemnumber["16768164989dffd819a373613b5e1a52e226a5b0".upper()] = 54
    itemnumber["0e41524dc46225dca21c9119f2fb735fd7ea5cb3".upper()] = 55
    itemnumber["04e58444d6d0beb57b3e998edc34c60f8318825a".upper()] = 56
    itemnumber["f3d9b82e10f2e969209c1a5ad7d22181c703bb36".upper()] = 57
    itemnumber["be67e009a5894f19bbf3b0c9d9b072d49040a2cc".upper()] = 58
    itemnumber["c21ff33ba8f0a7eadb6b7d1135763366f0c4b8bf".upper()] = 59
    itemnumber["05ee9654bd11a261f1ff0e5d0e49121b5e7e4401".upper()] = 60
    itemnumber["8a426241572b2fea57844acd99bc326fe40e35cf".upper()] = 61
    itemnumber["485a6d5624d9de836d3eb52b181b13423f795770".upper()] = 62
    itemnumber["fd895a5c9fd978b9c5c7b65158099773ba0eccef".upper()] = 63
    itemnumber["45d6660308689c65d97f3c27327b0b31f880ae75".upper()] = 64
    itemnumber["cb4fd53e61feced0d52cfc4c1ce383bad9c05f67".upper()] = 65
    itemnumber["14c17d49462963f5e5b67efa1257622ce1b866ac".upper()] = 66
    itemnumber["75accaa0d1bc22b78d83b89cd437bdccd6a58887".upper()] = 67
    itemnumber["78badde414b2cba7c0c37e3e11a5a42e8414c8ac".upper()] = 68
    itemnumber["10662141326cc46ee30bc4dd05f581424050a768".upper()] = 69
    itemnumber["bbc7ee322189528ad5bc3a19e048c4ff582538b5".upper()] = 70
    itemnumber["ddb65e18ec97b32d7dc50249a0d9c256f57664df".upper()] = 71
    itemnumber["e8e01fb84ed1a33ed3ab34af6fc84e86e3505142".upper()] = 72
    itemnumber["090a969b05d1b5dc458a6b1080da7ba08b84ec7f".upper()] = 73
    itemnumber["b956c46faa8e4e5d8775701c69dbfbf53309b279".upper()] = 74
    itemnumber["e254352ac599de4dd1f20f0719df0a070c623ca8".upper()] = 75
    itemnumber["2dd05cc4c0e185fce2e712112dc44932027aee98".upper()] = 76
    itemnumber["9374c79a24b84c4331f0d26526ef6c2d33319a6e".upper()] = 77
    itemnumber["77eff880829027daf23b755e14820a60c4c6fd93".upper()] = 78
    
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

