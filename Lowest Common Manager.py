"""
  Lowest Common Manager ☆
  You're given three inputs, all of which are instances of an OrgChart class that have a directReports property
  pointing to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance that
  isn't anybody else's direct report), and the other two inputs are reports in the organizational chart. The two reports are
  guaranteed to be distinct.
  Write a function that returns the lowest common manager to the two reports.

  Sample Input
     // From the organizational chart below.
     topManager = Node A
     reportone = Node E
     reportTwo = Node I
     tree  =    A
              /   \
             B      C
            / \    /  \
           D    E  F   G
         / \
        H   I

  Sample Output
    Node B

"""

# SOLUTION 1

# O(n) time | 0(d) space where n is the number of people
# in the org and d is the depth (height) of the org chart
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo). lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)

class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

# This is the input class.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
