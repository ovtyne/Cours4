class Vacancies:
    def __init__(self, title, url, salary, description, platform=""):
        self.title = title  #
        self.url = url
        self.salary = salary
        self.description = description

        if platform in ['HH', 'SJ']:
            self.platform = platform  #hh или sj
        else:
            if url[10, 12] == 'hh':
                self.platform == 'HH'
            else:
                self.platform == 'SJ'






