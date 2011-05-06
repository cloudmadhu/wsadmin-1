execfile("common.py")
import time
import java

# print cellName
cellName=getCellName()
cell = AdminConfig.getid('/Cell:'+ cellName + '/')
cells = AdminConfig.list("Cell").split(lineSeparator)
cellName = AdminConfig.showAttribute(cell, "name")

nodeEntries = AdminConfig.list("Node", cell).split(lineSeparator)
sec = getConfigId("cell", "" , "" ,"Security")
globalSec= AdminConfig.showAttribute(sec, "enabled")

for cell in cells:
	for nodeEntry in nodeEntries:
		nodeName = AdminConfig.showAttribute(nodeEntry, "name")
		nodeAttributes = "[-nodeName " + nodeName + "]"
		sVersion = AdminTask.getNodeBaseProductVersion(nodeAttributes)		
		oS = AdminTask.getNodePlatformOS(nodeAttributes)
		serverEntries = AdminConfig.list("ServerEntry", nodeEntry ).split(lineSeparator)			 	    
 	    	for serverEntry in serverEntries:
        		serverName = AdminConfig.showAttribute(serverEntry,"serverName")
			server = getConfigItemId("node", nodeName, "Server", serverName)
			clusterName = AdminConfig.showAttribute(server,"clusterName") 
       			javaVirtualMachineList = AdminConfig.list("JavaVirtualMachine", server)
	        	javaVirtualMachineEntries = strToList(javaVirtualMachineList)
	       		initialHeapSize = -1
		        maximumHeapSize = -1
             
			for javaVirtualMachineEntry in javaVirtualMachineEntries:
			   	    maximumHeapSize = AdminConfig.show(javaVirtualMachineEntry, "maximumHeapSize")
			       	    maximumHeapSize = maximumHeapSize[17:-1]
			            maximumHeapSize = int(maximumHeapSize)
			            if maximumHeapSize == 0:
						maximumHeapSize = 256
			for javaVirtualMachineEntry in javaVirtualMachineEntries:			
				initialHeapSize = AdminConfig.show(javaVirtualMachineEntry, "initialHeapSize")
				initialHeapSize = initialHeapSize[17:-1]
				initialHeapSize = int(initialHeapSize)
				if initialHeapSize == 0:
					initialHeapSize = 50		   							       
				deployedApplications = AdminConfig.showAttribute(serverEntry, "deployedApplications")
				#print "deployedApplications=" + repr(deployedApplications)
				lengthDeployedApplications = len(deployedApplications)
				try:
					deployedApplicationsList = deployedApplications.split(";")
				except:
					exceptionInfo( sys.exc_info())	
				lengthDeployedApplicationsList = len(deployedApplicationsList)
				#print "lengthDeployedApplicationsList=" + repr(lengthDeployedApplicationsList)
				for deployedApplication in deployedApplicationsList:		    			
					lengthDeployedApplication = len(deployedApplication)
					deployedApplicationList = strToList(deployedApplication)
					for deployedApplicationItem in deployedApplicationList:
						lengthDeployedApplicationItem = len(deployedApplicationItem)
						deployedApplicationItemList = deployedApplicationItem.split("/")
						deployedApplicationItemAppName = deployedApplicationItemList[2]
						deployedApplicationItemEarName = deployedApplicationItemList[0]
						runserv = AdminConfig.getObjectName(server)
						if len(runserv) > 0:
							state = AdminControl.getAttribute(runserv, 'state')
							print cellName + "," + nodeName + "," + str(clusterName) + "," + serverName + "," + state + "," + repr(initialHeapSize) + "," + repr(maximumHeapSize) + "," + deployedApplicationItemAppName + "," + deployedApplicationItemEarName + "," + sVersion + "," + oS 
						else:
							print cellName + "," + nodeName + "," + str(clusterName) + "," + serverName + "," + "NOT RUNNING" + "," + repr(initialHeapSize) + "," + repr(maximumHeapSize) + "," + deployedApplicationItemAppName + "," + deployedApplicationItemEarName + "," + sVersion + "," + oS						
print cellName + "," + "GLOBAL SECURITY is currently " + "," + globalSec
sys.exit(0)		
				
