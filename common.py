def getCellName():
	global AdminConfig
	global AdminControl
	cell = AdminConfig.list("Cell")
	return AdminConfig.showAttribute(cell,"name")
#endDef

def getConfigItemId (scope, scopeName, objectType, item):
	global AdminConfig
	scope = scope.title()
	#debug("DEBUG: scope=" + repr(scope))
	#debug("DEBUG: scopeName=" + repr(scopeName))
	#debug("DEBUG: objectType=" + repr(objectType))
	#debug("DEBUG: item=" + repr(item))
	if (scope == "Cell"):
		configItemId = AdminConfig.getid("/Cell:"+scopeName+"/"+objectType+":"+item)
	elif (scope == "Node"):
		configItemId = AdminConfig.getid("/Node:"+scopeName+"/"+objectType+":"+item)
	elif (scope == "Cluster"):
		configItemId = AdminConfig.getid("/ServerCluster:"+scopeName+"/"+objectType+":"+item)
	elif (scope == "Server"):
		configItemId = AdminConfig.getid("/Server:"+scopeName+"/"+objectType+":"+item)
	#endIf
	#debug("DEBUG: configItemId=" + repr(configItemId))
	return configItemId
###################################################################################
def strToList(inStr):
        outList=[]
        if (len(inStr)>0 and inStr[0]=='[' and inStr[-1]==']'):
                tmpList = inStr[1:-1].split(" ")
        else:
                tmpList = inStr.split("\n")  #splits for Windows or Linux
        for item in tmpList:
                item = item.rstrip();        #removes any Windows "\r"
                if (len(item)>0):
                        outList.append(item)
        return outList
#endDef  
###################################################################################
def exceptionInfo(sysdotexc_info):
	exc_type, exc_value, exc_tbck = sysdotexc_info
	print "The value supplied to the exception was:" +repr(exc_value)
	linenum = traceback.tb_lineno(exc_tbck)
	print "ERROR: Exception caught at line " + str(linenum)
	for line in traceback.format_tb(exc_tbck):
                     print line
	#endfor
#enddef
##################################################################################

def getConfigId (scope, scopeName, nodeName, objectType):
	global AdminConfig
	scope = scope.title()
	if (scope == "Cell"):
		confId = AdminConfig.getid("/Cell:"+scopeName+"/"+objectType+":/")
	elif (scope == "Node"):
		confId = AdminConfig.getid("/Node:"+scopeName+"/"+objectType+":/")
	elif (scope == "Cluster"):
		confId = AdminConfig.getid("/ServerCluster:"+scopeName+"/"+objectType+":/")
	elif (scope == "Server"):
		confId = AdminConfig.getid("/Node:"+nodeName+"/Server:"+scopeName+"/"+objectType+":/")
	#endIf
	return confId
#endDef
