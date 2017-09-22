#dictionary for all the tags
MC_tags = {"16" : {	"MU" 	: 	
			    {"DDDB"		:	"dddb-20150724",
			    "CONDDB" 	:	"sim-20161124-2-vc-mu100"},
			"MD"	:	
			    {"DDDB"		:	"dddb-20150724",
			    "CONDDB" 	:	"sim-20161124-2-vc-md100"}
		    },
	    "12" : {	"MU" 	: 	
			    {"DDDB"		:	"dddb-20130929-1",
			    "CONDDB" 	:	"sim-20130522-1-vc-mu100"},
			"MD"	:	
			    {"DDDB"		:	"dddb-20130929-1",
			    "CONDDB" 	:	"sim-20130522-1-vc-md100"}
		    }


	    }


def get_MC_tag (year, magPol, tag):
	try:
		tag = MC_tags[year][magPol][tag]
		return tag
	except:
		print "Error! Tag not found! Is the year, the polarity or the requested tag not existing?"
		return None
