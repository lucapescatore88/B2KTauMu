import os, sys, re
root = os.environ["B2KTAUMUROOT"]
gangapath = root+"/Ganga"
sys.path.append( gangapath )
optionpath = root+"/Options"
sys.path.append( optionpath )

from DB import decays_db # USED TO LOOP OVER DECAYS FOR MC SUBMISSIOn

import pickle

from glob import glob

options = [ LocalFile( f ) for f in glob(root+"/Options/*.py") ]


template = '''isTest = {isTest} #### CHANGE HERE

dtype = 'CL'
if {isMC} : dtype = 'MC'

import os, sys
root = os.getenv("B2KTAUMUROOT")
if root is not None : sys.path.append( root+"/Options" )
sys.path.append(os.getcwd())

import B2KTauMuOption as opt
from DV_Config import ConfigDaVinci

opt.setalgs({isMC},'{decay}')
ConfigDaVinci(dtype,{year},opt.algs,Mag='{mag}',RootInTES="Leptonic",restrip=[],isTest=isTest)
'''

def CreateJob(dataType,decay,year,mag,local = False) :
    
    jname = '{type}{year}_{dec}_{mag}'.format(dec=decay,year=year,type=dataType,mag=mag)
    print "Preparing", jname
    j = Job(name = jname, backend=Dirac())
    if local : j.backend = Local()
    
    DaVinci_dirname = "./DaVinciDev_v42r3"
    if os.path.exists(DaVinci_dirname): 
        myApp = GaudiExec()
        myApp.directory = DaVinci_dirname
    else :
        myApp = prepareGaudiExec('DaVinci','v42r3', myPath='.')
    j.application = myApp
    #j.applicaton.useGaudiRun = True
    
    ### Make option file
    #if dataType == "MC" :
    #    myoption = template.format(isMC='True', mag=mag, year=year, decay=decay , isTest = local)
    #else :
    #    myoption = template.format(isMC='False', mag=mag, year=year.split('_')[0], decay='LEPTONIC', isTest = local )

    #foption = open('MyOption.py','w')
    #foption.write(myoption)
    #foption.close()
    #j.application.options = ['$PWD/MyOption.py']
    j.application.options = ['$B2KTAUMUROOT/Options/MyOption_Data.py']

    ### Find data
    datafile = root+'/Data/'
    if dataType == "MC": datafile += 'MC/';
    datafile += 'data_{dt}{y}_{decay}_{mag}.py'.format(
	    dt=dataType,y=year,decay=decay,mag=mag)
    
    if not os.path.exists(datafile) :
        print "Wrong datafile name: ", datafile
        return

    lfns = [ re.findall("LFN:.*?.dst",x)[0] for x in open(datafile).readlines() if 'LFN' in x and '#' not in x ]
    #lfns = [ re.findall("/afs.*?dst",x)[0] for x in open(datafile).readlines() if '#' not in x and '/afs' in x ]
    #if local : lfns = lfns[1:5]
    print lfns
    dataset = LHCbDataset(lfns)
    j.inputdata = dataset
    
    ### Finish initialisation
    j.inputfiles = options
    if dataType == "CL" : j.splitter = SplitByFiles(filesPerJob=100)
    elif not local: j.splitter = SplitByFiles(filesPerJob=20) # For MC if local, do not split

    f = MassStorageFile('*.root')
    j.outputfiles=[f]
    j.do_auto_resubmit = True
    
    return j

def DumpTestOption() :
    
    myoption = template.format(isMC='True', mag='MU', year='16' )
    foption = open('MyOption_DataTest.py','w')
    foption.write(myoption)
    foption.close()

def SubmitS28() :
    j = CreateJob('CL','LEPTONIC','16_S28','MU')
    j.submit()
    j = CreateJob('CL','LEPTONIC','12','MU')
    j.submit()
    j = CreateJob('CL','LEPTONIC','16_S28','MD')
    j.submit()
    j = CreateJob('CL','LEPTONIC','12','MD')
    j.submit()

def SubmitAll(datatype = 'CL', years=[], mags = ['MU','MD'], decays = [], test = False) :

    if datatype == 'CL' :
        #if years == []: years = ['11','12','15_S24r0p1','16_S28'] # Default years for data: all
        if years == []: years = ['11','12']#,'15_S24','16_S28']
        for year in years :
            for mag in mags :
                #j = CreateJob(datatype,'LEPTONIC',year,mag,test)
                j = CreateJob(datatype,'BHADRON',year,mag,test)
                #print j
                queues.add(j.submit)
    else :
        print "Submit MC"
	if decays == []: decays = decays_db # IF NO DECAYS ARE GIVEN, RUN OVER ALL DECAYS
	for decay in decays:
	    if years  == []: years_to_run  = decays_db[decay]['MC_samples'] # Default years for MC: what is available
	    else:            years_to_run  = years

	    for year in years_to_run:
		for mag in mags:

		    if test: 
		        print "TEST"
			print "Decay:  {0}".format(decay)
			print " Year:  {0}".format(year)
			print "  Mag:  {0}".format(mag)

		    else:
		        j = CreateJob(datatype,decay,year,mag,test)
			queues.add(j.submit)



