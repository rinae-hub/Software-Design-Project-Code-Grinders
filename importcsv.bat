call C:\Users\HP\venv\Scripts\activate
py manage.py shell
import csv
from web.models import student


count = 0
with open('Output.csv') as file:
        reader = csv.reader(file)
		if count >0:
			for row in reader:
				students =student(YearStarted = row[0],RegistrationStart = row[1],RegistrationEnd = row[2],PlanCode = row[3],PlanDescription = row[4],Majors = row[5],StudentNumber = row[6],Streamline = row[7],ProbOfMatheStreamline = row[8],ProbOfPhysicsStreamline = row[9],ProbOfEarthStreamline = row[10],ProbOfBioStreamline = row[11],ProbOfUnknownStreamline = row[12],FirstYearSubjects =row[13],AggregateYOS1 =row[14],ProgressOutcomeYOS1 = row[15],FirstYearOutcome =row[16],SecondYearSubjects =row[17],AggregateYOS2 =row[18],ProgressOutcomeYOS2 = row[19],SecondYearOutcome = row[20],ThirdYearSubjects = row[21],AggregateYOS3 =row[22],ProgressOutcomeYOS3 = row[23],FinalOutcome = row[24],UnknownYearSubjects = row[25],Aggregate = row[26],Qualified = row[27],NumberOfYearsInSystem = row[28],RaceDescription = row[29],Language = row[30],Gender = row[31],Homeprovince = row[32],Homecountry = row[33],AgeAtFirstYear = row[34], AgeatDropOutORGrad = row[35],SchoolQuintile = row[36],isRuralorUrban = row[37],LifeOrientation = row[38], MathematicsMatricMajor = row[39], MathematicsMatricLit = row[40],AdditionalMathematics = row[41],EnglishFirstLang = row[42],EnglishFirstAdditional = row[43],ComputerStudies = row[44],NBTAL = row[45],NBTMA = row[46],NBTQL =row[47],AdditionalLanguage =row[48],Statistics = row[49],Accounting = row[50],OverallAggregate =row[51],Agriculture =row[52],Music = row[53],ArtDesign =row[54],CraftSpeechDrama =row[55],Electrical =row[56],Mechanical = row[57],Civil = row[58],BusinessEconomics =row[59],ReligiousStudies = row[60],PhysicsChem =row[61],InternationalRelations =row[62],Geography =row[63],Hospitality = row[64],History =row[65],Politics = row[66],LifeSciences =row[67],ForiegnSubject =row[68])
				students.save()
		count + = 1
	
       