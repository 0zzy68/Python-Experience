#Instantiate Constants
FED_STATE_TAXES = 0.265
OASDI_EMP = 0.062

class Employee:
	def __init__(self, pID, pName):
		#data attribute
		self.__name = pName
		self.__id = pID

	def __str__(self): #method gets called through the mechanism of class and python
		strOutput = ("Employee ID: " + + " " + self.pName + " (ID: " + self.__id + ")")#str output phrase
		return strOutput
	
class SalariedEmp(Employee):
	def __init__(self,pID,pName, pSal):
		self.__name = pName
		self.__id = pID
		self.__sal = pSal

	def getSalary(self):
		return self.__monthly_salary
	def setSalary(self, pSalary):
		strConfirm = ''
		if type(pSalary) == float or type(pSalary) == int:
			self.__salary = pSalary
			print('Salary value updated')
		else:
			print('Invalid number, salary not updated')
	def getPayroll():
		monthlySal
		taxes = ((OASDI_EMP * monthlySal) +(FED_STATE_TAXES * monthlySal))
		netPay = monthlySal - taxes
		
	def __str__(self):#method gets called through the mechanism of class and python
		strOutput = ("Employee ID: " + + " " + self.pName + " (ID: " + self.__id + ")\n" + "-------Monthly net salary: $" + monthlySal)#str output phrase
		return strOutput

class CommissionEmp(Employee):
	def __init__(self,pID,pName,pSal,pCommission):
		self.__name = pName
		self.__id = pID
		self.__sal = pSal
		self.__commision = pCommission

	def getPayroll():
		weekly_sal
		taxes = ((OASDI_EMP * weekly_sal) +(FED_STATE_TAXES * monthlySal))
		netPay = monthlySal - taxes

	def __str__(self): #method gets called through the mechanism of class and python
		strOutput = ("Employee ID: " + + " " + self.pName + " (ID: " + self.__id + ")\n" + "-------Net pay this week: $" + netPay)#str output phrase
		return strOutput
