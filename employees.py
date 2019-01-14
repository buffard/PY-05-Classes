# 1. Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

class Employees:
  def __init__(self, name, job_title, start_date):
    self.name = name
    self.job_title = job_title
    self.start_date = start_date

# 2. Copy this Company class into your module.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

        self.employees = list()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above

# 3. Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

  # did this on line 18 ie- self.employees = list()

# 4. Create a company, and three employees, and then assign the employees to the company.

ovation = Company("Ovation", "6/6/66")

samuel = Employees("Samuel", "Dev", "10/1/18")
ryan = Employees("Ryan", "Tanay", "2/1/18")
charisse = Employees("Charisse", "Lambert", "000000000")

ovation.employees = samuel
ovation.employees = ryan
ovation.employees = charisse

print("The company is", Company.get_company_name(ovation))