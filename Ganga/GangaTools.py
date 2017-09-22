import os
import subprocess
import pickle
import shutil

#print 'Loading modules from .ganga.py and renewing proxy...'
#gridProxy.renew()

def GetHome() :
    return os.getenv('HOME')

def GetBase() :
    return GetHome()+'/work'

def GetJobFolder( id ) :
    return GetHome()+'/gangadir/workspace/'+os.getenv('USER')+'/LocalXML/'+str(id)

def DumpJobs(jobs) :
    pickle.dump( jobs, open( GetHome()+"/.jobs.p" , "wb" ) )

if not os.path.exists(GetHome()+"/.jobs.p") : DumpJobs({})
avjobs = pickle.load( open( GetHome()+"/.jobs.p", "rb" ) )

######################################################################

DataTypesCL        = [ 'CL11', 'CL12' ]
DataTypesMC        = [ 'MC11', 'MC12' ]
DataTypes          = DataTypesCL + DataTypesMC;
MagPolarities      = [ 'MD', 'MU' ];

######################################################################
#
#       Rutines
#
######################################################################

def CleanUp() :

    jnames = set([ j.name for j in jobs ])
    for jname in jnames :
        print '\nAnalysing', jname
        ids = []
        for j in jobs :
            if j.name == jname :
                print "---->", j.time.timestamps['new'].strftime("%d/%m/%y"), j.id, j.status
                ids.append(j.id)
        if len(ids) > 1 :
            x = raw_input("More than one job found. Cleanup "+str(ids[:-1])+"? y/[n]")
            if x == 'y' :
                print "Removing"
                for cid in ids[:-1] :
                    print "Removing job info", cid
                    RemoveJobs(cid)
                    eospath = '/eos/lhcb/user/p/pluca/ganga/'+str(cid)
                    if os.path.exists(eospath) :
                        print "Removing eos data", eospath
                        shutil.rmtree(eospath)


def Progress(status,length = None) :
    
    #cols = ['black','red','green','yellow','blue','magenta','cyan','white']
    #colors = { col : 40+j for j,col in enumerate(cols) }
    colors = { 'black':40,'red':41,'green':42,'yellow':43,'blue':44,'magenta':45,'cyan':46,'white':47}
    semantic = {'Done' : 'blue', 'Running' : 'green', 'Failed' : 'red'}
    
    tot = int(status['Total'])
    if length is None :
        rows, length = os.popen('stty size', 'r').read().split()
        length = int(length) - 5
    cbin = length % tot
    if cbin < length : length = (length - cbin)

    ntot, out = 0, ""
    for st in [ 'Done', 'Running', 'Failed' ] : 
        nsp = int(round(status[st] / float(tot) * length))
        if nsp > 0. : 
            out += "\033[{0}m".format(colors[semantic[st]])
            out += ' '*nsp
            ntot += nsp
    if int(length - ntot) > 0 : out += "\033[47m"+(' '*int(length - ntot))

    print out+"\033[0m"

def CheckStatus( start, stop = 0 ) :

    if stop == 0 : stop = start
    if start > stop :
        print 'ERROR: invalid Start&Stop', start, stop
        return

    for j in jobs :
        if j.id >= start and j.id <= stop :

            status = { 'Total' : 0, 'Checking' : 0, 'Waiting' : 0,
            'Running' : 0, 'Done' : 0, 'Failed' : 0, 'Killed' : 0,
            'Unknown' : 0, 'Completing' : 0 }

            for s in jobs( j.id ).subjobs :
                
                status['Total'] += 1
                curStatus = jobs( j.id ).subjobs( s.id ).backend.status
                if ( curStatus in status ) : status[curStatus] += 1
                else : status["Unknown"] += 1
            
            if status['Done'] == status['Total'] :
                avjobs[j.name]['status'] = 'completed'
                DumpJobs(avjobs)

            print
            print 'JobId    :', j.id
            print 'Total    :', status["Total"]
            for st in status :
                if st != 'Total' and st != 'Unknown' and status[st] > 0 :
                    print "{0:10}: {1}".format(st,status[st]),
                    perc = float(status[st]) / status["Total"] * 100
                    if perc >= 1. : print "--> {0:.0f}%".format(perc),
                    print
            if status['Unknown'] > 0 : print 'Unknown:  ', status["Unknown"]

            Progress(status)

######################################################################

def DiracIdJob( jobID, subJobID ) :

    if jobs( jobID ).subjobs( subJobID ) :
        jid = jobs( jobID ).subjobs( subJobID ).backend.id 
        print 'DIRAC ID: ', jid
        return jid 

######################################################################

def ForceJobs( start, stop = 0, status = 'failed' ) :
    
    if stop == 0 : stop = start
    if start > stop :
        print 'ERROR: invalid Start&Stop', start, stop
        return
    
    for j in jobs :
        if j.id >= start and j.id <= stop :
            
            curStatus = jobs( j.id ).subjobs( s.id ).backend.status
            
            if curStatus in ["Done","Failed","Running","Checking"] :
                continue
        
            for sj in j.subjobs :
                jobs( j.id ).subjobs( sj.id ).force_status( status )
    
######################################################################

def KillJobs( start, stop = 0 ) :

    if stop == 0 : stop = start
    if start > stop :
        print 'ERROR: invalid Start&Stop', start, stop
        return

    for j in jobs :
        if j.id >= start and j.id <= stop :
            j.kill()
            os.system( 'sleep 5' )
            for sj in j.subjobs :
                sj.kill()

######################################################################

def PeekJob( jobID, subJobID, output = 'stdout' ) :

    if jobs( jobID ).subjobs( subJobID ) :
        jobs( jobID ).subjobs( subJobID ).peek( output )

######################################################################

def RemoveJobs( start, stop = 0 ) :

    if stop == 0 : stop = start
    if start > stop :
        print 'ERROR: invalid Start&Stop', start, stop
        return

    for j in jobs :
        if j.id >= start and j.id <= stop :
            j.remove()
            os.system( 'sleep 5' )

######################################################################

def SmartResubmitJob( jobID, force=0 ) :

    for sj in jobs( jobID ).subjobs :
        if(sj.status != 'completed' and sj.status != 'submitted') :
            if( (sj.status != 'completing') or force > 0 ) :
                if( (sj.status == 'running' and force > 1) or (sj.status != 'running') ) :
                    print 'Resubmitting SubJob... ('+sj.status+')'
                    if((sj.status == 'running') and force > 1) :
                        sj.kill()
                    sj.resubmit()
                    os.system( 'sleep 5' )
        
###############################################################################

def ResetSubJobs( id ) :

    for j in jobs :
        if j.id == id :
            for s in jobs( j.id ).subjobs :
                if s.status != "completed" :
                    s.backend.reset()

######################################################################

def SubmitJobs( start, stop = 0 ) :

    if stop == 0 : stop = start
    if start > stop :
        print 'ERROR: invalid Start&Stop', start, stop
        return

    for j in jobs :
        if j.id >= start and j.id <= stop :
            j.submit()
            os.system( 'sleep 5' )
            print

######################################################################

def CreateDVJob( jobName, appVersion, optFile, inputData, inputFiles, splitSize = 100, mergeOutput = True, local = False ) :

    j = Job(application=DaVinci(version=appVersion), name = jobName, backend=Dirac())
    if local : j.backend = Local()
    
    ### Inputs
    j.application.optsfile = [File(optFile)]
    j.inputdata = j.application.readInputData(inputData)

    ### Finish initialisation and submit
    j.inputfiles = [ File(f) for f in inputFiles]
    j.splitter = SplitByFiles(filesPerJob=splitSize)

    j.outputfiles=[MassStorageFile('*.root')]
    j.do_auto_resubmit = True
    
    #if(mergeOutput) :
    #    merge = RootMerger()
    #    merge.files = ['ntuples.root']
    #    job.merger = merge

    print 'INFO:', jobName, ', DaVinci ', appVersion, ',', optFile
    print job

    return job

######################################################################

def GetBox( boxName ) :

    try :
        boxObject = box [ boxName ]
        return boxObject
    except :
        print 'ERROR: invalid BoxName', boxName
        return

######################################################################

def GetBKPath( analysis, dataType, decayMode, magPolarity ) :

    mag = {'MD' : 'MagDown', 'MU' : 'MagUp'}
    
    if dataType == 'CL11' :
        bkPath = '/LHCb/Collision11/Beam3500GeV-VeloClosed-' + mag[magPolarity] + '/Real Data/' + GetReco( 'CL11', decayMode ) + '/' + GetStripping( 'CL11', decayMode ) + '/90000000/' + GetDecayCode( decayMode )

    elif dataType == 'CL12' :
        bkPath = '/LHCb/Collision12/Beam4000GeV-VeloClosed-' + mag[magPolarity] + '/Real Data/' + GetReco( 'CL12', decayMode ) + '/' + GetStripping( 'CL12', decayMode, analysis ) + '/90000000/' + GetDecayCode( decayMode )
            
    elif dataType == 'MC11' :
        bkPath = '/MC/2011/Beam3500GeV-2011-' + mag[magPolarity] + '-Nu2-Pythia8/' + GetSim( 'MC11', decayMode ) + '/Digi13/Trig0x40760037/' + GetReco( 'MC11', decayMode ) + '/' + GetStripping( 'MC11', decayMode, analysis ) + '/' + GetDecayCode( decayMode ) + '/ALLSTREAMS.DST'
    elif dataType == 'MC12' :
        bkPath = '/MC/2012/Beam4000GeV-2012-' + mag[magPolarity] + '-Nu2.5-Pythia8/' + GetSim( 'MC12', decayMode ) + '/Digi13/Trig0x409f0045/' + GetReco( 'MC12', decayMode ) + '/' + GetStripping( 'MC12', decayMode, analysis ) + '/' + GetDecayCode( decayMode ) + '/ALLSTREAMS.DST'
    
    else :
        bkPath = ''
        print 'NO PATH AVAILABLE!'

    return bkPath

######################################################################
#
# Dictionaries:
#
######################################################################

DecayCode = {
    'LPT'            : 'LEPTONIC.MDST',
    'Bd2KstEE'       : '11124001',
    'Bd2Kstgamma'    : '11102201',
    'Bd2KstMuMu'     : '11114001',
    'Bs2phiMuMu'     : '13114001',
    'Bd2JpsiKstMuMu' : '11144001',
    'Bd2JpsiKstEE'   : '11154001',
    'Bs2JpsiKstMuMu' : '13444001',
    'Bu2KMuMu'       : '12113001',
    'Bd2KpiMuMu'     : '11114011',
    'Bd2JpsiXMuMu'     : '11442001',
    'Bd2JpsiXEE'     : '11453001',
####################################
    'DIMUON'         : 'DIMUON.DST',
    'Lb2Lmumu'       : '15114101',
    'Lb2psi2SL'      : '15144111',
    'Lb2JpsiL'       : '15144103',
    'Lb2JpsipK'      : '15144001',
    'Bd2JpsiKS'     : '11144103',
    'Bd2KSmumu'     : '11114101'
    }

def GetProduction( dataType ) :

    if not CheckDataType( dataType ) :
        print 'ERROR: GetProduction'
        return

    if dataType == 'CL11' :
        production = 'R14S20R1'
    if dataType == 'CL12' :
        production = 'R14S20'

    if dataType == 'MC11' :
        production = 'S8R14aS20R1'
    if dataType == 'MC12' :
        production = 'S8R14aS20'

    return production

def GetReco( dataType, decayMode ) :

    print dataType, decayMode
    return GetSimStripReco(dataType, decayMode, 'Reco')

def GetSim( dataType, decayMode ) :

    return GetSimStripReco(dataType, decayMode, 'Sim')

######################################################################

def GetSplitSize( decayMode ) :

    if not CheckDecayMode( decayMode ) :
        print 'ERROR: GetSplitSize'
        return

    if decayMode in DecayModesCL :
        return 100

    if decayMode in DecayModesMC :
        return 10

######################################################################

def GetString( analysis, dataType, decayMode, magPolarity, type_ = True ) :

    if analysis == 'RKst' :

        if ( dataType == 'CL11' ) or ( dataType == 'MC11' ) :
            energy = '7TeV'
        if ( dataType == 'CL12' ) or ( dataType == 'MC12' ) :
            energy = '8TeV'

        if(type_) :
            string = energy + ' VC ' + magPolarity + ' ' + GetProduction( dataType ) + ' ' + decayMode + ' ' + dataType
        else :
            string = decayMode + ' ' + magPolarity + ' ' + dataType + ' ' + GetProduction( dataType )

    else :
        string = analysis + ' ' + decayMode + ' ' + magPolarity + ' ' + dataType

    return string

def GetStripping( dataType, decayMode, analysis = 'RKst' ) :
    
    return GetSimStripReco(dataType, decayMode, 'Strip')

def GetSimStripReco( dataType, decayMode, res = 'Strip' ) :
    
    if dataType == 'MC12' or dataType == 'CL12':
        recolist = {
        'LPT'            : ['', 'Stripping20r0p2', 'Reco14'],
        'Bd2KstEE'       : ['Sim08b', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2KstMuMu'     : ['Sim08b', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bs2phiMuMu'     : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiKstMuMu' : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiKstEE'   : ['Sim08b', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bs2JpsiKstMuMu' : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bu2KMuMu'       : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiXMuMu'     : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiXEE'     : ['Sim08c', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
####################################
        'DIMUON'         : ['', 'Stripping20r0', 'Reco14'],
        'Lb2Lmumu'       : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Lb2JpsiL'       : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Lb2JpsipK'      : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Lb2psi2SL'      : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiKS'     : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        'Bd2KSmumu'     : ['Sim08a', 'Stripping20NoPrescalingFlagged', 'Reco14a'],
        }
    else :
        recolist = {
        'LPT'            : ['', 'Stripping20r1p2', 'Reco14'],
        'Bd2KstEE'       : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2KstMuMu'     : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bs2phiMuMu'     : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiKstMuMu' : ['Sim08b', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiKstEE'   : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bs2JpsiKstMuMu' : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bu2KMuMu'       : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiXMuMu'     : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiXEE'     : ['Sim08c', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
####################################
        'DIMUON'         : ['', 'Stripping20r1p2', 'Reco14'],
        'Lb2Lmumu'       : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Lb2JpsiL'       : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Lb2JpsipK'      : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Lb2psi2SL'      : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2JpsiKS'     : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        'Bd2KSmumu'     : ['Sim08a', 'Stripping20r1NoPrescalingFlagged', 'Reco14a'],
        }

    if(res == 'Strip') :
        return recolist[decayMode][1];
    if(res == 'Reco') :
        return recolist[decayMode][2];
    if(res == 'Sim') :
        return recolist[decayMode][0];


