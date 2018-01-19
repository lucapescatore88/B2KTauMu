from Gaudi.Configuration       import *
from GaudiKernel.SystemOfUnits import *
from collections import defaultdict

def set_branches(full_descriptor,names) :
    descriptors = full_descriptor.split('||') #split the parts in OR and treat them separately
    branches = defaultdict(list)
    for descriptor in descriptors:
        descriptor = descriptor.replace("^","")
        branches[names[0]].append("(^"+descriptor+")") #no caret for the mother
        cleandesc = descriptor.replace("->"," ").replace("\ )"," ")\
                    .replace("( "," ").replace("[ "," ")\
                    .replace(" ]"," ").replace("==>"," ")
        daughters = cleandesc.split()[1:]
        pos = 0
        for ni,n in enumerate(names[1:]) :
            
            pos = descriptor.find(daughters[ni],pos)
            branches[n].append(''.join(list(descriptor[:pos] + "^" + descriptor[pos:])))
            pos += 1

    branches_full = {}
    for n in names : #now we can join back the n parts that were in OR
        branches_full[n] = " || ".join(branches[n])
    return branches_full

   
def ReStrip(mylines,stripping="stripping21r0p1",streamname=None) :

    from Configurables import EventNodeKiller, ProcStatusCheck
    from StrippingArchive.Utils import buildStreams
    from StrippingArchive import strippingArchive
    from StrippingConf.Configuration import StrippingStream
    from StrippingConf.Configuration import StrippingConf
    from StrippingSettings.Utils import strippingConfiguration
    
    NodeKiller       = EventNodeKiller( "StripKiller" )
    NodeKiller.Nodes = [ "/Event/AllStreams","/Event/Strip" ]

    from StrippingSelections import buildersConf
    from StrippingSelections.Utils import lineBuilder, buildStreamsFromBuilder

    config  = strippingConfiguration(stripping)
    archive = strippingArchive(stripping)
    streams = buildStreams(stripping=config, archive=archive) 

    #confs = buildersConf()
    
    mystream = StrippingStream( "MyStream" )
    #for name in confnames:
    #    streams = buildStreamsFromBuilder(confs,name)
    for stream in streams :
        #if streamname not in stream : continue
        for line in stream.lines:
            print line
            if line.name() in mylines:
                print "Adding ", line.name(), "for restripping"
                mystream.appendLines( [ line ] )

    restrip = StrippingConf( Streams = [ mystream ],
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    BadEventSelection = ProcStatusCheck(),
                    TESPrefix = 'Strip',
                    ActiveMDSTStream = True )
                    #Verbose = True,
                    #MicroDSTStreams = streams )
    return restrip, [ NodeKiller, restrip.sequence() ]


